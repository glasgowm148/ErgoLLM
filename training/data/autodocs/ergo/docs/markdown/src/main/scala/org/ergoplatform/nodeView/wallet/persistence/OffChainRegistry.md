[View code on GitHub](https://github.com/ergoplatform/ergo/src/main/scala/org/ergoplatform/nodeView/wallet/persistence/OffChainRegistry.scala)

The `OffChainRegistry` class is responsible for holding version-agnostic off-chain data in runtime memory. This data includes off-chain boxes, which are needed to obtain wallet state in regards to unconfirmed transactions without reprocessing them on each request. The class takes three parameters: `height`, which is the latest processed block height; `offChainBoxes`, which are boxes from off-chain transactions; and `onChainBalances`, which is an on-chain balances snapshot required to calculate off-chain indexes. 

The `OffChainRegistry` class has three methods. The first method, `digest`, calculates the off-chain index considering on-chain balances. It does this by summing the values of the off-chain balances and on-chain balances and then creating a map of the assets. The second method, `updateOnTransaction`, updates the registry on receiving a new off-chain transaction. It does this by filtering out spent boxes and adding new boxes. The third method, `updateOnBlock`, updates the balances snapshot according to a new block applied. It does this by filtering out on-chain boxes and updating the on-chain balances.

The `OffChainRegistry` class is used in the larger project to hold off-chain data in memory. This is useful for obtaining wallet state in regards to unconfirmed transactions without reprocessing them on each request. The class can be initialized using the `init` method of the `OffChainRegistry` object. This method takes a `walletRegistry` parameter and returns an `OffChainRegistry` object. 

Example usage:

```
val walletRegistry: WalletRegistry = ...
val offChainRegistry: OffChainRegistry = OffChainRegistry.init(walletRegistry)
```
## Questions: 
 1. What is the purpose of the `OffChainRegistry` class?
- The `OffChainRegistry` class holds off-chain data in runtime memory, which is needed to obtain wallet state in regards to unconfirmed transactions without reprocessing them on each request.

2. What is the `digest` property of the `OffChainRegistry` class?
- The `digest` property is an off-chain index considering on-chain balances, which is calculated based on the off-chain boxes and on-chain balances snapshot.

3. What is the purpose of the `updateOnBlock` method in the `OffChainRegistry` class?
- The `updateOnBlock` method updates the balances snapshot according to a new block applied, by filtering out the on-chain boxes and updating the off-chain boxes and on-chain balances snapshot.