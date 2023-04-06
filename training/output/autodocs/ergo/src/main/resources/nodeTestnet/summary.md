[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/resources/nodeTestnet)

The `application.conf` file in the `nodeTestnet` folder is a configuration file for the Ergo project, which is a blockchain platform for building decentralized applications (dApps) and smart contracts. This file sets up various parameters for the Ergo node, wallet, and Scorex network, allowing developers to customize the behavior of the Ergo node and wallet to suit their specific needs.

For instance, the `directory` parameter specifies the directory where the node will store its data. Developers can modify this parameter to change the storage location. The `mining` parameter is a boolean that determines whether the node will participate in mining new blocks. If a developer doesn't want their node to mine, they can set this parameter to `false`.

The `keepSpentBoxes` parameter is a boolean that determines whether the wallet will keep spent boxes or delete them immediately. This can be useful for optimizing storage space. The `testMnemonic` parameter is a string that sets the mnemonic seed used in the wallet for testing purposes, while the `testKeysQty` parameter is an integer that sets the number of keys to be generated for testing.

In the `scorex` section, the `nodeName` parameter sets the name of the node in the Scorex network. This can be useful for identifying nodes in a network. The `bindAddress` parameter in the `restApi` section sets the address where the REST API will be available. Developers can set this parameter to a public IP address to make the REST API available from remote hosts.

The `apiKeyHash` parameter is a Base16-encoded Blake2b hash that should be passed in headers as `api_key` to access the wallet. If this parameter is set to `null`, anyone can access the wallet. This can be useful for testing purposes but should be set to a secure value in production environments.

Here's an example of how to modify the `mining` and `bindAddress` parameters:

```conf
ergo {
  directory = "/path/to/custom/directory"
  mining = false
  ...
}

scorex {
  ...
  restApi {
    bindAddress = "0.0.0.0:9052"
    ...
  }
}
```

In summary, the `application.conf` file in the `nodeTestnet` folder is an essential part of the Ergo project, as it allows developers to customize the behavior of the Ergo node and wallet according to their specific use cases. By modifying the parameters in this file, developers can optimize the node's performance, storage, and network settings to better suit their needs.
