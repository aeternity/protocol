[back](./oracles.md)
## Oracle transactions

### Oracle register transaction
- Contains:
  - The oracle "owner"
  - A unique oracle address (a public key - proof of priv key should be given?!)
  - Query format definition
  - Response format definition
  - Query fee
  - Transaction fee

Questions/Later:
- Exact format for queries (API).
  - Protobuf or something similar?
- Exaxt format for responses.
- Fee for posting a query. The fee can be 0.
  - Fees are flat to begin with.
  - We could imagine fees to be proportional to something.
- Should Oracles have a TTL?

```
{ oracle_owner    :: {public_key(), nonce()}
, oracle_address  :: public_key()
, query_format    :: format_definition()
, response_format :: format_definition()
, query_fee       :: amount()
, fee             :: amount()
(, ttl             :: time_in_msecs()) }
```

### Oracle query transaction
- Contains:
  - The sender (address) + nonce
  - The oracle (address)
  - The query in binary format
  - The query fee - locked up until either:
    - The oracle answers and receive the fee
    - The TTL expire and the sender gets a refund
  - Query TTL
  - Response TTL
  - The transaction fee

Questions/Comments/Later:
- The Transaction ID is the hash of {sender_address, nonce, oracle_address}
- Should the query format be checked by the miner?
- The size of this TX is variable (the Query), so fee/gas will vary - also the
sender will pay for storing the query, thus the TTL will also affect the
transaction fee.
- The query fee should cover the possibly variable size (response format) of
the response.
- The response TTL is how long the response will live in the state tree.
- What is a sensible default?
- Should the response TTL be refunded if there is no response?

```
{ sender_address  :: public_key()
, nonce           :: nonce()
, oracle_address  :: public_key()
, query           :: binary()
, query_fee       :: amount()
, query_ttl       :: time_in_msecs()
, response_ttl    :: time_in_msecs()
, fee             :: amount() }
```

### Oracle response
- Contains
  - The query ID
  - The response in binary format
  - The transaction fee
  - Response TTL

### Questions/Later:
- The response Transaction ID (if needed) is the hash of {query_id, response}.
- Should we have a notification?
  - Callback to the query?
- Any callback is paid by the oracle.
  - The oracle operator needs to use funds from the query fee.
  - Returned fee - If the oracle for some reason could not
    provide an answer it might want to return (part of) the fee?!
- Response should have a TTL?
- Note the oracle will pay for the payload (the response) so there is an
  incentive to keep it precise (and small).

```
{ query_id        :: tx_id()
, response        :: binary()
, fee             :: amount()
, ttl             :: time_in_msecs() }
```

(Open question: should there be a generic _DATA TX_ and should the Oracle
answer be a special instance of this transaction.)
