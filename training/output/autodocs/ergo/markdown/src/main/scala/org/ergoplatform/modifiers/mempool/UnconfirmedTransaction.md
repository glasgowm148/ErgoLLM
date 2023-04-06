[View code on GitHub](https://github.com/ergoplatform/ergo/src/main/scala/org/ergoplatform/modifiers/mempool/UnconfirmedTransaction.scala)

The `UnconfirmedTransaction` class is a wrapper for an unconfirmed transaction and its corresponding data. It contains the transaction itself, the validation cost during the last check, the time when the transaction entered the pool, the time when the last validity check was done, the transaction bytes, and the peer which delivered the transaction (if any). 

The `UnconfirmedTransaction` class has two constructors. The first constructor takes the transaction, the last cost, the created time, the last checked time, the transaction bytes, and the source peer as parameters. The second constructor takes the transaction, the transaction bytes, and the source peer as parameters. In both cases, the created time and the last checked time are set to the current time. 

The `UnconfirmedTransaction` class has a method `withCost` that updates the cost and the last checked time of the unconfirmed transaction. It returns a new `UnconfirmedTransaction` object with the updated values. 

The `UnconfirmedTransaction` class also overrides the `equals` and `hashCode` methods. It checks if the `id` of the `UnconfirmedTransaction` object is equal to the `id` of the other object. 

The `UnconfirmedTransaction` object has two factory methods. The first factory method takes the transaction and the source peer as parameters. It creates a new `UnconfirmedTransaction` object with the current time as the created time and the last checked time, and the transaction bytes set to the bytes of the transaction. The second factory method takes the transaction, the transaction bytes, and the source peer as parameters. It creates a new `UnconfirmedTransaction` object with the current time as the created time and the last checked time. 

This code is part of the `ergo` project and is used to manage unconfirmed transactions in the mempool. The `UnconfirmedTransaction` class is used to store unconfirmed transactions and their corresponding data. The `UnconfirmedTransaction` object is used to create new `UnconfirmedTransaction` objects. The `UnconfirmedTransaction` class and object are used by other classes in the `ergo` project to manage the mempool. 

Example usage:

```
val tx = ErgoTransaction(...)
val source = Some(ConnectedPeer(...))
val unconfirmedTx = UnconfirmedTransaction(tx, source)
val updatedUnconfirmedTx = unconfirmedTx.withCost(100)
```
## Questions: 
 1. What is the purpose of the `UnconfirmedTransaction` class?
- The `UnconfirmedTransaction` class is a wrapper for an unconfirmed transaction and its corresponding data, such as validation cost and creation time.

2. What is the difference between the two `apply` methods in the `UnconfirmedTransaction` object?
- The first `apply` method takes an `ErgoTransaction` and a `ConnectedPeer` as input, while the second `apply` method takes an `ErgoTransaction`, an array of bytes, and a `ConnectedPeer` as input. The second method allows for the transaction bytes to be passed in directly, rather than being serialized.

3. What is the purpose of the `withCost` method in the `UnconfirmedTransaction` class?
- The `withCost` method updates the validation cost and last checked time of an unconfirmed transaction.