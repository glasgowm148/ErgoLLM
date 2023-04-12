[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/scala/org/ergoplatform/nodeView/wallet/models)

The code in the `.autodoc/docs/json/src/main/scala/org/ergoplatform/nodeView/wallet/models` folder contains two Scala files, `ChangeBox.scala` and `CollectedBoxes.scala`, which define models for the Ergo wallet API.

`ChangeBox.scala` defines a model for a change box, which is a type of output box created when a transaction spends more than one input box. The `ChangeBox` class has two properties: `value`, representing the amount of Ergs in the change box, and `tokens`, a map containing the IDs and amounts of other tokens in the change box. The `ModifierId` type is used as the key for the `tokens` map. The file also defines two implicit encoders for converting `ChangeBox` instances to JSON objects using the Circe library.

Example usage of `ChangeBox`:

```scala
import org.ergoplatform.nodeView.wallet.models.ChangeBox

val tokens = Map(
  "token1" -> 100L,
  "token2" -> 200L
)

val changeBox = ChangeBox(500L, tokens)

println(changeBox)
// Output: ChangeBox(500,Map(token1 -> 100, token2 -> 200))
```

`CollectedBoxes.scala` defines a case class called `CollectedBoxes` that represents a response for requested boxes containing `ErgoBoxes` and `ChangeBoxes`. The `CollectedBoxes` class has two fields: `boxes` and `changeBoxes`, both sequences of `ErgoBox` and `ChangeBox` objects, respectively. The purpose of this class is to group together the boxes that satisfy a user's request and the boxes with excessive tokens and ergs. The file also defines an `encoder` for converting `CollectedBoxes` instances to JSON objects using the Circe library.

Example usage of `CollectedBoxes`:

```scala
val ergoBoxes: Seq[ErgoBox] = Seq(ErgoBox(), ErgoBox())
val changeBoxes: Seq[ChangeBox] = Seq(ChangeBox(), ChangeBox())

val collectedBoxes = CollectedBoxes(ergoBoxes, changeBoxes)

val json = collectedBoxes.asJson
println(json)
// Output: {"boxes":[{"value":0,"ergoTree":"", ... }],"changeBoxes":[{"value":0,"ergoTree":"", ... }]}
```

These models are likely used in the larger Ergo project to represent change boxes and collected boxes in the wallet API. When a transaction is created in the Ergo system, the inputs and outputs are defined, and if the sum of the inputs is greater than the sum of the outputs, a change box is created to hold the leftover amount. The `ChangeBox` model represents this change box, while the `CollectedBoxes` model groups together the boxes that satisfy a user's request and the boxes with excessive tokens and ergs. The resulting JSON objects can be easily transmitted over the network or stored in a database.
