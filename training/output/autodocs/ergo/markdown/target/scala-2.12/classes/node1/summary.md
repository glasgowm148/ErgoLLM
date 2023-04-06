[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/target/scala-2.12/classes/node1)

The `application.conf` file in the Ergo project serves as a configuration file for setting up a local node, primarily for testing purposes. It contains several sections, each responsible for configuring different aspects of the node, chain, wallet, and Scorex framework.

In the `ergo` section, the node's data directory is specified, along with the node view holder regime, which determines the mining behavior. For example, the node is set to mine its own chain and mine one block every 5 seconds until difficulty adjustment. The `offlineGeneration` parameter ensures that the node will not broadcast its blocks to the network, while the `useExternalMiner` parameter indicates that the node will use its internal miner for mining blocks. The `internalMinerPollingInterval` parameter sets the frequency at which the node checks for new blocks to mine.

```conf
ergo {
  directory = ...
  nodeViewHolder {
    ...
    offlineGeneration = true
    useExternalMiner = false
    internalMinerPollingInterval = 5s
  }
}
```

The `chain` section configures the monetary policy and the genesis state digest. The `minerRewardDelay` parameter sets the number of block confirmations required before a mining reward is available. The `genesisStateDigestHex` parameter specifies the base16 representation of the genesis state roothash.

```conf
chain {
  ...
  minerRewardDelay = 1
  genesisStateDigestHex = ...
}
```

The `wallet` section sets the wallet parameters, such as the mnemonic seed used for tests and the number of keys to be generated for tests.

```conf
wallet {
  ...
  mnemonic = ...
  testKeys = ...
}
```

The `scorex` section configures the Scorex framework, which is used by the Ergo project. It sets the network parameters, including the bind address, node name, and known peers. It also configures the REST API parameters, such as the bind address and API key hash.

```conf
scorex {
  network {
    ...
    bindAddress = ...
    nodeName = ...
    knownPeers = ...
  }
  restApi {
    ...
    bindAddress = ...
    apiKeyHash = ...
  }
}
```

By adjusting the parameters in the `application.conf` file, developers can test different scenarios and configurations to ensure that the Ergo project is functioning as intended. For example, changing the `minerRewardDelay` parameter can help test how the node behaves with different reward delays, while modifying the `genesisStateDigestHex` parameter can help test the node's behavior with different genesis state digests.
