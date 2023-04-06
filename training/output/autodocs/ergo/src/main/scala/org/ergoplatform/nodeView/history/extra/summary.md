[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/scala/org/ergoplatform/nodeView/history/extra)

The `.autodoc/docs/json/src/main/scala/org/ergoplatform/nodeView/history/extra` folder contains various classes and objects that are used to index and manage data related to Ergo blockchain elements, such as transactions, boxes, and addresses. These indices improve the efficiency of querying and accessing data in the Ergo project.

For example, the `BalanceInfo` class is used to track ERG and token balances in an `IndexedErgoAddress`. It provides methods to add and subtract boxes, which update the balances accordingly. The `BalanceInfoSerializer` object is used to serialize and deserialize `BalanceInfo` objects.

The `ExtraIndexSerializer` object provides serialization and deserialization functionality for objects of type `ExtraIndex`, which includes subclasses like `IndexedErgoAddress`, `IndexedErgoBox`, and `IndexedErgoTransaction`. This functionality is used to store and retrieve `ExtraIndex` objects in a serialized format, for example in a database or on disk.

The `ExtraIndexer` actor is an Akka actor that constructs an index of database elements to improve the efficiency of querying and accessing data. It processes blocks, transactions, and boxes in the Ergo blockchain and maintains various buffers for fast access to data.

The `IndexedErgoAddress` class represents an index of an Ergo address and its associated transactions and boxes. It provides methods for adding and spending boxes, retrieving transactions and boxes, and rolling back the state of the address. The `IndexedErgoAddressSerializer` object provides methods to serialize and deserialize `IndexedErgoAddress` instances.

The `IndexedErgoBox` class is a wrapper for an `ErgoBox` object with additional information, such as the height of the block in which the creating transaction was included and whether the box is spent. The `IndexedErgoBoxSerializer` object provides serialization and deserialization methods for the `IndexedErgoBox` class.

The `IndexedErgoTransaction` class represents a transaction in the Ergo blockchain and stores the minimum information required for a transaction to save space. It provides methods to retrieve additional information about the transaction from the database. The `IndexedErgoTransactionSerializer` object provides serialization and deserialization methods for the `IndexedErgoTransaction` class.

The `IndexedToken` class defines a token index for the Ergo blockchain, tracking the creation information of each token. The `IndexedTokenSerializer` object provides serialization and deserialization methods for the `IndexedToken` class.

The `NumericIndex` code defines two case classes, `NumericTxIndex` and `NumericBoxIndex`, which represent numeric indices pointing to transactions and boxes respectively. These indices are used to retrieve transactions and boxes from a database. The `NumericTxIndexSerializer` and `NumericBoxIndexSerializer` objects define methods for serializing and deserializing instances of these case classes.

Example usage of `ExtraIndexer`:

```scala
val indexer = ExtraIndexer(chainSettings, cacheSettings)(system)
indexer ! StartExtraIndexer(history)
```

This creates an instance of the `ExtraIndexer` actor and starts the indexing process with the given `history`.
