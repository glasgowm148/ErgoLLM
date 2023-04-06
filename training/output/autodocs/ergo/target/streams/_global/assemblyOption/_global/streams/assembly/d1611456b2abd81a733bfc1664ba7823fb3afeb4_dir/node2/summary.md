[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/target/streams/_global/assemblyOption/_global/streams/assembly/d1611456b2abd81a733bfc1664ba7823fb3afeb4_dir/node2)

The `application.conf` file is a configuration file for setting up a local node in the Ergo project, primarily for testing purposes. It contains two main sections: `ergo` and `scorex`, which define settings related to the node, wallet, chain, network, and REST API.

In the `ergo` section, the `directory` setting specifies the directory where the node data will be stored. The `node` settings define the mining behavior of the node, such as mining its own chain and the block generation interval. The `wallet` settings configure the mnemonic seed and the number of keys generated for testing. The `chain` settings determine the miner reward delay and the genesis state digest hex.

The `scorex` section configures the network and REST API settings. The `bindAddress` setting defines the IP address and port number for the network and REST API. The `nodeName` setting provides a name for the node, while the `knownPeers` setting lists the IP addresses and port numbers of known peers. The `apiKeyHash` setting sets the API key hash for the REST API.

This configuration file is essential for setting up a local node for testing purposes in the Ergo project. Developers can modify the settings to suit specific testing requirements and scenarios. For example, to prevent the node from mining its own chain, set the `offlineGeneration` setting to `true`. To generate more keys for testing, increase the `testKeysQty` setting. To change the IP address and port number for the network and REST API, modify the `bindAddress` setting.

Here's an example of how to modify the `bindAddress` setting:

```conf
scorex {
  network {
    bindAddress = "127.0.0.1:9001"
  }
  restApi {
    bindAddress = "127.0.0.1:9002"
  }
}
```

In summary, the `application.conf` file is a crucial component of the Ergo project, allowing developers to set up and configure a local node for testing purposes. By adjusting the settings in this file, developers can test various scenarios and ensure the node functions as expected within the larger project.
