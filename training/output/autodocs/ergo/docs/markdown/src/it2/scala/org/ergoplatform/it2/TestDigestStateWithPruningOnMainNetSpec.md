[View code on GitHub](https://github.com/ergoplatform/ergo/src/it2/scala/org/ergoplatform/it2/TestDigestStateWithPruningOnMainNetSpec.scala)

The code is a Scala test file that tests the functionality of a node in the Ergo platform. The purpose of the code is to start a node with specific configurations, wait for it to synchronize with the network, and then test its functionality. 

The code imports several libraries and classes from the Ergo platform, including `NodeApi.NodeInfo`, `IntegrationSuite`, and `Node`. It also imports libraries from Scala, including `async` and `Await`. 

The `TestDigestStateWithPruningOnMainNetSpec` class extends `AnyFlatSpec` and `IntegrationSuite` and uses `OptionValues`. It defines a `nodeConfig` variable that is a `Config` object with specific configurations for the node. These configurations include `digestStatePeerConfig`, `prunedHistoryConfig`, and `nonGeneratingPeerConfig`. 

The `node` variable is a `Node` object that is created by starting a mainnet node with the `nodeConfig` configurations. The `get` method is called on the `docker.startMainNetNodeYesImSure` method to start the node. 

The `it should` block defines a test case that checks if the node is able to synchronize with the network. The `Async.async` method is called to create an asynchronous block of code that waits for the node to synchronize with the network. The `node.waitFor` method is called with a timeout of 1 minute to wait for the node to return a `NodeInfo` object. The `NodeInfo` object contains information about the node, including its best block height. The `exists` method is called on the `bestBlockHeightOpt` and `bestHeaderHeightOpt` properties of the `NodeInfo` object to check if they are equal. If they are equal, the node has synchronized with the network. 

The `Await.result` method is called to wait for the asynchronous block of code to complete. The timeout for this method is set to 4 hours. 

Overall, this code tests the ability of a node in the Ergo platform to synchronize with the network. It can be used as a part of a larger project to ensure that nodes in the network are functioning properly.
## Questions: 
 1. What is the purpose of the `TestDigestStateWithPruningOnMainNetSpec` class?
- This class is a test suite that checks if a node with stateType=digest and pruning can be started on the mainnet and synced successfully.

2. What dependencies are being imported in this file?
- This file is importing dependencies from `com.typesafe.config`, `org.ergoplatform.it.api`, `org.ergoplatform.it.container`, `org.scalatest`, and `scala` libraries.

3. What is the significance of the `nodeSeedConfigs`, `digestStatePeerConfig`, `prunedHistoryConfig`, and `nonGeneratingPeerConfig` variables?
- These variables are used to configure the `nodeConfig` object, which is then used to start a node on the mainnet with stateType=digest and pruning enabled. The `nodeSeedConfigs` variable is a list of seed node configurations, `digestStatePeerConfig` is a configuration for a node with stateType=digest, `prunedHistoryConfig` is a configuration for a node with pruning enabled, and `nonGeneratingPeerConfig` is a configuration for a node that does not generate blocks.