Bitcoin-NG for Aeternity
==========

Bitcoin-NG is a new consensus algorithm [1]. It depends on Proof-of-Work and uses chain of blocks with the most work done to resolve conflicts. Aeternity is PoW blockchain. Using Bitcoin-NG is very suitable for reducing on-chain confirmation latency. Bitcoin-NG is based on temporary leader that is elected randomly using Proof-of-Work.


How to understand Bitcoin-NG?
===

To understand NG really quickly, we need to re-cap how we can think about classic Nakamoto consensus.

Nakamoto consensus is based on crypto-puzzle that chooses a leader (miner) who confirms all the events included in the past block. New events are aggregated by all miners until one of them confirms them.

Bitcoin-NG consensus is based on crypto-puzzle that chooses a leader (miner) who confirms all the events that will happen until the next miner solves the crypto-puzzle. The next miner takes over leadership.


Low level view of Bitcoin-NG
===
Leaders are elected by solving Proof-of-Work puzzle. They broadcast the evidence that they solve the puzzle in Key Blocks (KB). The new Key Blocks holds PubKey representing the leader. From now on, the miner becomes a leader and gains right to broadcast signed blocks holding transactions. We call them Micro Blocks (MB). There is no Proof-of-work involved in emission of Micro Blocks.

      ┌────────┐                        ┌────────┐
      │   1    │   ┌─────┐   ┌─────┐    │   2    │  ┌─────┐
      │  KB-1  │───│MB(1)│───│MB(1)│────│  KB-2  ├──│MB(2)│
      │        │   └─────┘   └─────┘    │        │  └─────┘
      └────────┘                        └────────┘


      KB1: Key Block with Pub Key 1 belonging to Leader 1
      MB(1): Micro Block signed by Leader 1 with Priv Key 1
      1: Height of the chain at Key Block 1

      Description:
      Leader 1 broadcasted two Micro Blocks. Leader 2 send out new Key Block holding his key.
      Leader 2 emitted one Micro Block so far


Leaders, who follow the protocol, emit Micro Blocks until they receive Key Block broadcasted by another leader. Micro Blocks are not distinguished by height - they inherit the height of the leader that emitted them.

Latency
==

On average in Bitcoin blocks are broadcasted every 10 minutes - it is driven by protocol and guarded by target. Aeternity assumed 3 minutes for Key Blocks and 3 seconds time delta between Micro Blocks. 3 minutes resolution of Key Blocks is also guarded by target and Proof-of-Work.

Rewards
==
There is major challenge in providing liveness and integrity of the chain in the scheme proposed by Bitcoin-NG. It is solved by crypto-economic incentives. To guarantee that the next leader follows as much as possible of Micro Blocks the next leader receives fixed award on the top of 60% of fees from the previous generation of Micro Blocks. The previous leader receives 40% of the fees included in transactions he confirmed.

     ┌────────┐                        ┌────────┐
     │        │   ┌─────┐   ┌─────┐    │        │  ┌─────┐
     │Leader 1│───│FeeN1│───│FeeN2│────│Leader 2├──│FeeN3│
     │        │   └─────┘   └─────┘    │        │  └─────┘
     └────────┘                        └────────┘
      Leader 2 Award: Governance(Coinbase) + 0.6*(FeeN1+FeeN2) + 0.4*FeeN3


Forks
==

Bitcoin-NG inherits Bitcoin's ability to fork in case of multiple block producers at the same height. It happens on Key Block level. Bitcoin-NG resolves the conflict using the same method as Bitcoin - that is - the longest chain survives. Micro Blocks carry no weight. It is still possible to have forks at Micro Block level.
1. Network propagation time. There is a delay between mining new Key Block and receiving it by the old leader. In that time the old leader still broadcasts micro blocks. They are not valued any more, though. New leader will re-sign them and re-broadcast. We expect such Micro forks at every Leader switch.

2. Malicious leader. It is possible that malicious actor will emit conflicting Micro Blocks. The result will be incorrect chain. To fix that we will emit Proof-of-Fraud.


                         ┌──────┐
                ┌────────│MB(1)'│
                │        └──────┘
                │
                │
                │       ┌────────┐
             ┌─────┐    │        │  ┌─────┐
          ───│MB(1)│────│  KB-2  ├──│MB(2)│
             └─────┘    │        │  └─────┘
                        └────────┘

        Micro Block broadcasted by old leader is no longer forming consensus.
        New leader may read it and include all transaction in newly broadcasted
        micro blocks. Most likely, the new leader will broadcast micro blocks
        as soon as possible. Given that nodes in the network have very similar
        mempool content MB(1)' and MB(2) should be very similar. Re-signing
        the delta of transactions missing in Leader 2's node is very cheap operation.



References:

1. Bitcoin-NG: A Scalable Blockchain Protocol, Ittay Eyal, Adem Efe Gencer, Emin Gün Sirer, and Robbert van Renesse,Cornell University, 2016
