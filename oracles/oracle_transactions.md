# Oracle transactions

Oracle transactions are of four types:

- Register
- Extend
- Query
- Response

## Oracle register transaction

An oracle operator can register an existing account as an oracle.

The transaction contains:

- The address that should be registered as an oracle (oracle_owner) + nonce
- Query format definition
- Response format definition
- Query fee (that should be paid for posting a query to the oracle).
- A TTL (relative in number of blocks, or absolute block height)
- Vm version (see [VM description](../contracts/contract_vms.md)).
- Transaction fee.

See the [serialization specification](/serializations.md#oracle-register-transaction).

### TODO

- In the future we could imagine an oracle register transaction that
  creates a new account by double signing the request with the source
  account and the new account.

## Oracle extend transaction

An oracle operator can extend the TTL of an existing oracle.

The transaction contains:
- The address/oracle that should be extended (and a nonce)
- An extension to the TTL (relative to current expiry in number of blocks)
- Transaction fee.

See the [serialization specification](/serializations.md#oracle-extend-transaction).

## Oracle query transaction

- Contains:

  - The sender (address) + nonce
  - The oracle (address)
  - The query in binary format
  - The query fee - locked up until either:
    - The oracle answers and receive the fee
    - The TTL expire and the sender gets a refund
  - Query TTL
  - Response TTL
  - The transaction fee.

The transaction creates an oracle interaction object in the oracle
state tree. The id of this object is constructed from the query
transaction as the hash of {sender_address, nonce, oracle_address}

The query TTL decides how long the query is open for response from the
oracle.

The query TTL can be either absolute (in block height) or relative
(also in block height) to the block the query was included in.

The response TTL decides how long the response is available when given
from the oracle. The response TTL is always relative. This is to not
give incentive to the oracle to post the answer late, since the oracle
is paying the fee for the response.

See the [serialization specification](/serializations.md#oracle-query-transaction).

### Questions/Later

- We could include an earliest time that the oracle can answer to
protect against malicious oracles answering early and collect the fee.

## Oracle response

The oracle operator responds to a query by posting an oracle response
transaction, signing it with the oracle account's private key.

The response transaction is invalid if the TTL from the query has
expired.

The oracle pays the fee of the response transaction. The mininimum fee
is determined by the response TTL from the query and the size of the
response.

Note that there is an incentive to keep the response precise (and
small) since the oracle pays for the response transaction.

The transaction contains:

- The oracle (address) + nonce
- The oracle interaction ID (derived from the query)
- The response in binary format
- Response TTL (redundant, but makes the transaction self contained)
- The transaction fee.

See the [serialization specification](/serializations.md#oracle-response-transaction).

### Questions/Later

- Should we have an automatic callback defined in the query?
  - Any callback is paid by the oracle.
- Should we be able to return parts of the fee if the oracle for some
  reason could not provide an answer.
