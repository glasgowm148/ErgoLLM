[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/it/scala/org/ergoplatform/it/api)

The `.autodoc/docs/json/src/it/scala/org/ergoplatform/it/api` folder contains two Scala files, `NetworkNodeApi.scala` and `NodeApi.scala`, which provide interfaces for interacting with network nodes and the Ergo blockchain network.

`NetworkNodeApi.scala` defines a trait called `NetworkNodeApi` that provides an interface for interacting with a network node in the Ergo platform. It has several abstract methods, such as `networkAddress`, `networkPort`, `networkNodeName`, `chainId`, and `nonce`, which must be implemented by any class that extends it. The trait also provides a default implementation for a method called `sendByNetwork`, which sends messages to the network node using the `NetworkSender` class. This code can be used in the larger Ergo project to interact with network nodes in the blockchain network.

Example usage:

```scala
class MyNetworkNode extends NetworkNodeApi {
  override def networkAddress: String = "127.0.0.1"
  override def networkPort: Int = 9052
  override def networkNodeName: String = "my-node"
  override def chainId: Char = 'X'
}

val myNode = new MyNetworkNode()
val message = Array[Byte](1, 2, 3)
myNode.sendByNetwork(message).foreach(_ => println("Message sent!"))
```

`NodeApi.scala` defines a trait called `NodeApi` that provides an interface for interacting with a node in the Ergo blockchain network. It offers methods for sending HTTP requests to the node and parsing the responses. The trait also defines several methods for interacting with the Ergo blockchain network, such as `connectedPeers`, `waitForPeers`, and `waitForHeight`. The `NodeApi` trait uses the `AsyncHttpClient` library to send HTTP requests to the node and the `HashedWheelTimer` class to schedule retries of failed requests.

Example usage:

```scala
class MyNodeApi extends NodeApi {
  // Implement required methods
}

val myNodeApi = new MyNodeApi()

// Get connected peers
myNodeApi.connectedPeers().foreach(peers => println(s"Connected peers: $peers"))

// Wait for 5 peers to connect
myNodeApi.waitForPeers(5).foreach(_ => println("5 peers connected"))

// Wait for the node to reach block height 1000
myNodeApi.waitForHeight(1000).foreach(_ => println("Block height 1000 reached"))
```

In summary, the code in this folder provides interfaces for interacting with network nodes and the Ergo blockchain network. These interfaces can be used in the larger Ergo project to send messages to network nodes, query the current state of the blockchain network, or submit new transactions to the network.
