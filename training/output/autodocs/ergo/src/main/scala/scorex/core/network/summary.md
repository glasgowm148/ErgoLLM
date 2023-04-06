[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/scala/scorex/core/network)

The code in the `scorex.core.network` package is responsible for managing network communication within the Ergo project. It provides classes and objects for representing connected peers, handling network messages, and managing connections between nodes.

For example, the `ConnectedPeer` class represents a peer connected to the node and contains information about the connection, such as the connection address, a reference to the `PeerConnectionHandler`, and the timestamp of the last received message. The `ConnectionDescription` class represents a connection between two nodes and contains information about the connection, such as the connection actor, connection ID, local address, and local features.

The `NetworkController` class manages all network interactions, including establishing and maintaining connections with peers, handling incoming and
