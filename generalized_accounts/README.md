# Generalized accounts


## Motivation

Plain old accounts (POA) have very little flexibility when it comes to the
logic controlling them. While this results in a uniform user experience and
makes development easier, e.g. a wallet only needs to handle a single method of
accessing accounts, it also ignores that people may have varying needs when
managing their accounts.

This has led to a variety of smart contract wallets being developed, which can
enforce spending limits, enable more sophisticated authorization schemes via
multi-signatures and other things. The biggest drawback of this approach is the
need to still own a "normal" account, in order to invoke the smart contract and
pay for its execution.

Both of these issues, relying on a single private key and smart contracts not
being able to pay for their own execution, will be addressed by this proposal.

Generalized accounts (GA) are thus primarily introduced to improve the UX of the
system.


## Approaches

We give a brief overview of some of the different approaches, that would allow
for authorization logic to be more flexible.

They lie on a spectrum from the current fixed signature and nonce scheme to
having full fledged smart contracts.

When it comes to modifications required for transactions, there are two ways to
do it:

- change all current transactions such that instead of signatures/nonces, a more
  general `auth_data` is attached
- introduce a new transaction type `meta_tx`, that wraps a "normal" transaction
  with `auth_data` for a generalized account

In either case, signature logic will need to be touched, s.t. an empty signature
can be accepted.

Additionally, the more flexible authorization logic will make transaction
validation costlier and therefore also increase the associated fees.


### Side-effect free

A fairly non-invasive solution would be to attach a pure function to accounts.
This means that all relevant authorization code and data, e.g. public keys for
signature checks, have to be included directly in the function body and can not
be updated. Nonce handling would still be handled implicitly, i.e. stay
unchanged.

Making the authorization function optional ensures POAs to not be impacted.

The downsides of this would be the need to for special handling of the
authorization code because execution would not happen in the normal VM context
and thus likely end up with a lot of implementation complexity.

This approach would be a slight improvement over the status quo but still leave
a lot left to be desired, such as calling other contracts, enforcing dynamic
spending limits or more complex nonce handling.


### Full smart contracts

The far end of the flexibility spectrum is occupied by fully fledged smart
contracts, which can pay for their own execution.

Here POAs stay untouched and instead everything is handled by smart contracts.

The biggest downside is that initialising a smart contract requires a POA with
funds, because currently smart contracts cannot create other smart contracts.
In addition, the VM does not yet have to the ability to create all the available
transaction types.


### Hybrid

For the hybrid solution POAs and smart contracts stay separate, meaning that
accounts can still be used with the implicit nonce and signature authorization.
But accounts are extended with two new fields, allowing its owner to specify the
address of a smart contract and name of a function, which will be called
whenever a transaction needs to be authorised.
As soon as the new authorization contract is attached to an account, it is no
longer possible to author transactions with the old nonce plus signature method.


## Background

POAs and smart contract states are currently stored separately.

The only state transitions accounts can undergo are change of nonce and balance,
which always have to be authorised by producing a valid signature with the
private key belonging to the account id.

Smart contracts on the other hand can have arbitrary state associated with them,
where transitions are controlled solely by user defined logic.

All transactions can be abstracted in the following way:

```
 Fieldname       Size (bytes)
 -------------- -----
| from         | 32  |
 -------------- -----
| data         | var |
 -------------- -----
| nonce        | 32  |
 -------------- -----
| signature    | 64  |
 -------------- -----
```

with the `data` field containing the byte sequence making up the specific
transaction fields.
The signature is computed as `sign(hash(serialize(from||data||nonce)))`. It
guarantees integrity of the `data` and `nonce` fields, while the `nonce`
prevents replay of old transactions.

In addition to integrity, the signature is used to prove that the issuer knows
the private key for the public key specified in the `from` field, i.e. used as
authorization.

The above scheme is the only one natively supported via the POA.

If the authorization were to be abstracted as well, then we end up with:

```
 Fieldname       Size (bytes)
 -------------- -----
| data         | var |
 -------------- -----
| auth_data    | var |
 -------------- -----
```

which roughly corresponds to the newly introduced `meta_tx`, that wraps
transaction `data` into a smart contract call. This call uses the supplied
`auth_data` to assess whether the transaction is to be authorised or not by
the GA.


## Specification

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

## Overview

In order to convert a POA into a GA, an existing account will have to issue a
transaction similar to a contract creation, which associates a smart contract
with the POA.
After the conversion, a new meta transaction, that wraps a »normal« transaction,
will be used to interact with the GA. This meta transaction is always a smart
contract call and inner transactions will only be authorised if that call
returns true.

## Accounts

With the introduction of generalized accounts, the structure of the entries
stored in the account tree changes from:

```
 Fieldname       Size (bytes)
 -------------- -----
| nonce        | 32  |
 -------------- -----
| balance      | 32  |
 -------------- -----
```

to

```
 Fieldname       Size (bytes)
 -------------- -----
| nonce        | 32  |
 -------------- -----
| balance      | 32  |
 -------------- -----
| ga_contract  | 32  |
 -------------- -----
| ga_auth_fun  | var |
 -------------- -----
```

For the actual wire format please consult the [serialization](../serializations.md) document.

The `ga_contract` MUST be the identifier of a deployed contract or empty.
The `ga_auth_fun` MUST be the identifier of a function to be called or empty.

If the `ga_contract` field is not empty, then the `ga_auth_fun` field MUST NOT
be empty.

If `ga_contract` is not empty, then authorization MUST be done by calling the
`ga_auth_fun` of the contract located at `ga_contract`. The data provided to the
`ga_auth_fun` is supplied via a [`meta_tx`](#meta_tx). The `ga_auth_fun` MUST
return `true` for the authorization to succeed.

The `nonce` field is irrelevant if the account is a GA.

The `ga_contract` and `ga_auth_fun` fields MUST NOT go from non-empty to empty,
i.e. after a POA has been converted to a GA it cannot be undone.

The `ga_contract` and `ga_auth_fun` fields MUST NOT change after they have been
set once.

If the `ga_contract` field is empty, then authorization MUST be done via the old
verification of the signature attached to transactions. In this case, a
transaction MUST only be considered valid, if
	1. a signature is attached, that has been produced by the private key that
	   belongs to the account id
	2. the `nonce` included in the transaction is the successor of the nonce
	   stored in the account.


## Transactions

Two new transactions are introduced. The `ga_attach_tx` is used to convert a POA
into a GA by attaching code to it.
Afterwards the new `meta_tx` is used to interact with the GA.


### `ga_attach_tx`

```
 Fieldname       Size (bytes)
 -------------- -----
| owner_id     | 32  |
 -------------- -----
| nonce        | 8   |
 -------------- -----
| code         | var |
 -------------- -----
| auth_fun     | 32  |
 -------------- -----
| ct_version   | 4   |
 -------------- -----
| fee          | var |
 -------------- -----
| ttl          | 8   |
 -------------- -----
| gas          | var |
 -------------- -----
| gas_price    | var |
 -------------- -----
| call_data    | var |
 -------------- -----
```

For the actual wire format please consult the [serialization](../serializations.md) document.

The semantics of this transaction are almost identical to the [Create Contract Transaction](../contracts/contract_transactions.md#create-contract-transaction).
As such, only the additional logic not covered by the `Create Contract
Transaction` will be listed here.

The address for the contract, which holds `code`, will be computed just like
regular contract creation.

The `owner_id` is the POA, which will be converted into a GA, if the transaction
is valid. If the account at `owner_id` is already a GA, the transaction MUST be
considered invalid.

The transaction MUST include a signature created by the private key belonging to
the `owner_id`.

The `auth_fun` is a function hash as described in the
[Sophia](https://github.com/aeternity/aesophia/blob/master/docs/sophia.md)
section.

If valid, the transaction will set the `ga_contract` and `ga_auth_fun` of the
`owner_id` account.


### `meta_tx`

Before Iris, version 1:

```
 Fieldname       Size (bytes)
 -------------- -----
| ga_id        | 32  |
 -------------- -----
| auth_data    | var |
 -------------- -----
| abi_version  | 2   |
 -------------- -----
| fee          | var |
 -------------- -----
| gas          | var |
 -------------- -----
| gas_price    | var |
 -------------- -----
| ttl          | 8   |
 -------------- -----
| tx           | var |
 -------------- -----
```

After Iris, version 2:

```
 Fieldname       Size (bytes)
 -------------- -----
| ga_id        | 32  |
 -------------- -----
| auth_data    | var |
 -------------- -----
| abi_version  | 2   |
 -------------- -----
| fee          | var |
 -------------- -----
| gas          | var |
 -------------- -----
| gas_price    | var |
 -------------- -----
| tx           | var |
 -------------- -----
```

For the actual wire format please consult the [serialization](../serializations.md) document.

The semantics of this transaction are similar to the [Call Contract Transaction](../contracts/contract_transactions.md#contract-call-transaction).

A `meta_tx` is always a call of the `auth_fun` on the contract located at
`ga_id` with the supplied `auth_data`.

The `auth_fun` call MUST return true for the `tx` to be considered valid.

The `auth_fun` is a function hash as described in the [Sophia](https://github.com/aeternity/aesophia/blob/master/docs/sophia.md)
section.

The `ttl` is the maximum block height that could include the transaction. This
had changed from Iris hardfork and the innermost transaction's `ttl` is being
used instead.

The `tx`, or inner transaction, MUST be a well formed transaction with nonce set
to `0`. The `tx` MUST NOT be a `ga_attach_tx` transaction.

The `authorization` function is executed in a special FATE environment where
`Auth.tx_hash` and `Auth.tx` are available. These can (and should!) be used to
securely authorize a transaction. Note: `Auth.tx_hash` computation differs
between protocol versions, see [serialization](../serializations.md)
specification for details.

## Backwards compatibility

Going from POA to GA is entirely optional and both types of accounts can coexist
without problems.

## Discussion


### Threat model/attack vectors

Special care needs to be taken when writing contracts, that handle authorization
logic for a GA. If the contract does not enforce integrity checking or replay
protection, then it will be vulnerable to abuse.


### Example contracts

Some mechanisms, that we had in mind, as motivation for GA:

- spending limits (daily/weekly/...)
- spending limits per transaction type
- restrictions on transaction types that can be sent
- (social) recovery options
- multi-sig (e.g. phone + hardware wallet, or multiple people)
- using different signature algorithms (i.e. other than EdDSA)

GAs are further explained and an example is provided in [Generalized
accounts explained](ga_explained.md).
