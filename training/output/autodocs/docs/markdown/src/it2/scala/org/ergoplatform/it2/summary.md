[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/it2/scala/org/ergoplatform/it2)

The code in this folder contains Scala test files that test the functionality of nodes in the Ergo platform. These tests ensure that nodes can be started with specific configurations, synchronize with the network, and function correctly. The tests are written using the ScalaTest library, specifically the `AnyFlatSpec` testing style, which allows for a flat structure in test cases.

For example, the `TestDigestStateOnMainNetSpec.scala` file tests the ability of a node with `stateType=digest` to start on the Ergo network and fully sync with the network. The test case is defined using the `it should` method and an asynchronous block of code is executed using the `Async.async` method. The `node.waitFor` method is called with a function that returns a `NodeInfo` object, a predicate that checks if the node is fully synced, and a timeout duration. The `Await.result` method is used to wait for the asynchronous block of code to complete.

Similarly, the `TestDigestStateWithPruningOnMainNetSpec.scala` file tests the ability of a node with specific configurations, such as `digestStatePeerConfig`, `prunedHistoryConfig`, and `nonGeneratingPeerConfig`, to synchronize with the network. The test case checks if the `bestBlockHeightOpt` and `bestHeaderHeightOpt` properties of the `NodeInfo` object are equal, indicating that the node has synchronized with the network.

The `TestOnMainNetSpec.scala` file tests the functionality of a node in the Ergo platform by starting a node on the mainnet and waiting for a full sync. The test case uses the `Async.async` method to create an asynchronous block of code that waits for the node to return a `NodeInfo` object. The `node.waitFor` method is called with a predicate that checks if the `bestBlockHeightOpt` exists and is equal to the `bestHeaderHeightOpt`, and a timeout of 1 minute.

These test cases can be run as part of a larger suite of tests to ensure that nodes in the Ergo network are functioning properly. For example, to run all the tests in the Ergo project, including the test cases in this folder, you can use the following command:

```
sbt test
```

Overall, the code in this folder is crucial for ensuring the proper functioning of nodes in the Ergo platform and can be used by developers to verify that their changes do not break the expected behavior of the nodes.
