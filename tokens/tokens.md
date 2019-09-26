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

Only the owner of the ANT can mint new tokens, and is the owner
decides that enough is enough, the ANT can be finalized, preventing
more minting. An ANT can also be created with a final supply already
minted and given to the owner of the ANT.

An ANT can only be destroyed (TODO: design decision) if the total
token supply of the ANT is zero (i.e., all tokens are burnt).

Fees cannot be payed by native tokens, but only by aeons, but other
services can be payed for with them. (TODO: Oracle query fees, etc?)

If you need to govern the behavior of the tokens, a contract can be
connected to the ANT. The contract has functions that will be called
for example when tokens of the type is traded. The result of the call
decides if the trade can happen or not.


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

## ANT transactions
An ANT can be:
- *created* through the `ant_create_tx`
- *finalized* through the `ant_finalize_tx`, preventing more minting.

## Token transactions

Tokens can be:
- *minted* through the `ant_mint_tx`.
- *destroyed* through the `ant_burn_tx`.
- *traded* atomically through the `ant_trade_tx`.

Tokens can also be transfered from one account to another through any
other transaction that can pass an amount. You can:
- spend tokens through the `spend_tx`
- pass tokens as value in a `contract_call_tx` or `contract_create_tx`
- pass tokens as value in contract calls in a smart contract.
- spend tokens as query fees in `oracle_query_tx` (TODO: Might be a future extension).

### ANT create transaction (`ant_create_tx`)

The ANT create transaction takes the mandatory argument:
- Meta data : string

The ANT create transaction takes the optional arguments:
- Contract
- Amount
- Recipient
- Parent  (TODO: Decide what impact this have. Possibly delay having hierarchical tokens)
- Final

The `meta data` is an uninterpreted string but token minters are encouraged to
use the following json object:
```
{
  "type" : "object",
  "properties": { "name": {"type" : "string"},
                }
}
```

The `contract` has to provide the following ACI:
```
 spend(recipient : address, payload : Type) : boolean
 trade([(from : address, to: address, Optional(token : address))], payload : Type) : boolean
 mint(amount: integer) : boolean
 burn(amount : integer) : boolean
```

The `amount` is the number of tokens to create.

The `recipient` an account to dump the tokens created, if not given the tokens are
spent to the creators account.

The `parent` is a pointer to a parent token for hierarchical tokens.

The `final` argument sets the final flag which would block future minting.

If a contract is provided then any transaction (spend, trade, mint, burn) would
call this contract and the transaction only goes through if the result of the
corresponfing contract call returns true. Any other transaction using
the token (such as contract call) would only be executed if a call to spend
returns true.

## Tokens state tree

The tokens state tree contain token type objects.
Tokens are stored in the account state tree as a list of tuples of
token id:s and balances.

### Token state tree objects

- The token state tree contains
  - Token type objects

#### The token type object

- Created by an token create transaction.

```
{ creator         :: id()
, <meta_data>     :: binary()
, <contract>      :: id()
, <total_amount>  :: int()
, <parent>        :: id()
, <final>         :: bool()

}
```

