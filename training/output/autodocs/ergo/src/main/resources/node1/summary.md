[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/resources/node1)

The `application.conf` file in the `.autodoc/docs/json/src/main/resources/node1` folder is a configuration file for a local Ergo node, primarily used for testing purposes. It contains various settings that dictate the behavior of the node, chain, wallet, and network. By modifying these settings, developers can customize the node's behavior to suit their testing needs.

For example, the `node` section contains settings related to the node view holder regime, responsible for mining blocks. By setting `offlineGeneration` to true, the node will mine its own chain and generate one block per 5 seconds until difficulty adjustment. If you want to use an external miner, you can set `useExternalMiner` to true.

```conf
node {
  offlineGeneration = true
  useExternalMiner = false
  mining = true
  internalMinerPollingInterval = 5s
}
```

In the `chain` section, the `monetary` setting specifies the miner reward delay, which is reduced to 1 block for faster testing. The `genesisStateDigestHex` setting defines the Base16 representation of the genesis state roothash.

```conf
chain {
  monetary {
    minerRewardDelay = 1
  }
  genesisStateDigestHex = "..."
}
```

The `wallet` section contains settings related to the wallet, such as the `testMnemonic` setting, which specifies the mnemonic seed used in the wallet for tests. The `testKeysQty` setting defines the number of keys to be generated for tests.

```conf
wallet {
  testMnemonic = "..."
  testKeysQty = 10
}
```

The `scorex` section contains settings related to the network, such as the `bindAddress` setting, which specifies the address and port that the node will bind to. The `nodeName` setting defines the name of the node. The `knownPeers` setting lists known peers. The `restApi` section contains settings related to the REST API, such as the `bindAddress` setting, which specifies the address and port that the API will bind to. The `apiKeyHash` setting is set to null, which means that there is no protection and anyone with access to localhost may spend your coins.

```conf
scorex {
  network {
    bindAddress = "127.0.0.1:9001"
    nodeName = "node1"
    knownPeers = []
  }
  restApi {
    bindAddress = "127.0.0.1:9052"
    apiKeyHash = null
  }
}
```

In summary, the `application.conf` file in the specified folder is a configuration file for a local Ergo node, used for testing purposes. By modifying the settings in this file, developers can customize the behavior of the node, chain, wallet, and network to suit their testing needs.
