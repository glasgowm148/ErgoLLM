[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/ergo-wallet/src/main/scala/org/ergoplatform/wallet/transactions)

The `TransactionBuilder.scala` file in the `org.ergoplatform.wallet.transactions` package provides methods and utilities for building unsigned Ergo transactions. This is an essential part of the Ergo wallet, as it allows users to create and sign transactions before broadcasting them to the network.

The main functionality of this file is provided by the `TransactionBuilder` object, which contains several methods for creating unsigned transactions:

- `multiPaymentTransaction`: This method assembles an unsigned payment transaction with multiple outputs. It takes an array of input identifiers, a fee amount, a list of payment addresses and corresponding amounts, a change recipient address, a change amount, and the current blockchain height. It returns an unsigned transaction.

- `paymentTransaction`: This method assembles an unsigned payment transaction. It takes a payment recipient address, a change recipient address, an amount of ERGs to transfer, a fee amount, an amount to return back to the change address, an array of input identifiers, and the current blockchain height. It returns an unsigned transaction.

The `TransactionBuilder` object also contains utility methods for working with tokens and token maps:

- `collectOutputTokens`: This method takes a sequence of ErgoBoxCandidates and returns a TokensMap.

- `collTokensToMap`: This method takes a Coll of TokenIds and Longs and returns a Map of ModifierIds and Longs.

- `tokensMapToColl`: This method takes a TokensMap and returns a Coll of TokenIds and Longs.

The `buildUnsignedTx` method is another important part of the `TransactionBuilder` object. It creates an unsigned transaction from given inputs and outputs, adding outputs with miner's fee and change. It runs required checks ensuring that the resulted transaction will be successfully validated by a node. It takes in inputs, data inputs, output candidates, the current height, an optional fee amount to put in a new miner's fee box, which will be created by this method, a change address, a minimum change value to send, a reward delay to encode in the miner's fee box, and a TokensMap of tokens to burn. It returns a Try of an unsigned transaction.

The `EitherOpsFor211` class is an implicit class that provides additional functionality to the Either class. It contains the `mapRight` and `flatMapRight` methods, which apply a function to the right value of an Either or bind a function across the right value of an Either, respectively.

Example usage of the `TransactionBuilder` object:

```scala
val inputIds: Array[ModifierId] = ...
val feeAmount: Long = ...
val paymentAddresses: List[Address] = ...
val paymentAmounts: List[Long] = ...
val changeAddress: Address = ...
val changeAmount: Long = ...
val currentHeight: Int = ...

val unsignedTx = TransactionBuilder.multiPaymentTransaction(
  inputIds,
  feeAmount,
  paymentAddresses,
  paymentAmounts,
  changeAddress,
  changeAmount,
  currentHeight
)
```

In summary, the `TransactionBuilder.scala` file provides essential functionality for creating unsigned Ergo transactions, which is a crucial part of the Ergo wallet. It allows users to create and sign transactions before broadcasting them to the network, and it provides utility methods for working with tokens and token maps.
