# Aeternity Native Tokens

## Overview

We need to distinguish between a specification of a token, and a
countable amount of the token.  In this document we use **ANT**
(Aeternity Native Token) to represent the specification, and **native
token** or simply **token** to represent the countable asset.

Informally, when you need a new type of token for whatever purpose,
you create an ANT describing the token, and then you can mint new
tokens and start sending them to accounts.

Owners of the tokens can spend them to other accounts, or trade them
(atomically) for other assets with other accounts. If tokens are no
longer wanted you can burn them.

Only the owner of the ANT can mint new tokens. Only the owner can
finalize the ANT, preventing more minting. An ANT can also be
created with a final supply already minted.

An ANT can only be destroyed (TODO: design decision) if the total
token supply of the ANT is zero (i.e., all tokens are burnt).

Aeons are not part of the ANT system. There are no consensus
controlled exchange rate between tokens and aeons. Fees cannot be
payed by native tokens, but only by aeons. Other services could be
payed for with tokens (e.g., contracts accepting tokens as
payment). (TODO: Design decision: Should oracles be allowed to set
fees in tokens?)

The owner of a token can decide to govern the behavior of the tokens
by connecting a contract when an ANT is created. The contract must
provide entrypoints according to a specified ACI where one or many of
the primitive operation (spend, trade, mint, etc) is called to decide
if the operation is allowed or not.

## Definitions

Note that when *account* is used below, the account can belong to a
contract, the account may be an oracle, etc.

An Aeternity Native Token (ANT):
- is a *specification* of tokens
- is a *first class object* on the chain with its own state tree
- is *created* by an account which becomes its owner
- *governs the behavior* when interacting with tokens (trading, sending, minting, etc).
- can have a *connected contract* to govern the handling of its tokens

A native token:
- has an ANT describing its behavior.
- is *countable*
- is recorded as a *balance in the account* that owns it (in the accounts state tree).
- is *mintable* (`mint`)
- is *transferable* (`spend`, `trade`)
- is *destroyable* (`burn`)

## Tokens state tree

The tokens state tree contains ANT objects. Tokens are stored in the
accounts state tree in the owner's account.

### ANT object

The token id is determined by the creator's account and nonce.
```
  id := Blake2b(<CreatorPubkey><CreateTxNonce>)
```
where `Blake2b` is the 256 bit hash. The [API
serialization](../node/api/api_encoding.md) of an ANT id is tagged by
`nt_`

The ANT contains the fields:
- `creator` - The account id of the creator
- `meta_data` - A byte array field, uninterpreted, but under consensus
- `contract` - A contract id if there is a governing contract, or the empty binary otherwise
- `total_supply` - A counter of the currently available amount of the token
- `parent` - The id of the parent ANT (TODO: Hierarchical tokens?)
- `final` - If the ANT is final, new tokens cannot be minted. Can flip to true, but never back to false again.

The `meta data` is an uninterpreted string but token minters are
encouraged to use the following json object: (TODO: Extend).  The
intention of the meta data is to have a consensus controlled way of
providing information usable by tools (e.g., displaying an intended
denominator, a display name, etc).
```
{
  "type" : "object",
  "properties": { "name": {"type" : "string"},
                }
}
```

A contract governing the usage of tokens must have a non-empty subset
of the following ACI:

```
 spend(recipient : address, payload : Type) : boolean
 trade([(from : address, to: address, Option(token : address))], payload : Type) : boolean
 mint(amount: integer) : boolean
 burn(amount : integer) : boolean
```

The contract may contain other endpoints as well, but at least one of
the entrypoints above must be implemented. The contract can only be
attached at create time.

If a contract is provided, any transaction (spend, trade, mint, burn)
would call this contract and the transaction only goes through if the
result of the corresponding contract call returns true. Any other
transaction using the token (such as contract call) would only be
executed if a call to spend returns true. (TODO: Decide how this plays
with contract calls that tries to pass tokens as value, etc).

## ANT transactions

### ANT create transaction (`ant_create_tx`)

The ANT create transaction takes the argument:
- Meta data : string
- Amount
- Recipient
- Final
- Contract
- Parent  (TODO: Hierarchical tokens?)

The `amount` is the number of tokens to mint at create time. Set to
`0` if none should be minted. This can for example be combined with
setting the `final` argument to true, thereby immediately minting all
tokens that will ever exist.

The `recipient` is the recipient of the minted tokens in `amount`. If
not provided, the tokens are given to the creator's account.

The `parent` is a pointer to a parent token for hierarchical
tokens. (TODO: hierarchical tokens?)

### ANT finalize transaction (`ant_finalize_tx`)

The ANT finalize transaction takes the arguments:
- owner
- ANT

The finalize transaction can only be submitted by the actual owner,
and only if the ANT is not already finalized.

### ANT mint transaction (`ant_mint_tx`)
The ANT mint transaction takes the argument:
- owner
- ANT
- amount
- recipient
- final

Only the `owner` can mint new tokens, but it can pass the minted
tokens to a recipient. If `final` is set to true, the ANT will be
finalized after the new tokens are minted.

### ANT destroy transaction
TODO: Should we be able to destroy an ANT that has a `total_supply` of 0?


## Token transactions

### Token trade transaction
The token trade transaction takes the argument:
- trades

The `trades` field contans a non-empty list of token transfers. A
single token transfer consists of the fields:

- Sender
- Receiver
- Amount
- An ANT id

This construct makes it possible to atomically perform complicated
trade operations involving more than one ANT and also aeons (TODO: How
to signal that a trade concerns aeons) between multiple parties.

The transaction must be signed by all senders. (TODO: Should we use
some alternative multisig format here?).


### Token burn transaction

The token burn transaction contains the fields
- Account (owner of the tokens, not necessarily of the ANT)
- Amount
- ANT

Destroy an `Amount` of `ANT` tokens currently owned by the
`account`. The burned amount is also counted from the `total_supply`
in the ANT object.

### Other transactions on tokens

Tokens can also be transfered from one account to another through any
other transaction that can pass an amount. You can:
- spend tokens through the `spend_tx`
- pass tokens as value in a `contract_call_tx` or `contract_create_tx`
- pass tokens as value in contract calls in a smart contract.
- spend tokens as query fees in `oracle_query_tx` (TODO: Might be a future extension).
