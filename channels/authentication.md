# Authentication

Transactions represent intention and thus require explicit consent. This is
true both for on-chain transactions and for off-chain ones. A notable
difference between the two is that while on-chain transactions' consent MUST
be valid at the height at which the transaction had been included, this is
not the case with the off-chain one. Any off-chain transaction can be used in
an on-chain dispute, providing on-chain mutual agreement that a certain
`state_hash` had been valid at a certain `round`. This implies that consent of
off-chain state MUST be validatable in the future. This document explains the
different implications this has on channels.

We express consent in a provable and a cryptographically safe manner. From now
on we will call it authentication. In the context of channels we can have
both unilateral and mutual authentication, depending if just one or the two
parties had expressed their consent. Assumption is if both parties agreeed
upon a transaction, it had been valid at least at some point of time.

### Basic and generalized methods

Currently there are two different authentication methods:

* `basic` - a private key corresponding to the public key is being used for
  producing signatures upon the transaction binary. The account has a nonce
  and it is being bumped accordingly when the channel participant is the
  origin of the on-chain transaction. For off-chain ones nonce is not a part
  of the transaction itself and thus is neither checked nor bumped. This makes
  them validatable in the future as well.
* `generalized` - a smart contract is being attached to the account and is
  being used instead of private key. This smart contract has a state and it is
  updated by on-chain transactions. It is not updated by off-chain ones but
  since the authentication method MUST be valid in the future, a static
  version of the authentication method is used. More detailed explaination for
  Generalized Accounts can be found [here](../generalized_accounts/generalized_accounts.md).

Since a participant can upgrade their account from a `basic` to `generalized`
one any time, we have three options relating to channel's opening transaction.
In all cases, latest on-chain authentication is being used in the on-chain
transactions and for the off-chain ones - the one being present at channel's
creation time.


#### Participant is a `basic` account

If a participant is a `basic` account, the authentication method being used
is as described above. Both on-chain and off-chain transactions are signed
using the private key.

#### Participant upgrades their account after channel creation

If a participant upgades their account after the `channel_create_tx` is being
included, one MUST use the new authentication method for all on-chain
transactions. Off-chain on the other hand are signed as if the account is
being `basic`, as it was at channel creation time.

#### Participant is a `generalized` account at channel creation time

If a channel participant is a `generalized` account at a channel creation
time, both on-chain and off-chain transactions are being validated according
to this authentication method. There is still a difference, though: as
authentication methods are expected to implement a replay attack protection,
they are stateful. This is not the case with off-chain transaction
authentication - they use whatever the state of the generalized account
contract state was at channel creation time in a static manner.

A participant's authentication method for the channel can not be changed.

### Sequential and parallel authentication

Authentication methods can be added in different order but they are validated
in the order provided to the miner. Depending on the significance of the order
in which authentications are to be checked, we have two different types:

* `sequential` - when authentications must be checked in the provided order or
  they might fail validation.
* `parallel` - when order is irrelevant to the validation process and checks
  can be performed in a concurrent manner.

For `basic` authentication always `sequential` behavior is used.
For `generalized` authentication methods, different approaches are used
depending on whether the transaction is meant to be processed on-chain or not:

* for on-chain transactions (`channel_create`, `channel_deposit` and etc.) the
  `sequential` behavior is used and each layer of meta transactions
  authenticates the topmost transaction it wraps. This is the standart
  behaviour used for all on-chain transactions.
* for off-chain transactions (namely `channel_offchain`) the `parallel`
  behaviour is used and all meta transactions authenticate the innermost
  transaction.


