[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/target/scala-2.12/classes/node2)

The `application.conf` file in the `node2` folder is a configuration file for setting up a local node in the Ergo project, specifically for testing purposes. It contains various settings related to the node, wallet, chain, and Scorex framework, which can be modified to suit the needs of the project.

For example, the `node` section contains settings related to the node view holder regime, responsible for processing transactions and blocks. The `offlineGeneration` setting is set to false, meaning the node will not generate blocks while offline. The `mining` setting is set to true, meaning the node will mine blocks. The `useExternalMiner` setting is set to false, meaning the node will use its internal miner.

```conf
node {
  offlineGeneration = false
  mining = true
  useExternalMiner = false
  internalMinerPollingInterval = 10s
}
```

The `wallet` section contains settings related to the wallet used for testing. The `testMnemonic` setting specifies the mnemonic seed used in the wallet for tests. The `testKeysQty` setting specifies the number of keys to be generated for tests.

```conf
wallet {
  testMnemonic = "..."
  testKeysQty = 10
}
```

The `chain` section contains settings related to the chain. The `monetary` section contains settings related to the monetary policy of the chain. The `minerRewardDelay` setting is reduced to 1 block reward delay for faster testing. The `genesisStateDigestHex` setting specifies the Base16 representation of the genesis state roothash.

```conf
chain {
  monetary {
    minerRewardDelay = 1
  }
  genesisStateDigestHex = "..."
}
```

The `scorex` section contains settings related to the Scorex framework used in the Ergo project. The `network` section contains settings related to the network. The `bindAddress` setting specifies the address and port where the node will bind to. The `nodeName` setting specifies the name of the node. The `knownPeers` setting specifies the list of known peers.

```conf
scorex {
  network {
    bindAddress = "127.0.0.1:9002"
    nodeName = "node2"
    knownPeers = []
  }
}
```

The `restApi` section contains settings related to the REST API. The `bindAddress` setting specifies the address and port where the API will bind to. The `apiKeyHash` setting is set to null, meaning there is no protection for the API.

```conf
restApi {
  bindAddress = "127.0.0.1:9052"
  apiKeyHash = null
}
```

In summary, the `application.conf` file in the `node2` folder is crucial for setting up a local node for testing purposes in the Ergo project. It allows developers to configure various settings related to the node, wallet, chain, and Scorex framework, ensuring a smooth testing environment.
