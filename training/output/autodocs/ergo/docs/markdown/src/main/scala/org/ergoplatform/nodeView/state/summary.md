[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/scala/org/ergoplatform/nodeView/state)

The `.autodoc/docs/json/src/main/scala/org/ergoplatform/nodeView/state` folder contains classes and traits that manage the state of the Ergo blockchain. It includes implementations for both UTXO and Digest states, as well as state readers and context management.

The `BoxHolder.scala` file provides in-memory storage for ErgoBox objects, which are immutable boxes containing assets and data. It is useful for storing genesis state and testing purposes. The `VersionedInMemoryBoxHolder` class extends `BoxHolder` and adds support for in-memory diffs, which is useful for testing.

The `DigestState.scala` file implements a minimal state variant that stores only the digest of the UTXO set authenticated as a dynamic dictionary. It extends the `ErgoState` class and provides methods for validating and applying blocks to the state, as well as rolling back to a previous state.

The `ErgoState.scala` file defines the `ErgoState` trait, which represents the minimal state concept in the Ergo project. It provides methods for applying a modifier to the state, rolling back to a previous version, and getting a read-only view of the state. The `ErgoState` object provides utility methods for handling state changes, executing transactions, and generating genesis states.

The `ErgoStateContext.scala` file represents the context of the Ergo blockchain state, which is required for transaction validation. It provides methods to process and validate headers, extensions, and full blocks against the current state context.

The `SnapshotsInfo.scala` file is a container for UTXO set snapshots that the node holds. It keeps track of the available UTXO set snapshots and their corresponding heights.

The `StateConstants.scala` file defines constants that do not change when the state version changes. These constants are used throughout the codebase for various purposes, such as determining the number of versions of the state that are kept in the database, the voting settings, and the genesis state digest.

The `StateType.scala` file defines the different types of states that can be used in the Ergo platform, such as UTXO and Digest states. It provides methods for converting a state type code to the corresponding `StateType` object and checking the correspondence between a state type and an `ErgoState`.

The `UtxoState.scala` file implements the UTXO set for the Ergo platform, maintaining the state of unspent transaction outputs using an authenticated AVL+ tree. It extends the `ErgoState` trait and provides methods for transaction validation and state modification.

The `UtxoStateReader.scala` file defines a reader for the UTXO state of the Ergo blockchain. It extends the `ErgoStateReader` trait and provides methods for reading the UTXO set's contents and validating transactions.

The `VotingData.scala` file represents and serializes/deserializes voting data for a particular epoch. The `VotingData` case class stores the voting data, and the `VotingDataSerializer` object serializes/deserializes the voting data to/from a byte array.

Overall, this folder is crucial for managing the state of the Ergo blockchain, providing implementations for both UTXO and Digest states, as well as state readers and context management. These classes and traits are used throughout the Ergo project to define and manipulate different types of states, validate transactions, and maintain the integrity of the blockchain.
