[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/scala/org/ergoplatform/modifiers/mempool)

The `.autodoc/docs/json/src/main/scala/org/ergoplatform/modifiers/mempool` folder contains three Scala files that play a crucial role in handling transactions in the Ergo platform. These files are `ErgoTransaction.scala`, `UnconfirmedTransaction.scala`, and `UnsignedErgoTransaction.scala`.

`ErgoTransaction.scala` defines the `ErgoTransaction` class, which represents an atomic state transition operation in the Ergo platform. It is responsible for destroying boxes from the state and creating new ones. The class provides methods for stateless and stateful transaction validation, as well as serialization and deserialization functionality through the `ErgoTransactionSerializer` object. Here's an example of how to create and validate an `ErgoTransaction`:

```scala
val inputs: IndexedSeq[Input] = ...
val dataInputs: IndexedSeq[DataInput] = ...
val outputCandidates: IndexedSeq[ErgoBoxCandidate] = ...

val ergoTransaction = ErgoTransaction(inputs, dataInputs, outputCandidates)

// Stateless validation
val statelessValidationResult = ergoTransaction.statelessValidity()

// Stateful validation
val boxesToSpend: IndexedSeq[ErgoBox] = ...
val dataBoxes: IndexedSeq[ErgoBox] = ...
val stateContext: ErgoStateContext = ...
val accumulatedCost: Long = 0L
implicit val verifier: ErgoInterpreter = ...
val statefulValidationResult = ergoTransaction.statefulValidity(boxesToSpend, dataBoxes, stateContext, accumulatedCost)
```

`UnconfirmedTransaction.scala` defines the `UnconfirmedTransaction` class, which is a wrapper for an unconfirmed transaction and its corresponding data. It is used to manage unconfirmed transactions in the mempool. The class provides methods for updating the cost and the last checked time of the unconfirmed transaction. Here's an example of how to create and update an `UnconfirmedTransaction`:

```scala
val tx = ErgoTransaction(...)
val source = Some(ConnectedPeer(...))
val unconfirmedTx = UnconfirmedTransaction(tx, source)
val updatedUnconfirmedTx = unconfirmedTx.withCost(100)
```

`UnsignedErgoTransaction.scala` defines the `UnsignedErgoTransaction` class, which represents unsigned transactions in the Ergo blockchain. The class extends the `UnsignedErgoLikeTransaction` class and provides methods for creating instances of `UnsignedErgoTransaction`. Here's an example of how to create and sign an `UnsignedErgoTransaction`:

```scala
import org.ergoplatform.modifiers.mempool._

// create an unsigned transaction with two inputs and one output candidate
val inputs = IndexedSeq(UnsignedInput(...), UnsignedInput(...))
val outputCandidates = IndexedSeq(ErgoBoxCandidate(...))
val unsignedTx = UnsignedErgoTransaction(inputs, outputCandidates)

// sign the transaction
val signedTx = unsignedTx.sign(...)

// broadcast the transaction to the network
broadcast(signedTx)
```

These classes work together to handle the creation, validation, and management of transactions in the Ergo platform, which are the building blocks of the blockchain.
