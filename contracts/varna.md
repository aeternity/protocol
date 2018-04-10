[back](./contracts.md)
# The Varna Language

The high level language "Varna" (Sanskrit for type) is somewhat
similar to Bitcoins Script language.  Varna contracts do not contain
any loops and the gas cost for a call is bounded at compile
time. Thanks to Æternity's many first order objects the languages is
still very powerful.

Example:

```
 buy_tokens(value: aeons) =
     amount = (value div oracle("GameTokenPrice", "price"))
     if owner.tokens."GameTokens" > amount
        caller.tokens."GameTokens" += amount
        owner.tokens."GameTokens" -= amount
        owner.balance += value

```

The High Level Machine (HLM) is a very simple virtual machine.  The
Varna contract is evaluated directly by the node verification code.

TODO: Describe the Varna syntax & semantics

# The Varna_01 ABI
TODO: Describe the Varna ABI
