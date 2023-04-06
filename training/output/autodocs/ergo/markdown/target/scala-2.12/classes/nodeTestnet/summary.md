[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/target/scala-2.12/classes/nodeTestnet)

The `application.conf` file in the `nodeTestnet` folder is a configuration file for the Ergo blockchain platform, specifically for setting up a testnet node. Ergo is a platform that enables the creation of decentralized applications, and this configuration file allows users to customize various parameters for the Ergo node, wallet, and Scorex network.

For instance, the `directory` parameter sets the directory where the node will store its data, while the `mining` parameter specifies whether the node will participate in mining new blocks. The `keepSpentBoxes` parameter determines if the wallet will keep spent boxes or delete them immediately. For testing purposes, the `testMnemonic` parameter sets the mnemonic seed used in the wallet, and the `testKeysQty` parameter sets the number of keys to be generated.

In the Scorex network section, the `nodeName` parameter sets the name of the node, and the `bindAddress` parameter specifies the address and port where the REST API will be available. The `apiKeyHash` parameter is a Base16-encoded Blake2b hash from the user's secret, which should be passed in headers as `api_key`. If this parameter is set to `null`, anyone can access the wallet.

This configuration file is essential for customizing the behavior of the Ergo node and wallet. For example, if a user wants to run a node that participates in mining, they can set `mining` to `true`. If the user wants to generate a specific number of keys for testing, they can set `testKeysQty` to the desired value.

Here's an example of how to modify the `application.conf` file to enable mining and generate 10 keys for testing:

```conf
ergo {
  directory = "./nodeTestnet/data"
  mining = true
  wallet {
    keepSpentBoxes = false
    testMnemonic = "edge talent poet tortoise trumpet dose"
    testKeysQty = 10
  }
}

scorex {
  network {
    nodeName = "Ergo Testnet Node"
    bindAddress = "0.0.0.0:9052"
  }
  restApi {
    apiKeyHash = "null"
  }
}
```

In summary, the `application.conf` file in the `nodeTestnet` folder is a crucial component of the Ergo project, as it allows users to customize the behavior of the Ergo node and wallet to suit their needs. This configuration file is particularly useful for setting up a testnet node and adjusting various parameters for testing and development purposes.
