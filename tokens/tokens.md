# Native Tokens

A native tokens is made up of two parts: a Native token type and a native token balance.

Native tokens types are a first class object on the chain that defines the
behaviour of a type of tokens. Native tokens live in their own account balances
of accounts.

Native tokens (from now on just tokens) are:
- Transferable (`spend`, `trade`)
- Countable
- Mintable (`mint`)
- Destroyable (`burn`)

Token types are:
- Creatable


## Token transactions

There is one transaction on token types:
- create

There are five token transactions:
- mint
- spend
- trade
- burn
- finalize

Other transactions that takes a balance can also take a native token balance.

### token create transaction

The token create transaction takes the following argument
- Meta data : string
and the following optional arguments
- Contract
- Amount
- Recipient
- Parent
- Final

The `meta data` is an uninterpreted string but token minters are encouraged to
use the following json object:
{
  "type" : "object",
  "properties": {
    "name": {"type" : "string"},
  }
}

The `contract` has to provide the following ACI:
 spend(recipient : address, payload : Type) : boolean
 trade([(from : address, to: address, Optional(token : address))], payload : Type)
 mint(amount: integer)
 burn(amount : integer) : boolean

The `amount` is the number of tokens to create.

The `recipient` an account to dump the tokens created, if not given the tokens are
spent to the creators account.

The `parent` is a pointer to a parent token for hierarchical tokens.

The `final` argument sets the final flag which would block future minting.

If a contract is provided then any transaction (spend, trade, mint, burn) would
call this contract and the transaction only goes through if the result of the
corresponfing contract call returns true. Any other transaction using
the token (such as contract call) would only be ececuted if a call to spend
returns true.
