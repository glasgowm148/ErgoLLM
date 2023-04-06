[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/scala/org/ergoplatform/nodeView/wallet/persistence)

The code in the `persistence` folder is responsible for managing wallet-related data and persisting the wallet's mutable state. It provides classes and methods for representing wallet balances, handling off-chain data, and managing wallet-specific indexes.

For example, the `Balance` class represents the balance of a wallet, including the value and assets held in a box. It can be easily created from a `TrackedBox` object using the `apply` method in its companion object:

```scala
import org.ergoplatform.nodeView.wallet.persistence.Balance
import org.ergoplatform.wallet.boxes.TrackedBox

val trackedBox: TrackedBox = // get a tracked box from somewhere
val balance: Balance = Balance(trackedBox)
println(balance.value) // prints the value of the box
println(balance.assets) // prints the assets held in the box
```

The `OffChainRegistry` class holds off-chain data in runtime memory, which is useful for obtaining wallet state in regards to unconfirmed transactions without reprocessing them on each request. It can be initialized using the `init` method of the `OffChainRegistry` object:

```scala
val walletRegistry: WalletRegistry = ...
val offChainRegistry: OffChainRegistry = OffChainRegistry.init(walletRegistry)
```

The `WalletDigest` class holds aggregate wallet data, including off-chain data, and can be serialized and deserialized using the `WalletDigestSerializer` object:

```scala
// create a new WalletDigest object
val walletDigest = WalletDigest(100, 5000000000L, Seq(("token1", 1000L), ("token2", 2000L)))

// serialize the WalletDigest object
val writer = new ByteArrayOutputStream()
WalletDigestSerializer.serialize(walletDigest, writer)
val serialized = writer.toByteArray()

// deserialize the serialized data
val reader = new ByteArrayInputStream(serialized)
val deserialized = WalletDigestSerializer.parse(reader)

// check if the deserialized object is equal to the original object
assert(deserialized == walletDigest)
```

The `WalletRegistry` class manages wallet-related data and updates the wallet state based on new blocks and transactions:

```scala
val walletRegistry = WalletRegistry(settings)
val unspentBoxes = walletRegistry.allUnspentBoxes()
val walletTransaction = walletRegistry.getTx(transactionId)
walletRegistry.updateOnBlock(scanResults, blockId, blockHeight)
```

Finally, the `WalletStorage` class persists the wallet's mutable state and provides methods to read, write, and remove data from the database:

```scala
val walletStorage = WalletStorage(settings)
walletStorage.addPublicKeys(publicKeys)
val publicKey = walletStorage.getPublicKey(derivationPath)
walletStorage.updateStateContext(stateContext)
```

In summary, the code in the `persistence` folder plays a crucial role in managing wallet-related data and persisting the wallet's mutable state in the Ergo project. It provides classes and methods for handling wallet balances, off-chain data, and wallet-specific indexes, which are essential for the wallet to function properly.
