# Governance


## Abstract

This document describes the first draft of the governance mechanisms
available to users of the Aeternity blockchain.


## Motivation

The Aeternity blockchain aims to provide tools to enable its participants
to govern themselves effectively. At the most basic level this means
giving them the ability to coordinate. We believe that

It is essential to note that governance is very much a human problem that
most likely cannot be "solved" purely by technical means. Therefore the
mechanisms should be understood as tools to facilitate the process of finding
consensus among humans.

## Background

### Voting

Voting is regarded to be the primary mechanism for governance and can be
effective in a number of cases but it is still very much unclear whether
it scales with todays societies, seeing as voting has been done,
historically speaking, in very small groups. Typically, participant would
expect the following properties from a voting system:

1. secrecy of their vote and plausible deniability
2. can check integrity, i.e. their vote was correctly recorded and counted
3. can check that all votes were correctly counted and only eligible voters
  included

Generally speaking, voting can be seen as a tool for information gathering
in the sense of »let's see what everyone thinks« and it most likely works
reasonably well for that use case. It gets problematic, when the gathering
of information and authoritative enforcment get conflated, as is the case
with many peoples expectations of the utility of voting. This can be
remedied by runoff voting, any iterative process in general, range voting
and a couple of others, which all increase the complexity of the voting
protocol significantly. The authoritative power given to votes is often
derived by the argument that it represents »the will of the people«, which
is a questionable argument at best, given that it is people who have
volition, while groups have choices at best.

The will of the people argument shows its weakness even more when one
considers that for many important decisions a simple majority is enough
to win a vote. see for example the recent referendum in Britain to leave
the EU, which was split at `Leave` 51.9% and `Remain` 48.1%. This almost
perfect split looks a lot more as if the people are completely indecisive
as to what the best course of action is, as opposed to acting with one
»will«, yet it was accepted as such.

The conflation of concerns can also be favourable under some circumstances
because it has a very clear user experience, in that it can end a stuck
discussion and allow interlocutors to move on. A vote here should be
understood as a last ditch effort to be tried after all collaborative
approaches failed to produce and acceptable outcome.


#### Voting in decentralized systems

In the context of decentralized, open systems guaranteeing that only eligible
voters participate is a non-trivial task, and even capturing what exactly
makes an eligible voter might be tricky. In a democracy people usually follow
the »one person one vote« doctrine, for companies votes might be weighted by
shares and for blockchains one could imagine it being the entity securing the
ledger, storing the ledger or using the ledger; and with the importance many
proponents of blockchains give to the »code is law« rule, smart contracts
could end up being considered eligible voters as well.

Since the identity problem has yet to be solved for decentralized systems,
an easy solution to prevent sybill attacks is the Proof of Stake approach,
i.e. weighting voting power of one identity by the amount of coins it owns.
One possible problem with this coin weighting approach might be that in the
future people with a lot of power might prevent votes which would enact a more
egalitarian system from succeeding. Another problem is that miners, who are
going to represent a substantive share of the stakeholders might not necessarily
be represented in fair manner if one assumes that they use a (substantial)
fraction of their mined coins to cover running costs.


#### Proof of Work

- allows miners to vote

#### Proof of Stake

- dash proposals gather ~25% masternode (~4500) votes
- even if we allow stake holders and miners to contribute (via pos and pow
  respectively) then there are still more groups of people: node operators,
  who validate the chains, and end users, both of which have who have no good
  way of voting. (Proof of Storage for node?)
- non expert can appeal to »meta-expert agreement«, i.e. most experts go with
  option one, therefore I should follow them


#### Delegated Proof of Stake/Liquid democracy

- direct democracy, flexible delegation, meta-delegation, and instant recall
- policy area specific representation
- the more expertise can be brought to bear on policy decisions, the more
  likely is it that these decisions will advance the common good
- »trustee model of representation, requires decision-makers to adhere to
  deliberative norms, and balances liquid decision-making in legislatures
  with an executive that reviews the formal feasibility of policies and
  moderates package deals between proposals from different policy areas.«[3]

#### Reputation

- prevent people from directly influencing others/propaganda
- (expertise =?more=) reputation (=?more= influence)

#### Forking

Having an inclusive approach when it comes to hard forks might ease a lot of the
pains surrounding them. This could mean that nodes have the capability to track
and interact with multiple forks at once. Or in general try not to frame it as
an us vs. them issue but as a collaborative, we have to solve this together.

Using votes to decide on forks could be seen as detrimental to this goal, since
a vote has loser by design—if you are not voting for me, you're voting against
me.


#### Exit costs

One of our goal is to make exit costs low, i.e. allow users to easily abandon
undesirable forks. But it can be argued that if people have very low exit costs
for a given system, then they incentive to vote according to their true beliefs,
which should be the main goal for any sort of vote, is lowered and in turn would
then render the vote pointless.

And while the exit costs for a single voter can be quite low, the costs a fork
imposes on a community can end up very high, especially when it results in two
persistent chains. Both forks will have a vested interest in keeping the »original«
name, code will have to be adjusted, wallets to be updated, nodes changed and
users will definitely end up being confused.


### Constitution

- what is allowed to be decided on
- rules on how to change rules are informed by expectations of what the outcomes
  should/could be


### Automatic protocol amendments

- need formal methods to guarantee integrity of constitution
- need to be implementation agnostic
- formal proof to generate code from
- auto updates, take away users right to choose
- default opt-in?


#### Coordination

Coordination game is easy when rules can be codified easily but it is unclear
how it works with different code changes when nobody oversees the process



### Atomic swaps

Atomic swaps lower the exit costs for users of chains or forks they do
not want to be a part of by providing a trustless way to exchange coins
across chains.

### Replay Protection

If a fork results in two persistent chains that end up coexisting then
an account which interacts with one of the two chains can end up in a
situation where transactions made on one chain can be replayed on the
second chain, if no replay protection is in place, or they might end up
making a transaction on the wrong chain since it might be unclear which
of the two forks they are interacting with if there exists no obvious
way to distinguish them or no way for clients to specify which of them
specificly they want to use.



## Specification

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).


### Protocol

### Replay Protection

commit to list of RFCs

### Atomic Swaps

The atomic swap protocol relies on time and hash locked transaction.
A spend transaction with a time lock prevents the coins transfered
from being accessed before the lock expires. Similarly, a hash lock
prevents coins from being spent unless a witness for a given commitment
can be supplied.

This is adopted from the protocol suggested by [TierNolan on bitcointalk](https://bitcointalk.org/index.php?topic=193281.msg2224949#msg2224949), except that we can reduce the initial
claim to just one transaction.

#### Time locks

[Tesseract](https://eprint.iacr.org/2017/1153.pdf) provides an algorithm
for choosing appropriate locking times, along with a proof of security for
the given parameters.

```
c_0 = number of blocks it takes for Pr[block reversal] being negligible
```

```
t_0 = base number of blocks to wait for protocol to time out (e.g. 1 week)
t_1 = (blockinterval_chain_1/blockinterval_chain_2)*t_0
s_0 = Ω(sqrt(t0))

delta_A = c_0 + t_0 + s_0
delta_B = t_1
```

These values should be understood as recommendations.

#### Swap Deposit

Alice initiates the protocol by choosing a random x. She hashes this random
x `H(x)` and publishes it via a `swap_deposit` transaction to Chain1:

```
to: PK_bob
amount: 10
commitment: H(x)
reclaim_after: current_blockheight() + Delta_a
```

***to*** SHOULD be a valid payment address.

***amount*** MUST less or equal than the available coins of the signer.

***commitment*** SHOULD be computationally binding and hiding to guarantee
that Bob cannot learn the value of `x`.

***reclaim_after*** SHOULD be calculated according to the formula given
above.


Once Alices' transaction is included in the blockchain and has sufficient
confirmations, Bob creates his `swap_deposit` tx to publish it to Chain2:

```
to: PK_alice
amount: 10
commitment: H(x)
reclaim_after: current_blockheight() + Delta_b
```

It is in Bob's interest to make sure that `Delta_a >> Delta_b`, otherwise
Alice can wait for her lock to expire, reclaim her coins on Chain1 and then
claim coins on Chain2.


#### Swap claim

At this point Alice waits for sufficient confirmation of Bob's transaction.
She can then publish a `swap_claim` tx on Chain2:

```
deposit_id: $DEPOSIT_B_ID
witness: x
```

***deposit_id*** MUST refer to a valid transaction hash.

***witness*** SHOULD be the witness for the commitment referred to by the
deposit_id.

A miner seeing this transaction will then credit Alices' account on Chain2
and once it is observed by Bob, he can issue a similar transaction on Chain1

```
deposit_id: $DEPOSIT_A_ID
witness: x
```

Alice or Bob might not have any funds on Chain2 or Chain1 respectively, so
we  could consider deducting the transaction fees for the `swap_claim` directly
from the `swap_deposit`.

Since Bob chose a `Delta_b` much smaller than `Delta_a` neither party can
cheat,  because Alice can not claim the deposit on Chain2 without revealing
secret x and if she refuses to reveal the secret both will just have to wait
for the time lock to release.

### AEIP

#### Add proposal

### Voting

#### Delegate

#### Recall

## Storage



## (possible) Future(s)


### Atomic Swaps

In the case that both chains support Schnorr signatures, an atomic swap
could be condensed to a simple spend transaction with [adaptor signatures](https://scalingbitcoin.org/stanford2017/Day2/Using-the-Chain-for-what-Chains-are-Good-For.pdf).

### Reputation

Sabater, Jordi, and Carles Sierra. "Regret: A reputation model for gregarious societies." Fourth workshop on deception fraud and trust in agent societies. Vol. 70. 2001.

### Quadratic Voting

### Curation lists/markets


## References

[1] https://scalingbitcoin.org/stanford2017/Day2/Changes-without-unanimous-consent.pdf

[2] Cheryl Boudreau, ‘Making Citizens Smart: When Do Institutions Improve Unsophisticated Citizens’ Decisions?’, Political Behaviour 31 (2009), pp. 287-306

[3] Blum, Christian, and Christina Isabel Zuber. "Liquid Democracy: Potentials, Problems, and Perspectives." Journal of Political Philosophy 24.1 (2015).




