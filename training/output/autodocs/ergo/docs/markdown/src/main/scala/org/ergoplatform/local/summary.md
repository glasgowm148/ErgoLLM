[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/scala/org/ergoplatform/local)

The `.autodoc/docs/json/src/main/scala/org/ergoplatform/local` folder contains classes responsible for managing the mempool, collecting node statistics, and verifying PoPoW proofs in the Ergo platform.

`CleanupWorker.scala` is responsible for re-validating mempool transactions when a new block arrives. It validates transactions for a specified amount of time and updates the valid transactions and invalidated transaction ids. This class ensures that mempool transactions are validated and updated correctly, contributing to the security and validity of the blockchain.

Example usage:

```scala
val cleanupWorker = context.actorOf(CleanupWorker.props)
cleanupWorker ! CleanupWorker.RunCleanup(validator, mempool)
```

`ErgoStatsCollector.scala` collects and provides statistics about the Ergo node to API requests. It subscribes to `NodeViewHolderEvents` and gathers information about the node's state, history, and mempool. This class is useful for developers and users to monitor the node's status and performance.

Example usage:

```scala
val statsCollector = context.actorOf(ErgoStatsCollector.props(readersHolder, networkController, syncTracker, settings))
```

`MempoolAuditor.scala` controls the mempool cleanup workflow by watching NodeView events and delegating the cleanup task to the `CleanupWorker`. It ensures that the mempool is cleaned up periodically and that all transactions in the mempool are valid.

Example usage:

```scala
val mempoolAuditor = context.actorOf(MempoolAuditor.props)
mempoolAuditor ! MempoolAuditor.RecheckMempool(stateReader, mempoolReader)
```

`NipopowVerifier.scala` verifies PoPoW proofs and determines the best (sub)chain rooted at the specified genesis block. It can be used in a consensus algorithm to determine the valid chain in the network.

Example usage:

```scala
val verifier = new NipopowVerifier(genesisBlockId)
val proof = new NipopowProof(headersChain)
verifier.process(proof)
val bestChain: Seq[Header] = verifier.bestChain
```

These classes work together to maintain the integrity of the Ergo platform by ensuring that mempool transactions are validated, node statistics are collected, and PoPoW proofs are verified. They can be used in the larger project to ensure that the blockchain is secure, transactions are validated correctly, and the node's status and performance are monitored.
