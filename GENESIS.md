# Genesis

The genesis block of the Aeternity blockchain will contain the initial
distribution of coins.

## ERC20 token

After collecting funds in early 2017, Aeternity issued an ERC20 token `AE` on
the Ethereum blockchain. Such a token is, at the most fundamental level, just a
mapping from a set of Ethereum addresses to their respective balances and a
standardised interface to interact with the token. It is setup in such a way
that modifying the balance for a given address requires a valid signature of a
public key for that address.

The `AE` tokens function as IOUs for the the initial distribution of coins for
the Aeternity blockchain and they will be usable until `Mon Sep 02 19:56:09 2019 UTC`
after which the smart contract should refuse any token transfers.

Given that the ERC20 token is transferable until late 2019, we are going to

1. have to take a snapshot at a target block
2. or have users burn their tokens, e.g. via sending them to the token contract
   itself,

in order to be able to come up with an initial distribution, since we do not
want to wait until the tokens are no longer transferable.

(***TODO***: find out how many smart contracts are managing AE tokens currently
and how many of the initial distribution never moved)

## Snapshot

A snapshot is simply taking the state of the contract at some height and put the
`(address, balance)` pairs into the genesis block.
This is arguably the simplest solution but it comes with a couple of downsides.

First of all, it forces us to use the same address scheme as Ethereum, i.e. an
address is `KECCAK256(ECDSAPUBKEY(priv_key))[96:255]` or the rightmost 160 bits
of the the public keys' Keccak-256 hash. But the current plan is to use EdDSA/
Ed25519 for signatures and use Blake2b instead of Keccak-256.
(***TODO***: Alternative would be to support multiple signature schemes? How
much would that increase verification effort/complexity? Or )

Secondly, since tokens can be, and actually are, managed by smart contracts, we
would have to replicate all these contracts, including state and dependencies,
because private keys for smart contracts are unknown and thus preventing anyone
from accessing the funds at a given address unless the contract is replicated.

And much worse, it promotes private key re-use, which is akin to re-using
passwords, just worse, especially given the context and the fact that now the
security of users private keys rely on even more parties. This something users
should be weary of since it jeopardises their funds on all chains involved.


## Token burning

A more involved solution would be to have users actively burn their tokens and
supply the address that they want to use on the Aeternity chain.

The disadvantage of this approach is that it requires active involvement of the
users. That is, while the process can be automated easily, it still requires
users to initiate the process and issue a transaction on the Ethereum chain.

Since not all users would finish this process in time, as witnessed numerous
times for other projects, where people stop paying attention to projects for
months at a time, a pair of smart contracts could be set up on the Ethereum and
Aeternity chain, which could be used to hand out unclaimed coins.
(***TODO:*** Give detailed explanation for this)

The Aeternity token on the Ethereum chain is a [HumanStandardToken](https://github.com/ConsenSys/Token-Factory/blob/master/contracts/HumanStandardToken.sol)
that comes with an `approveAndCall` method, which allows us to burn the tokens
and register the public key for the Aeternity chain in just one call.

Solidity contract on Ethereum chain:

```
pragma solidity ^0.4.21;

// Fallback ERC20 token definition.
contract tokenFallback {
    uint256 public totalSupply;

    function balanceOf(address _owner) public constant returns (uint256 balance);
    function transfer(address _to, uint256 _value) public returns (bool success);
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success);
    function approve(address _spender, uint256 _value) public returns (bool success);
    function allowance(address _owner, address _spender) public constant returns (uint256 remaining);

    event Transfer(address indexed _from, address indexed _to, uint256 _value);
    event Approval(address indexed _owner, address indexed _spender, uint256 _value);
}

// TODO: Run this in the EVM to make sure that this actually does what we want
//       it to do.
contract TokenBurner {
    struct Claim {
        uint256 amount;
        bytes32 pubkey;
    }
    // TODO: Do we actually care who burned the tokens or should we just
    //       record pubkey => balance mappings?
    mapping(address => Claim) burned;

    function receiveApproval(
      address _from,
      uint256 _value,
      address _token,
      bytes _extraData
    ) public returns (bool) {
        // Only let people burn AET.
        require(msg.sender == 0x5CA9a71B1d01849C0a95490Cc00559717fCF0D1d);
        // We only care about the first 32 bytes, which should hold our new pub key.
        require(_extraData.length >= 32);
        bytes32 _pubkey = 0x0;
        assembly {
            _pubkey := mload(add(_extraData, 0x20))
        }
        require(tokenFallback(_token).transferFrom(_from, this, _value));
        burned[_from].pubkey += _pubkey;
        burned[_from].amount += _value;
        emit Burn(_from, _pubkey, _value);
        return true;
    }

    event Burn(address _from, bytes32 _pubkey, uint256 _value);
}
```

On the Aeternity chain, we need a contract, that either holds or funds, or can
mint new coins, (***TODO***: This is where native tokens/assets come into play?)
and a proof that the tokens were burned on the Ethereum chain. A proof of burn
could be a proof that the above contract's state contains a claim entry.


## Incentives

It is important to note, that users will need to withdraw their tokens from
(centralised) exchanges in either case if they do not want to have to rely on
these exchanges to start supporting the Aeternity blockchain and distribute
their coins accordingly.

Assuming that the overwhelming majority of current users see their tokens
exclusively as investment vehicles could introduce another problem. If exchanges
fail to support the native Aeternity blockchain coin or, for whatever reason,
the native coin is traded at much lower value than the ERC20 token, then the
incentive for the exchange of ERC20 tokens for native coins is weak.

To give people more of an incentive, we might consider an interactive auction.
The burn and snapshot approaches can be seen as auctions, where one unit of the
ERC20 token buys exactly one share of the native coin. So if we want people to
abandon the old ERC20 token as quickly as possible, we might use a Reverse Dutch
Auction, where the price per share never drops below one. That is, the
multiplier starts off at e.g. 1.1 and decreases with time.
(***TODO***: Dilution etc.)

