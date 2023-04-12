[View code on GitHub](https://github.com/ergoplatform/ergo/papers/whitepaper/utxo.tex)

The code in this file explains the design of the Ergo state, which is used to check new transactions in the Ergo cryptocurrency. The Ergo state is represented using one-time coins, called boxes, which are similar to Bitcoin's UTXOs but contain user-defined data in addition to monetary value and protecting script. The state snapshot is fixed within the protocol and is represented by boxes not destroyed by previous transactions. 

Each Ergo box has ten registers, of which the first four are mandatory and the rest may contain arbitrary data or be empty. The first register contains the monetary value of the box, the second contains the serialized script protecting the box, the third contains an array of token identifiers and amounts locked in the box, and the fourth contains information about the transaction that created the box. The remaining registers can contain arbitrary user-defined data.

The use of one-time immutable objects in the Ergo state provides several advantages over Ethereum's long-lived mutable accounts, including easier and safer protection from replay or reordering attacks, easier parallel processing of transactions, and the absence of side-effects resulting from `out-of-gas' exceptions or reentrancy issues. 

The Ergo protocol fixes the ledger snapshot representation in the form of boxes not destroyed by previous transactions. A miner maintains an AVL+ tree-like authenticated data structure built on top of the UTXO set, and includes a short digest of this structure in each block header. This digest is calculated after applying the block, and is used to verify that all spent boxes were removed from the state, all created boxes were added to it, and no more changes were made. 

AVL+ trees allow building efficient authenticated dictionaries that reduce the proof size and speed up verification, making them better suited for cryptocurrency applications than prior solutions such as Merkle Patricia tries. Proofs for multiple transactions in a single block are compressed together, reducing their total length by approximately an additional factor of 2. 

Overall, the Ergo state provides an efficient and secure way to prove the existence or non-existence of certain elements in it, as well as proofs of tree modifications. These tree operations are supported by the Ergo smart contract language, providing the ability to implement sophisticated contracts.
## Questions: 
 1. What is the difference between Ergo's one-time coins and Bitcoin's UTXO model?
- Ergo follows Bitcoin's UTXO design and represents the snapshots using one-time coins. The difference from Bitcoin is that in addition to monetary value and protecting script, an Ergo one-time coin, called a {\em box}, also contains user-defined data.

2. How does Ergo fix the ledger snapshot representation?
- The Ergo protocol fixes the ledger snapshot representation in the form of boxes not destroyed by previous transactions. In detail, a miner should maintain a Merkle-tree like authenticated data structure built on top of the UTXO set and must include a short digest (just 33 bytes) of this structure in each block header.

3. What are the advantages of using one-time immutable objects?
- One-time immutable objects (as in Bitcoin's UTXO model) have some advantages over Ethereum's long-lived mutable accounts. Firstly, it gives easier and safer protection from replay or reordering attacks. Secondly, it is easier to process transactions in parallel because they don't modify state of the objects they access. Finally, it seems easier to build fully stateless clients using one-time coins.