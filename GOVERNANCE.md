# Governance


## Abstract

This document describes the first draft of the governance mechanisms
available to users of the Aeternity blockchain.


## Motivation

The Aeternity blockchain aims to provide tools to enable its participants
to govern themselves effectively.
It is essential to note that governance is very much a human problem
that most likely cannot be "solved" purely by technical means. Therefore
the mechanisms should be understood as tools to facilitate the process
of finding consensus among humans.

Thus, our goal is twofold, provide both technical tools to automate
processes that lend themselves to such automation and also frameworks for
human interaction.

## Background

### Voting

Voting is regarded to be the primary mechanism for governance and can be
effective in a number of cases but it is still very much unclear whether
it scales with todays societies, seeing as voting has been done,
historically speaking, in very small groups. Typically, a participant would
expect the following properties from a voting system:

1. secrecy of their vote and plausible deniability
2. can check integrity, i.e. their vote was correctly recorded and counted
3. can check that all votes were correctly counted and only eligible voters
  included

Generally speaking, voting can be seen as a tool for information gathering
in the sense of »let's see what everyone thinks« and it most likely works
reasonably well for that use case. It gets problematic, when the gathering
of information and authoritative enforcement get conflated, as is the case
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


#### Preventing sybil attacks

In the context of decentralized, open systems guaranteeing that only eligible
voters participate is a non-trivial task, and even capturing what exactly
makes an eligible voter might be tricky. In a democracy people usually follow
the »one person one vote« doctrine, for companies votes might be weighted by
shares and for blockchains one could imagine it being the entities securing the
ledger, storing the ledger or using the ledger; and with the importance many
proponents of blockchains give to the »code is law« rule, smart contracts
could end up being considered eligible voters as well.


#### Proof of Stake/Proof of Work

Proof of Stake voting again just like shareholder voting, where the weight of
a vote is given either by the balance of the identity doing the voting or the
amount of stake they are willing to commit to a vote.

With a Proof of Work scheme, miners could vote by including their preferences
in the blocks they produce, given that block production rate should be
proportional to available hashing power, this scheme would be similar to
shareholder voting.

Miners starting to enforce different consensus rules could be seen as a different
form of voting and again be information gathering and authoritative enforcement
of the vote, although miners will risk their blocks being rejected by the network
if they are in the minority if the rules are incompatible or less strict than
the rest.

Both of these schemes are problematic because they place even more power in the
hands of those people who already have a lot of power. One formula that has been
evoked in this context is that of »having skin in the game«, where it is argued
that people who have a lot of stake in a system have a vested interes in its well
being and thus are the ones who should have the biggest impact on decisions.
This is problematic because our goal is to build a system for end-users to use
and it is unlikely that the interests of these groups are aligned.

Another possible problem with these approaches might be that in the future people
with a lot of power might prevent votes which would enact a more egalitarian system
from succeeding.


#### Node operators

Node operators have no natural way of being included in an on-chain voting
process, since spinning up a node easy and thus does not prevent sybill attacks.
If updates are not automatic their mechanism to make a choice is simple, though:
just don't adopt the new software.


### Reputation

- prevent people from directly influencing others/propaganda
- (expertise =?more=) reputation (=?more= influence)

- if all experts agree on a change but the general userbase disagrees, who's in the right?

- non expert can appeal to »meta-expert agreement«, i.e. most experts go with
  option one, therefore I should follow them

- loss of reputation punishment for misbehaviour
- »trustee model of representation, requires decision-makers to adhere to
  deliberative norms, and balances liquid decision-making in legislatures
  with an executive that reviews the formal feasibility of policies and
  moderates package deals between proposals from different policy areas.«[3]


### Cooperation

- a lot of our political problems come from using political force to turn non-rivalrous
  matters into rivalrous matters, instead of coordinating consensus around rivalrous matters


- have to be in the clear what is exactly being voted upon, how it is evaluated and
  tradeoffs with other proposals

- votes should only be required for things that people can't reach consensus on
  i.e. uncontroversial changes really don't need any vote
- special interest groups only


- a simplification could also be to have a technical advisory board instead of a voting system. This advisory board would produce reports including all inputs that went into their decision and the resulting outputs, i.e. documenting the full process.
-> this process would be more about consent, e.g. asking users whether they can live with this decision (no objections) rather than convincing them that you are in the right


### Failure modes


### Forking

Having an inclusive approach when it comes to hard forks might ease a lot of the
pains surrounding them. This could mean that nodes have the capability to track
and interact with multiple forks at once. Or in general try not to frame it as
an us vs. them issue but as a collaborative »we have to solve this together.«

Using votes to decide on forks could be seen as detrimental to this goal, since
a vote has loser by design—if you are not voting for me, you're voting against
me.


### Exit costs

One of our goal is to make exit costs low, i.e. allow users to easily abandon
undesirable forks. But it can be argued that if people have very low exit costs
for a given system, then their incentive to vote according to their true beliefs,
which should be the main goal for any sort of vote, is lowered and in turn would
then render the vote pointless.

And while the exit costs for a single voter can be quite low, the costs a fork
imposes on a community can still end up very high, especially when it results in
two persistent chains. Both forks will have a vested interest in keeping the
»original« name, code will have to be adjusted, wallets to be updated, nodes
changed and users will definitely end up being confused.


### Constitution

In our context a constitution could provide the most important invariants that
should be upheld both in the technical and human domain, e.g. across protocol
changes the total supply must never exceed n coins or the Aeternity Foundation
shall produce detailed reports of its allocation of funds.

Thus a constitution specifies what is allowed to be decided on. It should be
noted however that these rules on how to change rules are informed by expectations
of what the outcomes should or could be., which could lead to problems if these
rules were to be enforced by computers, if it is even possible to encode all of
them as »smart contracts«.


### Automatic protocol amendments

Automatic protocol amendments are a mechanism where updates to the node software
run by participants are tracked inside the system and in most cases adoption
is also being voted upon.
The most obvious issue with this approach is that for this system to work for
all clients, the changes need to be expressed in a way that can be understood by
everyone, which means that everyone has to either run the same software or there
needs to be a common language. This could be achieved by either encoding all the
relevant consensus rules in a language for a virtual machine every participant
has to run or by using a language for these change that can be transpiled easily.

Now if we assume that we have such a language, then the next step is to verify
that the given piece of code adheres to the constitution and does not violate
any of its invariants. This could either be done via manual, human review or
formal methods, i.e. having both the constitution and the code be formally
verifiable. The problem is, that this is most likely a gross oversimplification
because software engineering is never as simple as just writing a single piece
of code and have it just magically work, especially not

Automatic updates just taken by themselves are not without controversy either.
On one hand, having updates be opt-out instead of opt-in, will probably lead
to the system adopting changes quickly but it has also been argued that opting
out, especially if it is not easy to do, would take away a users option to refuse
consent.


contracts in human law, as long as humans are still the
biggest group/driving force, this should be a human process


### Coordination

Coordination game is easy when rules can be codified easily but it is unclear
how it works with different code changes when nobody oversees the process

- forcing cooperation; if everything is automated would that deteriorate the
  development process?


### Funding



### Atomic swaps

Atomic swaps lower the exit costs for users of chains or forks they do
not want to be a part of by providing a trustless way to exchange coins
across chains.

### Replay Protection

If a fork results in two coexisting persistent chains then an account
which interacts with one of the two chains can end up in a situation
where transactions made on one chain can be replayed on the second chain,
if no replay protection is in place, or they might end up making a
transaction on the wrong chain since it might be unclear which of the
two forks they are interacting with if there exists no obvious way to
distinguish them or no way for clients to specify which of them specificly
they want to use.


## Specification

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).


### Protocol

### AEIP

#### Add proposal

### GeneralizedVoting

Following voting proposal defines basic voting method without specifying how obtained VotesSummery should be used.

#### Definitions:
- Voting = a process of supplying VotesSummery on DecisionMatter after Timeframe based on VoteTxs (balances of Entities that created those). Voting is created with QuestionTx.
- Timeframe = start block, end block pair. All blocks from the block after start block to the end block are considered _in_
- Entity = an Account, Contract or any other possible "being" with balance allowed to vote
- Answer = unique payload in VoteTx.
- VoteTx = a transaction with Answer referencing Voting. VoteTxs are only valid _in_ Timeframe. New VoteTx by Entity overwrites previous one. Addictional fee may be required if Answer is unique (wasn't previously supplied by anyone).
- VotesSummery = map of Answers with assigned weights. Weights are assigned to Answer by summing balances at TimeFrame.end\_block of Entities that choose this Answer in valid VoteTx referencing this Voting. Any Entity that didn't vote is assumed to have chosen a `nil` Answer. (we record the total balance of Entities that didn't participate in Voting in special Answer)
- QuestionTx = a transaction created by an Entity specifying Timeframe and DecisionMatter. It\'s only valid if block of inclussion is not _in_ or after Timeframe.
- DecisionMatter = specification of purpose of voting and extensions used. Can be an not blockchain altering question (a human readable string), or a call to specific Governance process that will alter (or not) blockchain depending on VotesSummery. DecisionMatter can apply additional changes or restrictions to the Voting process.
- VotingID = hash of QuestionTx

#### Process details:
1. (before Timeframe) QuestionTx is created and included in a block. This adds `{VotingID => VotingObject}` to chainstate.
2. (in Timeframe) For every valid VoteTx `{EntityID => Answer}` is added to VotingObject in chainstate.
3. (at Timeframe.end\_block) VotesSummery is calculated and added to VotingObject. Map `EntityID => Answer` is removed from VotingObject.

#### Optional Voting changes:
a. step 3. of GeneralizedVoting.Process can be saved in chainstate at some block after end\_block. This gives nodes more time to calculate the results. This offset should be proportional to Tiemframe length.

### Voting extenstions

#### ActiveEntities

Only entities that created a Tx in last X blocks are included in `nil` Answer. I would recommend X to represent about 3-12 months.

#### VotingPowerDelegation

Entities can delegate their Voting power to others. This can be achieved by creating special Tx for changing VotingDelegation of Entities. This extension can include:
- limited delegation
- delegated voting power is weeker by multiplying it by some factor.
- Entity can vote in voting making the delegation invalid or Delegation may prohibit voting. (to vote entity would have to first cancel the delegation and potentially delegate votes again after Voting ends)
- delegation can be transferable or not

This may be implemented in following ways:
- by requiring inclusion of all the Entities whose Delegations are used in VoteTx - that would make VoteTx fee and size higher.
- by storing in every Entity current Voting power and changing it whenever an Entity with VotingDelegation Votes - this will add overhead to every transaction created by Entity with VotingDelegation and limit possibility of transferring VotingDelegation.

### OffChainAggreement

When the only important value for some protocol is "Has >50% of Entities power voted on one answer?" such a voting can be done completely off-chain. Fee requirements can be removed completely or exchanged for less expensive anti spam methods (like hashcash). Votes in such systems should include expiration time. Depending on the use-case hash of such an agreement can be saved on chain for a kind of proof of oldness or complete voting can be submitted to blockchain. If a complete voting is submitted to blockchain, the fee can be split between all voters or the submitter may pay. (Some Entities may not want to pay a fee and some submitter may be have an incentive for the voting to pass big enought he is willing to pay fees for others votes)

### Protocol Amendment

Protocol Amendment can be split into parts:
- changes to parameters of protocol - such changes do not break the consensus mechanics so they can be done without high quorum requirements and many security measures.
- protocol extension - only possible if:
    - we are able to represent our constitution in a way such that code changes can be automatically verified for compliance with constitution. This might be very hard, because a part of constitution will have to be "AEternity node code can't interfere with other parts of users system."
    - or we are able to modularize code to an extend that allows creating protocol extensions that can't break consensus (are sandboxed from code enforcing constitution). This might be possible in a very limited extend if parts of node code will be expressed in sandboxable language.
- protocol replacement - changes that can break consensus should require >50% quorum and security measures that prevents exploiting this functionality with attacks on offline forks.

#### ProtocolParameterChange

- To change some parameter of protocol first a Voting on that parameter should be opened. Such voting has to use set of extensions defined in protocol and Timeframe has to have length between minimum and maximum defined in protocol.
- Depending on time passed since last change to parameter different quorum will be required.
- Low quorum may impose as to an attack where someone puts a vote on the last block possible to vote on and changes parameter in a way that's unwanted by most Entities. To counter that: changes to parameter are applied only after X blocks of the last change. So change can be reverted before it takes effect by having another voting on the parameter. New Voting quorum has to be at least equal to power of voting it's trying to override.
- For turning on and off futures and changing some other "choices" defined in protocol a normal Voting can be used with limited valid Answer set. Answer with most votes is applied if quorum was met.
- For decisions on a variable that "represents a point on a line" (when answers can be sorted and small change to answer is insignificant) a normal Voting can be used. After voting ends if the quorum was met we take the weighted median (middle value after sorting all values) of all Answers and apply it.

#### ProtocolExtenstion

*TODO*

#### ProtocolReplacement

As it is allowed to change (so also "break") consensus, it should require >50% of total tokens (not only active tokens) voting on one Answer. OffChainAggreement can be used for this. I can think of the following approach:
- Trusting always the longest chain and saving all votes from all ProtocolReplacements on chain. The problem is that an attacker can ignore the block that included ProtocolReplacement data and create over time a longer chain then the longest containing the ProtocolReplacement. This can be countered by remembering in nodes all executed ProtocolReplacements and never reverting them, but this leaves new nodes vournable to such attacks and if such an attack is executed, a software update hardcoding the ProtocolReplacement would have to be used. This attack can be made harder by delaying the ProtocolReplacement execution after inclusion on chain.
- Trusting always the ProtocolReplacement with lowest block height even if it's on a fork + requiring all new ProtocolReplacemens to be on chains with previous executed ProcolReplacement. As a significant portion of AE is going to be created in genesis block this makes it extreamly unlikely for attacker to be able to have enough tokens is some fork to trigger a ProtocolReplacement. Over time when we introduce ProtocolReplacements we will limit possible attack surface as then an attacker would have to get >50% of tokens on a block with lower block height then the ProtocolReplacment or on a block in chain with the ProtocolReplacement.

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


## Storage



## (possible) Future(s)


### Atomic Swaps

In the case that both chains support Schnorr signatures, an atomic swap
could be condensed to a simple spend transaction with [adaptor signatures](https://scalingbitcoin.org/stanford2017/Day2/Using-the-Chain-for-what-Chains-are-Good-For.pdf).

### Reputation

Sabater, Jordi, and Carles Sierra. "Regret: A reputation model for gregarious societies." Fourth workshop on deception fraud and trust in agent societies. Vol. 70. 2001.

### Quadratic Voting

### Curation lists/markets


## References/reading

[1] https://scalingbitcoin.org/stanford2017/Day2/Changes-without-unanimous-consent.pdf

[2] Cheryl Boudreau, ‘Making Citizens Smart: When Do Institutions Improve Unsophisticated Citizens’ Decisions?’, Political Behaviour 31 (2009), pp. 287-306

[3] Blum, Christian, and Christina Isabel Zuber. "Liquid Democracy: Potentials, Problems, and Perspectives." Journal of Political Philosophy 24.1 (2015).

[4] Levy, Karen EC. "Book-Smart, Not Street-Smart: Blockchain-Based Smart Contracts and The Social Workings of Law." Engaging Science, Technology, and Society 3 (2017): 1-15.

[5] Olson, Mancur. The logic of collective action. Vol. 124. Harvard University Press, 2009.


