[View code on GitHub](https://github.com/ergoplatform/ergo/papers/whitepaper/currency.tex)

The code presented in this file explains the importance of Ergo's native token, \Erg{}, and its role in ensuring the stability and security of the Ergo platform. The \Erg{} token is divisible into up to $10^9$ smallest units, \nanoErg{}s, and is used to incentivize miners to participate in the Ergo network, securing it from hashrate-based attacks like the known 51\% attack. 

The emission of \Erg{} tokens will be finished within eight years, after which miners will only receive \Erg{}s from fees. The fees will help miners to sort transactions, preventing spam attacks while allowing miners to include transactions from honest users in blocks. Ergo has a storage rent component that periodically charges users \Erg{} for every byte included in the state. This storage rent is making the system more stable by limiting state size or insuring proper compensation for larger state size, returning lost coins into circulation and providing an additional stable and predictable reward to miners.

All \Erg{} tokens that will ever circulate in the system are presented in the initial state, which consists of three boxes: No Premine Proof, Treasury, and Miners Reward. The No Premine Proof box contains exactly one \Erg{} and is protected by a script that prevents it from being spent by anyone. The Treasury box contains 4,330,791.5 \Erg{}s that will be used to fund Ergo development. The Miners Reward box contains 93,409,132 \Erg{}s that will be collected by block miners as a reward for their work. 

The code also explains the emission of \Erg{} tokens, which will be released according to a predefined and hard-coded token emission schedule. During blocks 1-525,599 (2 years), 7.5 \Erg{}s will be released every block. During blocks 525,600-590,399 (3 months), 4.5 \Erg{}s will be released every block. Finally, during blocks 590,400-655,199 (3 months), 1.5 \Erg{}s will be released every block. The number of \Erg{}s in circulation with time is shown in the emission curve.

In conclusion, the \Erg{} token is an essential component of the Ergo platform, ensuring its stability and security. The token is used to incentivize miners to participate in the network, sort transactions, and limit state size. The emission of \Erg{} tokens is released according to a predefined schedule, and all tokens that will ever circulate in the system are presented in the initial state.
## Questions: 
 1. What is the purpose of the No Premine Proof box and how does it prevent private mining before the launch date?
    
    The No Premine Proof box contains one Erg and is protected by a script that prevents it from being spent by anyone. Its purpose is to prove that Ergo mining was not started privately by anyone before the declared launch date. The box contains additional registers with the latest headlines from the media and the latest block identifiers from Bitcoin and Ethereum, which ensure that Ergo mining could not have started before certain events in the real world and the cryptocurrency space.

2. How does Ergo limit state size and ensure proper compensation for larger state size?
    
    Ergo has a storage rent component that periodically charges users Erg for every byte included in the state. This storage rent is making the system more stable by limiting state size or insuring proper compensation for larger state size, returning lost coins into circulation and providing an additional stable and predictable reward to miners.

3. How will the Treasury box funds be used and distributed in a decentralized manner?
    
    During the first year, the Treasury funds will be used to cover the pre-issued EFYT token. After that, they will be distributed in a decentralized manner via a community voting system that is under development. The Treasury box contains 4,330,791.5 Ergs that will be used to fund Ergo development, and its protecting script ensures that only a predefined portion of the box value is unlocked at any given time.