[back](./oracles.md)
## Oracle life cycle examples

### The football game results oracle

Alice is a big fan of football and she wants to share the results of games.

Alice registers an oracle by submitting a oracle register transaction
to the chain.

Alice pays a fee for submitting the transaction.

Alice needs to include some information in the transaction
- A query fee for covering her costs.
- A declaration of the query format.
- A declaration of the response format.

The oracle is created in the oracle state tree when the oracle
transaction is included in the chain.

Alice is running a node in the network. Alice registers a subscription
in her local node so she will be notified when someone posts a query
to her oracle.

Bob wants to use the result of a specific game on the block chain.

Bob finds Alice's oracle on the chain and posts a query transaction to
the chain.

Bob pays a fee for submitting the transaction. The fee is collected by
the miner.

Bob pays a fee posting a query to the oracle. The fee is transfered to
the oracle's account.

The query transaction contains:
- The address or Alice's oracle.
- A query in the format declared by Alice's oracle.
- A transaction fee for the miner.
- A transfer of coin to Alice's oracle.
- A TTL for the query (If Alice's oracle doesn't answer the query
  within the given time, Bob is refunded the coins)

The query transaction creates an oracle interaction object in the
oracle state tree. The id of the oracle interaction object is derived
from the query transaction.

Bob registers a subscription on a node (using the the oracle
interaction id) for getting notified when there is a response on his
query.

When Bob's query transaction gets accepted into the chain, Alice's
event subscription triggers and she gets notified that there is a new
query on the chain.

The event contains:
- The address of the sender account,
- The Id of the oracle interaction.

When the match has been played, and there is a result, Alice posts an
oracle response transaction on the chain.

The response transaction contains:
- The Id of the oracle interaction object.
- The result as defined in the oracle definition.

Alice pays a transaction fee for posting the transaction. The fee is
collected by the miner. And as part of the transaction Alice's oracle
receives the fee for the query.

When the response transaction has been accepted to the chain, Bob's
event subscription notifies him that there is a response.

The event contains:
- The Id of the oracle interaction object.
- The content of the response.
- The TTL of the response.

Bob can now use the response by:
- Executing a smart contract which references the oracle interaction object.
- Use a public API of a node to get the answer.
