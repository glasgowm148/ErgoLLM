[View code on GitHub](https://github.com/ergoplatform/ergo/papers/yellow/block.tex)

The code presented here provides documentation for the Ergo blockchain system, specifically the Ergo Modifiers. The Ergo block is divided into four parts: Header, BlockTransactions, ADProofs, and Extension. The Header contains the minimum amount of data required to synchronize the chain and check PoW correctness, as well as hashes of other sections. It also includes the block version, the ID of the parent block, the hash of ADProofs for transactions in a block, the root hash of a state after block application, the root hash of transactions in a block, the block timestamp, the current difficulty in a compressed form, the block height, the root hash of the extension section, the solution of Autolykos PoW puzzle, and votes for changes in system parameters.

The Extension section is a key-value storage for a variety of data. A key is always 2-bytes long, and the maximum size of a value is 64 bytes. The Extension section could be no more than 16,384 bytes. Some keys have predefined semantics. For example, if the first byte of a key equals to 0x00, then the second byte defines the parameter identifier, and the value defines the value of the parameter. Another predefined key is used for storing interlinks vector, where the first byte of the key is 0x01, the second one corresponds to the index of the link in the vector, and the value contains the actual link (32 bytes) prefixed with the number of times it appears in the vector (1 byte). Other prefixes may be used freely.

The purpose of this code is to provide a clear understanding of the structure and content of the Ergo block, specifically the Header and Extension sections. This information is essential for developers who want to build applications on top of the Ergo blockchain system. By understanding the structure and content of the Ergo block, developers can create more efficient and effective applications that take advantage of the unique features of the Ergo blockchain system. For example, developers can use the Extension section to store custom data that is specific to their application, allowing them to create more complex and sophisticated applications that are tailored to the needs of their users.
## Questions: 
 1. What are the different parts of an Ergo block and what do they contain?
- The Ergo block consists of four parts: Header, BlockTransactions, ADProofs, and Extension. The Header contains minimal data required to synchronize the chain and check PoW correctness, as well as hashes of other sections. BlockTransactions is a sequence of transactions included in the block, while ADProofs are proofs for transactions included in the corresponding BlockTransactions section of a block. Extension contains additional data that does not correspond to previous sections, including interlinks and current parameters of the chain.

2. What fields are included in the Header section of an Ergo block?
- The Header section of an Ergo block includes the following fields: version, parentId, ADProofsRoot, stateRoot, transactionsRoot, timestamp, nBits, height, extensionRoot, powSolution, and votes. Some of these fields may be calculated by the node itself if it is in a certain mode.

3. What is the Extension section of an Ergo block and what kind of data does it store?
- The Extension section of an Ergo block is a key-value storage for a variety of data. A key is always 2-bytes long, and the maximum size of a value is 64 bytes. The Extension section could be no more than of $16,384$ bytes. Some keys have predefined semantics, such as storing system parameter values or interlinks vector. Other prefixes may be used freely.