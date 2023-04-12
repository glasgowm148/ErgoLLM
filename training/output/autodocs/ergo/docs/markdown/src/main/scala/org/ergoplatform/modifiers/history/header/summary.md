[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/scala/org/ergoplatform/modifiers/history/header)

The code in this folder is responsible for handling the block headers in the Ergo blockchain. Block headers contain important metadata about a block, such as its parent, timestamp, and transactions. The folder contains four files: `Header.scala`, `HeaderSerializer.scala`, `HeaderWithoutPow.scala`, and `PreGenesisHeader.scala`.

`Header.scala` defines the `Header` class, which represents a block header in the Ergo blockchain. It contains fields such as the block's version, parent ID, ADProofs root, state root, transactions root, timestamp, nBits, height, extension root, proof-of-work solution, and votes. The class also provides methods for interacting with other parts of the Ergo blockchain, such as computing the IDs of corresponding block sections, required difficulty, and checking if a given modifier corresponds to this header.

`HeaderSerializer.scala` is responsible for serializing and deserializing `Header` objects. It provides methods for converting `Header` objects to and from binary format, which is useful when sending block headers over the network or storing them on disk. The object also provides methods for serializing and deserializing `HeaderWithoutPow` objects, which are headers without a proof-of-work solution.

`HeaderWithoutPow.scala` defines a class and an object for creating block headers without a proof-of-work solution. This is useful when the proof-of-work solution is not yet known or needs to be calculated separately. The class provides a method to convert a `HeaderWithoutPow` object to a complete `Header` object with a proof-of-work solution.

`PreGenesisHeader.scala` defines a fake header that is used as a starting point for the blockchain before the actual genesis block is created. It extends the `Header` class and sets most fields to `null` or `0`. The `parentId` field is set to the `GenesisParentId`, and the `height` field is set to `ErgoHistory.EmptyHistoryHeight`.

Here's an example of how this code might be used in the larger Ergo project:

```scala
import org.ergoplatform.modifiers.history.header.{Header, HeaderWithoutPow}
import org.ergoplatform.nodeView.history.ErgoHistory

val history = new ErgoHistory()
val headerWithoutPow = HeaderWithoutPow(version, parentId, ADProofsRoot, stateRoot, transactionsRoot, timestamp, nBits, height, extensionRoot, votes)
val powSolution = AutolykosSolution(...) // Calculate the proof-of-work solution
val header = headerWithoutPow.toHeader(powSolution)

history.append(header)
```

In this example, we import the `Header`, `HeaderWithoutPow`, and `ErgoHistory` classes. We create a new `ErgoHistory` object, a `HeaderWithoutPow` object, and calculate the proof-of-work solution. We then convert the `HeaderWithoutPow` object to a complete `Header` object with the proof-of-work solution and append it to the `ErgoHistory` object. This creates a new block in the blockchain with the given header.
