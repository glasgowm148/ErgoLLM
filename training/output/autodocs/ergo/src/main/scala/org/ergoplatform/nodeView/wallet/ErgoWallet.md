[View code on GitHub](https://github.com/ergoplatform/ergo/src/main/scala/org/ergoplatform/nodeView/wallet/ErgoWallet.scala)

The `ErgoWallet` class is a part of the `ergo` project and is responsible for managing the wallet functionality. It provides an interface for scanning transactions and blocks, rolling back to a specific version, and getting a read-only copy of the wallet state. 

The class takes three parameters: `historyReader`, `settings`, and `parameters`. `historyReader` is an instance of `ErgoHistoryReader` which provides access to the blockchain history. `settings` is an instance of `ErgoSettings` which contains various settings for the Ergo node. `parameters` is an instance of `Parameters` which contains various parameters for the Ergo node.

The `ErgoWallet` class extends `ErgoWalletReader` which provides read-only access to the wallet state. It also extends `ScorexLogging` which provides logging functionality.

The class has a private `walletSettings` field which is an instance of `WalletSettings` and contains various settings for the wallet. It also has a `boxSelector` field which is an instance of `ReplaceCompactCollectBoxSelector`. This class is used to select boxes for spending in a transaction. It is parameterized with the maximum number of inputs a transaction could have and the optimal number of inputs. 

The class has several methods for scanning transactions and blocks. The `scanOffchain` method is used to scan off-chain transactions. It takes an instance of `ErgoTransaction` or a sequence of `ErgoTransaction`s as input and sends a `ScanOffChain` message to the `walletActor`. The `scanPersistent` method is used to scan on-chain transactions. It takes an instance of `BlockSection` or an optional sequence of `BlockSection`s as input and sends a `ScanOnChain` message to the `walletActor`. The `rollback` method is used to roll back to a specific version. It takes a `VersionTag` as input and sends a `Rollback` message to the `walletActor`. 

The `ErgoWallet` object provides a `readOrGenerate` method which is used to create an instance of `ErgoWallet`. It takes the same parameters as the `ErgoWallet` constructor and returns a new instance of `ErgoWallet`.

Overall, the `ErgoWallet` class provides an interface for managing the wallet functionality in the `ergo` project. It allows for scanning transactions and blocks, rolling back to a specific version, and getting a read-only copy of the wallet state. The `boxSelector` field is used to select boxes for spending in a transaction.
## Questions: 
 1. What is the purpose of the `ErgoWallet` class and what dependencies does it have?
- The `ErgoWallet` class is a wallet implementation for the Ergo blockchain. It depends on `ErgoHistoryReader`, `ErgoSettings`, `Parameters`, and `ActorSystem`.

2. What is the `boxSelector` field and how is it used?
- The `boxSelector` field is an instance of `ReplaceCompactCollectBoxSelector` that is used to select boxes for spending in a transaction. It is parameterized with the maximum number of inputs a transaction could have and the optimal number of inputs.

3. What is the purpose of the `scanOffchain` and `scanPersistent` methods?
- The `scanOffchain` method is used to scan off-chain transactions and update the wallet state accordingly. The `scanPersistent` method is used to scan on-chain transactions and update the wallet state accordingly.