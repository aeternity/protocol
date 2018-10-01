# Genesis

The genesis block of the Aeternity blockchain will contain the initial
distribution of coins and this document describes the different possible
processes available to us for the conversion of `AE` tokens to native coins.


## Aeternity token

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

Whenever the point comes at which the ERC20 tokens are no longer transferable,
there will most likely still be token owners, which have failed to burn their
tokens, in order to claim them on the Aeternity chain.
Since tokens will not be transferable anymore, a simple signature will suffice
to claim coins on the Aeternity chain.

It is important that no smart contracts are left with tokens, since they cannot
sign messages and thus wouldn't be able to claim coins using this method.
The last resort then would be to setup another smart contract on the Ethereum
chain with all the left-overs and have users send a small amount of Ether to
that contract, or execute a contract call if the smart contract has the ability
to do so, in order to show that they do control the tokens in question.


## Snapshot

A snapshot is simply taking the state of the contract at some height and put the
`(address, balance)` pairs into the genesis block.
This is arguably the simplest solution but it comes with a couple of downsides.

First of all, it forces us to use the same address scheme as Ethereum, i.e. an
address is `KECCAK256(ECDSAPUBKEY(priv_key))[96:255]` or the rightmost 160 bits
of the the public keys' Keccak-256 hash, which goes against our current usage of
EdDSA/Ed25519 for signatures and Blake2b instead of Keccak-256.

Secondly, since tokens can be, and actually are, managed by smart contracts, we
would have to replicate all these contracts, including state and dependencies,
because private keys for smart contracts are unknown and thus preventing anyone
from accessing the funds at a given address unless the contract is replicated.

It also promotes private key re-use, which is akin to re-using passwords, just
worse, especially given the context and the fact that now the security of users
private keys rely on even more parties. This something users should be weary of
since it jeopardises their funds on all chains involved.


## Token burning

A more involved solution would be to have users actively burn their tokens and
supply the address that they want to use on the Aeternity chain.

The disadvantage of this approach is that it requires active involvement of the
users. That is, while the process can be automated easily, it still requires
users to initiate the process and issue a transaction on the Ethereum chain and
therefore also requires them to have Ether.

The Aeternity token on the Ethereum chain is a [HumanStandardToken](https://github.com/ConsenSys/Token-Factory/blob/master/contracts/HumanStandardToken.sol)
that comes with an `approveAndCall` method, which allows us to burn the tokens
and register the public key for the Aeternity chain in just one call.

The solidity code for a contract used for burning coins on the Ethereum chain
might look like this:

```pragma solidity ^0.4.25;

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
        uint256[] amount;
        bytes32[] pubkey; // if people burn tokens multiple times, we can either 
                          //1. store every AE-pubkey or 
                          //2. store only those which havn't been stored before, which would require a seperate mapping + array to iterate over, so I suggest we go with option 1.
    }
    
    
    // Store the hashes of Aadmins' msg.data used for counting up the AE delivery batch
    mapping (address => bytes32) private multiSigHashes;
    // Keep track of token burn batches - use this number for filtering in the emitted Burn event.
    uint16 public AEdeliveryBatchCounter = 0;
    
    // The admins which may count up the AE delivery batch count
    address public AEdmin1;
    address public AEdmin2;
    // multi sig for counting up the token delivery batch counter
    modifier onlyAEdmins() {
        // check if transaction sender is AEdmin.
        require (msg.sender == AEdmin1 || msg.sender == AEdmin2, "Not an AEdmin.");
        // if yes, store his msg.data. 
        multiSigHashes[msg.sender] = keccak256(msg.data);
        // check if his stored msg.data hash equals to the one of the other aedmin
        if ((multiSigHashes[AEdmin1]) == (multiSigHashes[AEdmin2])) {
            // if yes, both aedmins agreed - continue.
            _;

            // Reset hashes after successful execution
            multiSigHashes[AEdmin1] = 0x0;
            multiSigHashes[AEdmin2] = 0x0;
        } else {
            // if not (yet), return.
            return;
        }
    }
    
    // TODO: Do we actually care who burned the tokens or should we just
    //       record pubkey => balance mappings?
    mapping(address => Claim) burned;
    uint256 public burnCount; // count the amount of burns for later filtering of all burnings
    
    constructor(address _AEdmin1, address _AEdmin2){
        require (_AEdmin1 != 0x0);
        require (_AEdmin2 != 0x0);
        require (_AEdmin1 != AEdmin2);
        AEdmin1 = _AEdmin1;
        AEdmin2 = _AEdmin2;
    }
    
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
        burned[_from].pubkey.push(_pubkey); // pushing pubkey and value, to allow 1 user burn n times to m pubkeys
        burned[_from].amount.push(_value);
        emit Burn(_from, _pubkey, _value, burnCount++, AEdeliveryBatchCounter);
        return true;
    }
    
    function countUpDeliveryBatch()
    public onlyAEdmins
    {
        ++AEdeliveryBatchCounter;
    }
    
    // proposing to index two events: _from for easier user support, and 
    // _deliveryPeriod for easy retrieval of all users to include in the next 
    // AE delivery period
    event Burn(address indexed _from, bytes32 _pubkey, uint256 _value, uint256 _count, uint16 indexed _deliveryPeriod);
}
```

On the Aeternity chain, we need a contract, or a protocol level mechanism, that
holds all funds that need to be dispersed and can verify that tokens were
actually burned, e.g. by supplying the path in the state tree to the entry plus
a valid Ethereum block header, and then after `Mon Sep 02 19:56:09 2019 UTC`
allow signatures to be used.

Since not all users would finish this process in time—as witnessed numerous
times for other projects, where people stop paying attention to projects for
months at a time—a pair of smart contracts could be set up on the Ethereum and
Aeternity chain, which could be used to hand out unclaimed coins.


## Third party/centralised solutions

The above approach requires users to spend Ether, in order to burn their tokens.
Given the assumption that the majority of users are currently using their tokens
solely for speculation, we cannot assume them to actually know what exactly a
token is or even how to use them outside of exchanges.
The upshot of the last assumption is, that the exchanges have all the expertise
needed. That is, exchanges can handle the conversion from ERC20 token to native
coin without users actually having to anything.
We might even encourage users, who would otherwise not be able to convert their
tokens, to deposit them on an exchange.

Currently, the AE token is traded on [17 centralised exchanges](https://coinmarketcap.com/currencies/aeternity/#markets) and some more decentralised exchanges. The
decentralised exchanges operate via smart contracts on the Ethereum chain and
will therefore not be able to list the native coin.

With the majority of users having their tokens on exchanges, offloading the
token to coin conversion to these third parties would be the solution with the
best user experience, since there would be no need for the users to do anything.
With this approach scammers trying to get users to send them their tokens
would also have a hard time.

Another approach—that would require users to put trust into a service setup by
us—is to have a simple webservice, where users can post the public key they
intend to use on the Aeternity chain and then receive an unique burn address on
the Ethereum network. For each `AE` token sent to one of the burner addresses,
we would then release the appropriate amount of native coins. This would be very
easy to set up but has the major downside that it would most likely attract a
lot of scammers.


## Incentives

We assume that the overwhelming majority of current users see their tokens
exclusively as investment vehicles. If exchanges fail to support the native
Aeternity coin or, for whatever reason, the native coin is traded at much lower
value than the ERC20 token, then the incentive for the exchange of ERC20 tokens
for native coins is weak.

To have more of an incentive, we might consider an interactive auction. The burn
and snapshot approaches can be seen as auctions, where one unit of the ERC20
token buys exactly one share of the native coin. So if we want people to abandon
the old ERC20 token as quickly as possible, we might use a Reverse/Dutch
Auction, where the price per share never drops below one. That is, the
multiplier starts off at e.g. 1.1 and decreases with time.
In the ideal case, where all users act immediately, this would not result in any
dilution, since the total initial supply would just be multiplied by 1.1.
But given that many people fail to keep up with projects, those that do fail
to exchange their tokens in the first period, will end up with less coins
relative to earlier participants.

