[View code on GitHub](https://github.com/ergoplatform/ergo/src/main/scala/org/ergoplatform/nodeView/history/storage/modifierprocessors/FullBlockPruningProcessor.scala)

The `FullBlockPruningProcessor` class is responsible for keeping track of the minimal height for full blocks that need to be downloaded from the network and stored in the history of the Ergo platform. This class is part of the `org.ergoplatform.nodeView.history.storage.modifierprocessors` package.

The class takes two parameters in its constructor: `nodeConfig` and `chainSettings`. These parameters are instances of `NodeConfigurationSettings` and `ChainSettings` respectively. The `NodeConfigurationSettings` class contains various settings related to the node configuration, while the `ChainSettings` class contains settings related to the blockchain.

The class has two private variables: `isHeadersChainSyncedVar` and `minimalFullBlockHeightVar`. The former is a boolean variable that indicates whether the headers chain is synchronized with the network, while the latter is an integer variable that stores the minimal height for full blocks that need to be downloaded.

The class has four public methods: `isHeadersChainSynced`, `minimalFullBlockHeight`, `shouldDownloadBlockAtHeight`, and `updateBestFullBlock`.

The `isHeadersChainSynced` method returns the value of the `isHeadersChainSyncedVar` variable.

The `minimalFullBlockHeight` method returns the value of the `minimalFullBlockHeightVar` variable.

The `shouldDownloadBlockAtHeight` method takes an integer parameter `height` and returns a boolean value indicating whether the headers chain is synchronized with the network and whether the modifier is not too old.

The `updateBestFullBlock` method takes a `Header` parameter and updates the `minimalFullBlockHeightVar` variable. If `nodeConfig.isFullBlocksPruned` is false, then all blocks are kept in history. If `isHeadersChainSynced` and `nodeConfig.stateType.requireProofs` are false, then the method starts with the height of the UTXO snapshot applied. Otherwise, the method starts from `config.blocksToKeep` blocks back, but not later than the beginning of a voting epoch.

Overall, the `FullBlockPruningProcessor` class is an important part of the Ergo platform's history storage and is responsible for keeping track of the minimal height for full blocks that need to be downloaded and stored in the history. It provides methods to check whether the headers chain is synchronized with the network and whether a block should be downloaded at a certain height.
## Questions: 
 1. What is the purpose of this class?
- This class keeps track of the minimal height for full blocks that need to be downloaded from the network and stored in the history.

2. What is the significance of the `VotingEpochLength` variable?
- The `VotingEpochLength` variable is used to calculate the extension height for a given height, which is used to determine the minimal full block height to download.

3. What is the logic behind updating the `minimalFullBlockHeightVar` variable in the `updateBestFullBlock` method?
- The `minimalFullBlockHeightVar` variable is updated based on whether full blocks are pruned, whether the headers chain is synced with the network, and the number of blocks to keep. The updated value is returned as the minimal height to process the best full block.