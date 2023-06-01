[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/target/streams/_global/assemblyOption/_global/streams/assembly/d1611456b2abd81a733bfc1664ba7823fb3afeb4_dir/nodeTestnet)

The `application.conf` file in the Ergo project serves as a configuration file for setting up various parameters related to the Ergo node, wallet, and REST API. By customizing these parameters, developers can deploy their own instances of the Ergo platform and build decentralized applications.

For instance, to set up a node for mining and use the wallet to manage funds, the following code can be used:

```conf
ergo {
  directory = "/home/user/ergo/data"
  node {
    mining = true
  }
  wallet {
    keepSpentBoxes = true
  }
}

scorex {
  network {
    nodeName = "my-ergo-node"
  }
  restApi {
    bindAddress = "0.0.0.0:9052"
    apiKeyHash = "my-unique-hash"
  }
}
```

In this example, the `directory` parameter sets the directory where the node will store its data. The `mining` parameter is set to `true` to enable mining. The `keepSpentBoxes` parameter is set to `true` to keep spent boxes in the wallet. The `nodeName` parameter sets the name of the node for the network. The `bindAddress` parameter is set to `0.0.0.0:9052` to make the REST API available from remote hosts. The `apiKeyHash` parameter is set to a unique hash to restrict access to the wallet.

The `application.conf` file allows developers to:

- Configure the data storage directory for the Ergo node.
- Enable or disable mining on the node.
- Choose whether to keep or delete spent boxes in the wallet.
- Set a mnemonic seed for testing purposes.
- Set the number of keys to be generated for testing.
- Set the node name for the network.
- Configure the REST API's bind address and access restrictions.

By modifying these parameters, developers can tailor the Ergo node, wallet, and REST API to their specific needs, enabling them to build and deploy decentralized applications on the Ergo platform.
