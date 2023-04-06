[View code on GitHub](https://github.com/ergoplatform/ergo/src/main/scala/org/ergoplatform/nodeView/mempool/ErgoMemPool.scala)

The `ErgoMemPool` class is an implementation of an immutable memory pool for the Ergo platform. It stores unconfirmed transactions and provides various methods to interact with the transactions in the pool. The memory pool is sorted based on a specified sorting option, either by fee-per-byte or fee-per-cycle.

The `put` method adds a transaction to the memory pool, while the `remove` method removes a transaction from the pool. The `invalidate` method marks a transaction as invalid and removes it from the pool. The `isInvalidated` method checks if a transaction has been invalidated earlier.

The `process` method validates a transaction against the current state and decides whether to accept, decline, or invalidate the transaction. It also handles double-spending transactions by comparing their weights (fee/byte or fee/cycle) with existing transactions in the pool.

The `getRecommendedFee` method returns the recommended fee for a transaction to be processed within a specified wait time interval, based on the pool's current state. The `getExpectedWaitTime` method calculates the estimated wait time for a transaction to be included in a block, given its fee and size.

The `ErgoMemPool` class also provides methods to retrieve transactions from the pool, such as `modifierById`, `contains`, `take`, `random`, `getAll`, `getAllPrioritized`, and `spentInputs`.

Example usage:

```scala
val ergoSettings: ErgoSettings = ...
val emptyPool: ErgoMemPool = ErgoMemPool.empty(ergoSettings)

val unconfirmedTx: UnconfirmedTransaction = ...
val updatedPool: ErgoMemPool = emptyPool.put(unconfirmedTx)

val txId: ModifierId = ...
val txOpt: Option[ErgoTransaction] = updatedPool.modifierById(txId)
```

Overall, the `ErgoMemPool` class plays a crucial role in managing unconfirmed transactions in the Ergo platform, ensuring that transactions are validated, prioritized, and processed efficiently.
## Questions: 
 1. **Question**: What are the different sorting strategies for mempool transactions, and how are they chosen?
   **Answer**: There are two sorting strategies for mempool transactions: `FeePerByte` and `FeePerCycle`. `FeePerByte` sorts transactions by fee paid for transaction size, while `FeePerCycle` sorts transactions by fee paid for transaction contracts validation cost. The sorting strategy is chosen based on the `settings.nodeSettings.mempoolSorting` value, which can be set in the configuration.

2. **Question**: How does the `getRecommendedFee` method work, and what does it return?
   **Answer**: The `getRecommendedFee` method calculates the recommended fee value for a transaction to be processed within a specified time. It takes two parameters: `expectedWaitTimeMinutes`, which is the maximal amount of time for which the transaction can be kept in the mempool, and `txSize`, which is the size of the transaction in bytes. The method iterates through the mempool statistics histogram to find the average fee for the specified wait time interval and returns the recommended fee value based on the transaction size.

3. **Question**: What is the purpose of the `ProcessingOutcome` trait and its subclasses?
   **Answer**: The `ProcessingOutcome` trait represents the root of the possible mempool transaction validation result hierarchy. Its subclasses represent different outcomes of processing a transaction in the mempool, such as `Accepted` (transaction is accepted to the memory pool), `DoubleSpendingLoser` (transaction is rejected due to double-spending inputs of mempool transactions), `Declined` (transaction is declined from being accepted into the memory pool), and `Invalidated` (transaction is found to be invalid when checked in the mempool).