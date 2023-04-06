[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/scala/org/ergoplatform/tools)

The `.autodoc/docs/json/src/main/scala/org/ergoplatform/tools` folder contains two Scala files, `CoinEmissionPrinter.scala` and `ValidationRulesPrinter.scala`, which provide tools for printing information about the Ergo blockchain's coin emission schedule and validation rules, respectively.

`CoinEmissionPrinter.scala` is a tool that prints information about the coin emission schedule of the Ergo blockchain. It calculates the total coin supply and block rewards for miners and the foundation using the `EmissionRules` and `MonetarySettings` classes. The `CoinEmissionPrinter` object defines two lazy values, `TotalSupply` and `FirstYearSupply`, which calculate the total coin supply of the Ergo blockchain and the total coin supply for the first year, respectively. The `loop` function iterates over all blocks up to the total number of blocks defined in the `EmissionRules` object, calculating block rewards for miners and the foundation, and printing information about the block rewards and the total coin supply at intervals of 100,000 blocks. This tool can be used to monitor the coin emission schedule of the Ergo blockchain and to calculate the expected block rewards for miners and the foundation at a given block height.

Example usage:

```scala
object CoinEmissionPrinterApp extends App {
  CoinEmissionPrinter.printEmissionSchedule()
}
```

`ValidationRulesPrinter.scala` is a tool used to print out the validation rules for transactions, headers, block sections, and block application to state validation in the Ergo platform. The purpose of this tool is to provide a way for developers to easily view and understand the validation rules that are in place for each of these components. The `ValidationRulesPrinter` object contains a `main` method that prints out the validation rules for each component, iterating through each validation rule and checking if it is a fatal error, and printing out the rule ID, the validation rule itself, whether it is soft-forkable, whether it is active, and the affected modifiers. The tool also includes several helper methods, such as `printHeader` and `boolToLatex`. This tool is useful for developers working on the Ergo platform to easily view and understand the validation rules in place for each component.

Example usage:

```scala
object ValidationRulesPrinterApp extends App {
  ValidationRulesPrinter.main(Array.empty)
}
```

In summary, the `org.ergoplatform.tools` folder provides two tools for printing information about the Ergo blockchain's coin emission schedule and validation rules. These tools can be helpful for developers working on the Ergo platform to monitor the coin emission schedule, calculate expected block rewards, and understand the validation rules in place for various components.
