[View code on GitHub](https://github.com/ergoplatform/ergo/src/main/scala/scorex/core/network/PeerConnectionHandler.scala)

The `PeerConnectionHandler` class is responsible for handling incoming and outgoing messages between two peers in the Ergo network. It is an Akka actor that manages the TCP connection with a remote peer and implements the Ergo protocol for message exchange.

When a new connection is established, the `PeerConnectionHandler` sends a handshake message to the remote peer and waits for a response. If the handshake is successful, the `PeerConnectionHandler` notifies the `NetworkController` that a new peer has been connected and enters the working cycle. If the handshake fails, the `PeerConnectionHandler` adds the peer to the blacklist and closes the connection.

During the working cycle, the `PeerConnectionHandler` can receive and send messages to the remote peer. Incoming messages are deserialized and forwarded to the `NetworkController` for further processing. Outgoing messages are serialized and sent to the remote peer. If a message fails to be sent, the `PeerConnectionHandler` switches to buffering mode and stores the message in a buffer until it can be sent successfully. Once all buffered messages have been sent, the `PeerConnectionHandler` returns to the working cycle.

The `PeerConnectionHandler` also handles connection errors and closes the connection if necessary. If the connection is closed by the remote peer, the `PeerConnectionHandler` stops itself. If the connection is closed due to an error or is aborted, the `PeerConnectionHandler` logs the reason and stops itself.

Overall, the `PeerConnectionHandler` is a crucial component of the Ergo network that enables peers to communicate with each other and exchange messages according to the Ergo protocol.
## Questions: 
 1. What is the purpose of the `PeerConnectionHandler` class?
- The `PeerConnectionHandler` class is responsible for handling the connection with a peer in the network, including sending and receiving messages and managing the connection state.

2. How does the `PeerConnectionHandler` handle buffering of outgoing messages?
- The `PeerConnectionHandler` operates in ACK mode until all buffered messages are transmitted. When a message fails to write, it switches to buffering mode and buffers the message. It then waits for ACKs for each message and removes them from the buffer once they are acknowledged. If there are still messages in the buffer, it continues to operate in ACK mode until all messages are transmitted.

3. What happens if the `PeerConnectionHandler` receives corrupted data from a peer?
- If the `PeerConnectionHandler` receives corrupted data from a peer, it logs the error message and ignores the data. If the corruption is due to malicious behavior, it bans the peer by adding it to the blacklist and sending a `PenalizePeer` message to the `NetworkController` to close the connection.