[View code on GitHub](https://github.com/ergoplatform/ergo/src/main/scala/org/ergoplatform/nodeView/state/SnapshotsInfo.scala)

The `SnapshotsInfo` class is a container for UTXO (Unspent Transaction Output) set snapshots that the node holds. It takes in a map of available UTXO set snapshot manifests and corresponding heights. The purpose of this class is to keep track of the available UTXO set snapshots and their corresponding heights. 

The `withNewManifest` method is used to add a new snapshot to the container. It takes in a height and a manifest ID and returns a new instance of the `SnapshotsInfo` class with the new snapshot added. This method is useful for updating the container with new snapshots as they become available.

The `nonEmpty` method is used to check whether there are any snapshots available in the container. It returns a boolean value indicating whether the container is empty or not. This method is useful for checking whether there are any snapshots available before attempting to access them.

The `SnapshotsInfo` object provides an empty container with no snapshots. This is useful for initializing a new `SnapshotsInfo` instance with no snapshots.

Overall, the `SnapshotsInfo` class is an important component of the larger project as it helps to keep track of the available UTXO set snapshots. This information is critical for validating transactions and maintaining the integrity of the blockchain. Here is an example of how this class might be used in the larger project:

```
val snapshots = SnapshotsInfo.empty
val newSnapshot = // get new snapshot from somewhere
snapshots = snapshots.withNewManifest(newSnapshot.height, newSnapshot.manifestId)
if (snapshots.nonEmpty) {
  // do something with available snapshots
}
```
## Questions: 
 1. What is the purpose of the `SnapshotsInfo` class?
    
    The `SnapshotsInfo` class is a container for UTXO set snapshots that the node holds.

2. What is the purpose of the `withNewManifest` method?
    
    The `withNewManifest` method returns a new container instance with a new snapshot added.

3. What is the purpose of the `empty` object in the `SnapshotsInfo` companion object?
    
    The `empty` object is an empty container with no snapshots.