[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/scala/org/ergoplatform/reemission)

The `ReemissionRules.scala` file in the `org.ergoplatform.reemission` package is responsible for handling the re-emission feature of the Ergo blockchain. This feature allows unlocking of re-emission tokens at specific block heights, which can be used to support the network's long-term sustainability.

The `ReemissionRules` class extends the `ReemissionContracts` trait, which defines the re-emission contracts. It also contains a `basicChargeAmount` variable that specifies the initial amount of ERG taken from emission to re-emission. The main functionality of this class is provided by the `reemissionForHeight` method, which calculates how many re-emission tokens can be unlocked at a given height. This method takes a height and an `EmissionRules` object as input parameters and returns the number of unlockable re-emission tokens based on the conditions specified in the method.

The `ReemissionRules` object provides additional utility functions for the re-emission feature. The `injectionBoxP2SAddress` method creates a Pay2SAddress object for a box used to carry emission NFT and re-emission tokens. This box is used to inject these tokens into the emission box at the activation height. The method takes a boolean `mainnet` parameter and returns the Pay2SAddress object based on the conditions specified in the method.

Additionally, the `ReemissionRules` object contains a `main` method that prints various information about the monetary and re-emission settings, emission rules, and re-emission rules. This method is useful for developers to understand the current state of the re-emission feature and its impact on the Ergo blockchain.

In the larger Ergo project, the `ReemissionRules` class and object work together with other components, such as the `EmissionRules` class, to manage the emission and re-emission of tokens in the Ergo blockchain. For example, the `reemissionForHeight` method can be used to calculate the number of re-emission tokens that can be unlocked at a specific block height:

```scala
val height = 1000
val emissionRules = new EmissionRules(...)
val reemissionRules = new ReemissionRules(...)
val unlockableTokens = reemissionRules.reemissionForHeight(height, emissionRules)
```

Overall, the `ReemissionRules.scala` file plays a crucial role in managing the re-emission feature of the Ergo blockchain, providing the necessary contracts and utility functions to calculate and unlock re-emission tokens at specific block heights.
