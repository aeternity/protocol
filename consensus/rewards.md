# Miners' rewards

Aeternity is Proof of Work blockchain. This is a description of rewards paid to miners.

## Introduction

Miners mine key blocks and receive rewards composed out of two ingredients:
1. Coinbase-like reward for mining a key block
2. Fees and gas paid by users for transactions and contract calls

There is also special case altering rewarding scheme. It crypto economic incentive designed to lower risk of fraud - and it is called Proof of Fraud.

Miners rewards are also affected by protocol protected mechanism of reward split.

### Reward for mining a key block

Miners include beneficiary address in a key block. The reward is sent to it with protocol protected delay.
The size of the reward is computed based on inflation curve

### Fees and gas

Users need to pay for execution of their actions. According to Bitcoin-NG protocol a miner gets 60% of previous generation fees and 40% of the next one.

### Proof of Fraud

If a miner decides to cheat and double spend by creating a fork within generation of his leadership PoF is a mechanism to detect it and punish. Such a fork will be resolved by usual Proof of Work fork algorithm and no funds are double spent. Furthermore, the next leader is able to signal malicious activity by including two microblock headers with the same parent and the same leader. The consequences are following:
1. Malicious leader is not rewarded with mining reward
2. The signaling miner receives 5% of according reward

### Reward split

Reward split is way to dedicate portion of miners rewards to protocol protected address (or addresses). The exact ratio of reward split is established via blockchain governance procedure. The amount send to protocol protected address includes fees. It is also subject to
1. Protocol reward delay -- so it is going along original coinbase reward
2. Proof of Fraud signaling 

