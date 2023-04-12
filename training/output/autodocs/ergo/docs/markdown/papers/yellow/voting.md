[View code on GitHub](https://github.com/ergoplatform/ergo/papers/yellow/voting.tex)

The code describes the voting system used in the Ergo blockchain to allow miners to change various parameters on-the-fly. These parameters include instruction costs, computational cost limits, block size limits, storage fee factors, and block versions. There are two types of changes: foundational changes and everyday changes. Foundational changes require more than 90% of miners to vote for the change and last for 32 epochs. Everyday changes require a simple majority. 

Miners can vote for two everyday changes and one foundational change per block. To vote "Yes," a miner includes the identifier of the change in the block header. To vote "No," a miner writes a zero value instead of the corresponding byte. 

The code includes a table of parameters that can be changed, their default values, possible steps, and minimum and maximum values. Miners can propose changes by posting an identifier of a vote for a change in the first block of a voting epoch. There are three slots in a block header for changes to propose, with two slots reserved for everyday changes and the third one for proposing a softfork. 

Soft-forks happen when a protocol version supported by the network is increased. The protocol version is written into every block header, with the initial value set to 1 during launch. Soft-forks require a proposal to increase the protocol version and put deactivated rules into the extension. Other miners vote within 32 epochs for the proposal. If the proposal is rejected, a new voting may be proposed next epoch after the voting is done. If the proposal is approved, an activation period of 32 epochs starts. Soft-fork data is still written to corresponding extension sections during the activation period, and on activation height. Block version written into extensions is increased from the first block of the activation period, while protocol version in headers is still the same. Protocol version in headers is increased from the activation height.

Overall, this code allows for a flexible and democratic system of parameter changes in the Ergo blockchain. Miners can propose and vote on changes, with different requirements for foundational and everyday changes. Soft-forks can also be proposed and voted on, with an activation period of 32 epochs.
## Questions: 
 1. What types of changes can be made via miners voting?
- Miners can vote for changes such as instruction costs, computational cost limit per block, block size limit, storage fee factor, block version, and more.

2. How are votes for proposals and changes handled?
- A miner can vote for two everyday changes and one foundational change per block, and to vote "Yes" or propose a change, the miner includes the identifier of the change in the block header. To vote "No" or abstain from voting, the miner writes a zero value instead of the corresponding byte.

3. How does the soft-fork voting process work?
- A soft-fork happens when a protocol version supported by the network is increased, and it requires more than 90% of miners to vote for the change. The first block after the activation period should carry soft-fork voting parameters, and a new voting may be started in the next epoch after the activation period.