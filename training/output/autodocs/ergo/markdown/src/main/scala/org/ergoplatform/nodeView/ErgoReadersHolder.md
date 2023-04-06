[View code on GitHub](https://github.com/ergoplatform/ergo/src/main/scala/org/ergoplatform/nodeView/ErgoReadersHolder.scala)

The `ErgoReadersHolder` class is responsible for holding references to various readers used by the Ergo node view. These readers include `ErgoHistoryReader`, `ErgoStateReader`, `ErgoMemPoolReader`, and `ErgoWalletReader`. The purpose of this class is to provide access to these readers to other parts of the Ergo project.

When an instance of `ErgoReadersHolder` is created, it takes an `ActorRef` to an `ErgoNodeViewHolder` as a parameter. It then subscribes to the `NodeViewChange` event and sends a `GetNodeViewChanges` message to the `ErgoNodeViewHolder` to request changes to the history, state, vault, and mempool readers.

The `ErgoReadersHolder` class has four instance variables, one for each type of reader. These variables are initially set to `None`. When a reader is changed, the corresponding instance variable is updated with the new reader. The `receive` method of the `ErgoReadersHolder` class handles messages that update the readers or request access to them.

The `GetReaders` message is used to request access to the readers. If all readers have been initialized, the `Readers` message is sent back to the sender with references to all four readers. If any readers are not initialized, the `GetReaders` message is scheduled to be sent again in 2 seconds.

The `GetDataFromHistory` message is used to request data from the history reader. If the history reader has not been initialized, a warning is logged. Otherwise, the requested data is sent back to the sender.

The `ErgoReadersHolderRef` object provides a factory method for creating instances of `ErgoReadersHolder`. It takes an `ActorRef` to an `ErgoNodeViewHolder` and an `ActorRefFactory` as parameters and returns an `ActorRef` to an `ErgoReadersHolder`.

Overall, the `ErgoReadersHolder` class provides a way for other parts of the Ergo project to access the history, state, vault, and mempool readers. It ensures that these readers are initialized before they are accessed and provides a way to request data from the history reader.
## Questions: 
 1. What is the purpose of the `ErgoReadersHolder` class?
- The `ErgoReadersHolder` class is responsible for holding and managing instances of `ErgoHistoryReader`, `ErgoStateReader`, `ErgoMemPoolReader`, and `ErgoWalletReader`.

2. What messages can be sent to the `ErgoReadersHolder` actor?
- The `ErgoReadersHolder` actor can receive messages such as `ChangedHistory`, `ChangedState`, `ChangedMempool`, `ChangedVault`, `GetReaders`, and `GetDataFromHistory`.

3. What happens if the `Readers` are not initialized yet when `GetReaders` message is received?
- If the `Readers` are not initialized yet when `GetReaders` message is received, the actor will log a message indicating that the readers are not initialized yet and schedule another `GetReaders` message to be sent after 2 seconds.