# Polling System

This document describes a polling system, that will be used as one of the
signal sources to influence the governances processes around Aeternity.
Signal meaning that these polls are not part of a formal on-chain governance
process but are meant to inform—provide signals for—decisions made off-chain.
That is, the polls are not formally binding but, to some degree, socially
binding, if all parties involved end up taking them seriously.
We chose this approach, because we believe that giving a particular group of
participants, here accounts with coins, exclusive say over governance processes
is not the right approach, given that wealth is not equally distributed and
would thus just reinforce existing power imbalances. Further, it is still very
much unclear how all the various processes required can be effectively
represented on-chain without having to fall back to centralising some decision
making power.
And last, designing and deploying a voting system, that has all the characteristics required to make them usable, secure and verifiable is a
notoriously hard problem.

This polling system uses an accounts' available coins to weight their selected
preference, e.g. an account with 1000 coins contributes 1000 votes while a
different account with 500 coins contributes just 500 votes.


## Specification

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to
be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).


### Overview

The polling system is kept simple since a more complicated approach would most
likely not increase the quality of the signals generated.
Keeping it simple here means that a participant will always use their full stake
when participating in a poll and delegation can only be done for either
individual polls or all at once.

Our polling system supports delegation for two reasons:

- security
- signal quality

The security argument is that a user might have a cold wallet, which holds most
of their coins and should thus only rarely be used, and and a hot wallet, that
holds less coins and is used regularly. Now with delegation, they can have their
cold wallet delegate its voting weight to the hot wallet. This then means the
hot wallet can vote with the combined weights, without requiring the cold wallet
to be used.

Participating in the decision processes typically requires a significant time
investment in order to be able to assimilate all the information needed to
properly assess all possible choices. While certainly possible, it is unlikely
that everyone who wants to get involved has the necessary resources. With
delegations, users can engage in a sort of trade. Those who might have the
expertise—or time to absorb all the required information–can trade it for voting 
weight from others, who possibly have a bigger stake available but not the time
or ability to make an informed choice.

We assume that delegation chains will be fairly short and that cycles are a
feature, not a bug.
Long chains would most likely imply a great deal of uncertainty as to who can
be considered an expert for a given topic or is generally knowledgeable. If we
consider the inverse case, where there is little or no uncertainty over
competence levels, there would be no reason to have long chains as opposed to
people just directly delegating their votes to the experts.

The existence of delegation cycles is a no-op, i.e. it has no influence given
that none of the involved parties end up with more voting weight. But finding
cycles is interesting in so far as it can suggest a more general problem with
the distribution of information, given that it suggests a lack of consensus as
to who can be trusted to make decisions—or exposes a bad faith actor somewhere
along the chain.
Cycles can be broken easily, too, since a vote overrides a delegation.

### Example

Polling systems should be familiar to most readers but the following are the
steps a poll will go through:

1. The poll is created
2. Accounts can participate in the poll or delegate their stake to another
   account
3. The poll closes
4. The poll is updated with the final result after resolving all delegations 


### Storage

Every poll stores the data of its creation plus a list of the delegations, votes
cast and eventual results:

- `id`: id
- `end_height`: block_height
- `summary`: string
- `reference`: string
- `options`: [string]
- `meta`: [byte]
- `delegations`: tree
- `votes`: tree
- `results`: [uint]

These entries are stored in a Merkle Patricia Tree, which holds all polls.

For a description of the `end_height`, `summary`, `reference`, `options` and
`meta` fields please see the [`create` message](#create).

The `delegations` field holds the delegations for this specific poll. A
delegation here is a mapping from one `account_id` to `[account_id]`. That is,
a mapping from delegatee to delegators.

Votes are recorded in the `votes` field. A vote is mapping from an `account_id`
to a `uint`, which is the index of one of the available `options`. Indexing
starts at `0`, i.e. the first entry of a list has index `0`.

After the poll is closed, the `results` list will be a filled with the sums of
coins put towards the individual options. The `results` list MUST be the same
length as the `options` list.
For example, if we have `["Yes", "No", "Abstain"]` as options, then results such
as `[23500, 1700, 13050]` suggest, that `23500` coins were put towards `"Yes"`,
`1700` towards `"No"` and `13050` towards `"Abstain"`.


#### The `0` poll

The state tree for polls has a special entry, which holds all permanent
delegations. This entry has the id `0`:

- `id`: `0`
- `end_height`: `0`
- `summary`: `"This entry holds all permanent delegations"`
- `reference`: `""`
- `options`: `[]`
- `meta`: `[]`
- `delegations`: 
- `votes`: `{}`
- `results`: `[]`

This poll MUST NOT receive any votes and only stores delegations.


### Messages

- `create`
- `delegate`
- `vote`
- `revoke_vote`
- `revoke_delegation`


#### `create`

- `from`: account_id
- `nonce`: uint
- `ttl`: uint
- `fee`: uint
- `end_height`: block_height
- `summary`: string
- `reference`: string
- `options`: [string]
- `meta`: [byte]

Each poll MUST run for a finite time and the block_height MUST be at most
`floor(60 * 24 * 60/key_block_interval)` blocks ahead—that is about 60 days.
That is, once `end_height` is reached, no further votes can be cast.
The only exception to the above rule is the poll with the id `0`, which is used
as permanent storage for delegations and has an `end_height` of `0`.

The `summary` field SHOULD be a short and descriptive summary of the issue at
hand. If there is reference material to be considered then the `reference`
SHOULD contain a URI for that material.

The `options` SHOULD contain a list of statements from which participants can
choose one which they think is appropriate.

A poll is open for votes immediately after creation and once a poll has been
created, it cannot be deleted or stopped prematurely.


#### `delegate`

- `from`: account_id
- `nonce`: uint
- `ttl`: uint
- `fee`: uint
- `target`: account_id
- `poll`: poll_id  

The delegate transaction allows an account, as the name suggests, to delegate
its stake to a `target` account. The `target` SHOULD be a valid account id.
A delegation can be valid indefinitely or for a specific poll. To specify the
validity, the `poll` field is used. Its value MUST be either the id of an existing and running poll or the special `0` id, which indicates that the
delegation is valid for *all* polls.

If an account has delegated its stake to account `1` for an issue and
afterwards publishes a delegation to account `2` for all issues then the
previous delegation to `1` MUST still be considered valid. That is, the specific
overrides the general.

Even after delegating its stake for all issues, an account can still do vote in
a poll, effectively overriding the delegation for a specific poll.

If an account has voted in a poll and later, while the poll is still running,
decides to delegate its stake, then it must revoke its vote if wants the
delegation target to vote in that poll instead.


#### `vote`

- `from`: account_id
- `nonce`: uint
- `ttl`: uint
- `fee`: uint
- `poll`: poll_id
- `option`: uint

Participating in a poll is done by casting a vote for one of the poll's options.
The `poll` MUST be an existing and open poll, with the `option` field
specifying the index of the chosen option. Indexing starts at `0`, i.e. to
select the second option, a vote would set the option field to `1`.

A vote will record the `from` accounts full balance as being put towards the
indicated option once the votes are tallied after the poll closed.


#### `revoke_vote`

- `from`: account_id
- `nonce`: uint
- `ttl`: uint
- `fee`: uint
- `poll`: poll_id

In the case of a change of mind, it is possible to revoke a vote. The `poll`
MUST be an existing and open poll.


#### `revoke_delegation`

- `from`: account_id
- `nonce`: uint
- `ttl`: uint
- `fee`: uint
- `target`: account_id
- `poll`: poll_id

Delegations can be revoked at any time by issuing this transaction. The `target`
MUST have received a delegation prior to the `revoke` and the `poll` value MUST
be be either the id of an existing and running poll or the special `0` id.


### Vote tallying

Once the `end_height` is reached, votes need to be tallied. The tallying process
will use an accounts' balances at `end_height` for counting.
The process itself comes down to reconstructing the directed delegation graphs, which are trees rooted each at one of the available options, with possibly cycles disconnected from the trees.



is fairly simple, although it can potentially involve a
significant of database queries, given that all delegations need to be resolved.

Given that a vote overrides a delegation and a delegation for a specific poll
overrides a delegation for a single poll, we start with the specific poll and
then fill in the rest from the permanent delegations. Our process looks as
follows:

1. Gather the `account_id` of all participants from the votes and add them as
   children to the roots. 
2. Look up the `account_id`s in the delegation map for the poll
	- if the account is a delegatee, collect the delegators, remove already
	  visited nodes and add them as children to the delegatee
	- otherwise it is a leaf and can be added without further actions
3. Continue with step 2. until all delegations are resolved
4. Take all nodes identified in the previous steps and restart at step 2 with
   them as initial nodes, this time checking the delegations in the special `0`
   id poll, ignoring duplicate connections
5. With the fully reconstructed trees, look up all the account's balances and
   either start at the leaves or roots and sum up all balances per root
6. Update the poll `results`

