[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/scala/org/ergoplatform/nodeView/history/storage)

The `HistoryStorage.scala` file contains the `HistoryStorage` class, which serves as a storage implementation for Ergo's history. It is responsible for storing and retrieving blocks, headers, and other objects related to Ergo's blockchain. The class utilizes three key-value stores: `indexStore`, `objectsStore`, and `extraStore`. The `indexStore` stores indexes required for efficient history management, such as links to the best header, best full block, heights, and scores for different blocks. The `objectsStore` stores blocks and headers, while the `extraStore` stores extra indexes.

To improve performance, the class employs four caches: `headersCache`, `blockSectionsCache`, `extraCache`, and `indexCache`. The `headersCache` and `blockSectionsCache` store headers and blocks, respectively. The `extraCache` stores extra indexes, and the `indexCache` stores indexes.

The class provides methods for inserting and removing blocks, headers, and indexes from the stores, as well as methods for retrieving them. It uses the `HistoryModifierSerializer` and `ExtraIndexSerializer` to serialize and deserialize blocks and indexes, respectively.

Other classes in the Ergo project use the `HistoryStorage` class to store and retrieve blocks, headers, and indexes. For example, the `History` class uses it to store and retrieve blocks and headers, the `StateContext` class retrieves blocks and headers for state validation, and the `UtxoState` class retrieves blocks and headers for UTXO set validation.

Example usage:

```scala
val ergoSettings: ErgoSettings = ???
val historyStorage: HistoryStorage = HistoryStorage(ergoSettings)

// Insert a block
val block: Block = ???
historyStorage.insert(Array.emptyByteArray, Array(block))

// Retrieve a block by id
val blockId: ModifierId = ???
val blockBytes: Option[Array[Byte]] = historyStorage.modifierBytesById(blockId)

// Remove a block by id
historyStorage.remove(Array.emptyByteArray, Array(blockId))
```

The `.autodoc/docs/json/src/main/scala/org/ergoplatform/nodeView/history/storage/modifierprocessors` folder contains traits and classes for processing and validating different parts of the Ergo blockchain, such as block headers, block sections, and extensions. These components maintain the consistency and security of the Ergo blockchain.

For instance, the `BasicReaders` trait provides basic read-only functionality for accessing data stored in the Ergo blockchain. The `BlockSectionProcessor` trait declares interfaces for validation and processing of various block sections, allowing for modular and extensible code design.

The `HeadersProcessor` trait processes and validates block headers in the Ergo blockchain, managing the history of block headers and calculating the required difficulty for the next block. The `FullBlockProcessor` extends the `HeadersProcessor` and focuses on handling transactions and proofs while pruning modifiers older than `blocksToKeep`.

The `ToDownloadProcessor` trait calculates the next set of modifiers to download for synchronizing a node's full chain with the headers chain. It provides a method `nextModifiersToDownload` that returns a map of modifier ids to download, filtered by a given condition.

Example usage:

```scala
class MyNode extends ToDownloadProcessor with BasicReaders {
  protected val settings: ErgoSettings = ???

  protected def headerChainBack(limit: Int, startHeader: Header, until: Header => Boolean): HeaderChain = ???

  def isInBestChain(id: ModifierId): Boolean = ???
}

val node = new MyNode()
val modifiersToDownload = node.nextModifiersToDownload(10, Some(1000), (mtid, mid) => true)
val blockIds: Seq[ModifierId] = node.headerIdsAtHeight(100)
val block: Option[ErgoFullBlock] = node.bestFullBlockOpt
val tx: Option[ErgoTransaction] = node.typedModifierById[ErgoTransaction](txId)
val containsBlock: Boolean = node.contains(blockId)
```

In summary, the code in this folder plays a vital role in the Ergo project by providing the necessary components for processing and validating different parts of the Ergo blockchain. These components ensure the integrity and consistency of the blockchain, allowing the Ergo node to maintain an accurate and up-to-date view of the blockchain.
