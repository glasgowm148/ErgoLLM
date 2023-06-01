[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/ergo-wallet/src/main/scala/org/ergoplatform/wallet/protocol/context)

The `.autodoc/docs/json/ergo-wallet/src/main/scala/org/ergoplatform/wallet/protocol/context` folder contains code related to the context of various aspects of the Ergo blockchain, such as transaction validation, input context, and blockchain parameters.

`ErgoLikeParameters.scala` defines a trait representing a set of adjustable blockchain parameters and voting-related data. These parameters can be accessed and modified by developers working on the Ergo project. For instance, they can use the `softForkStartingHeight` parameter to determine when a soft-fork should be started or the `maxBlockCost` parameter to limit the computation units per block.

`ErgoLikeStateContext.scala` provides context information about the blockchain state during transaction validation. It is likely used in conjunction with other traits and classes to validate transactions against the current state of the blockchain. An example usage of this trait might look like:

```scala
class MyTransactionValidator extends ErgoLikeTransactionValidator {
  def validate(tx: ErgoTransaction, context: ErgoLikeStateContext): Boolean = {
    // use context information to validate transaction
    val headers = context.sigmaLastHeaders
    val prevDigest = context.previousStateDigest
    val preHeader = context.sigmaPreHeader
    // perform validation logic
    true
  }
}
```

`InputContext.scala` defines a case class used to store information about a box being spent in a transaction, including its index and any additional context provided during the spending process. This information can be used by other parts of the Ergo platform to ensure that transactions are executed correctly and securely. Here's an example of how the `InputContext` case class might be used:

```scala
import org.ergoplatform.wallet.protocol.context.InputContext

// create an InputContext for a box being spent
val inputContext = InputContext(0, Map("key1" -> "value1", "key2" -> "value2"))

// use the InputContext to execute a transaction
val result = executeTransaction(inputContext)

// check the result of the transaction
if (result.isSuccess) {
  println("Transaction executed successfully!")
} else {
  println("Transaction failed.")
}
```

`TransactionContext.scala` provides a context for executing a spending transaction. It allows the user to specify the inputs and data inputs of the transaction, as well as the spending transaction itself. This context can then be used in other parts of the Ergo project to execute the transaction. For example, a user could create a new instance of `TransactionContext` and pass in the necessary inputs and spending transaction, then use this context to execute the transaction and update the blockchain accordingly.

Overall, the code in this folder plays a crucial role in the Ergo project by providing context information for various aspects of the blockchain, such as transaction validation, input context, and adjustable blockchain parameters.
