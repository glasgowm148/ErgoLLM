[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/target/streams/_global/assemblyOption/_global/streams/assembly/d1611456b2abd81a733bfc1664ba7823fb3afeb4_dir/samples)

The `local.conf.sample` file in the `samples` folder is a configuration file for the Ergo project, which allows users to customize various settings related to the node, wallet, network, and REST API. This file is essential for users to tailor the Ergo project to their specific needs and preferences.

The configuration file is divided into three main blocks: `ergo`, `wallet`, and `scorex`. The `ergo` block contains settings related to the node, such as the state type (either "utxo" or "digest"), whether the node is doing mining, and whether to use an external miner. It also allows the user to specify a public key for mining rewards. The `wallet` block contains settings related to the wallet, such as the language to be used in the mnemonic seed and whether to keep spent boxes or delete them immediately.

The `scorex` block contains settings related to the network and REST API. The `network` block allows the user to specify a node name to send during handshake, a list of well-known nodes, and the network address to bind to. The `restApi` block allows the user to specify the network address to bind to and an API key hash for authentication purposes.

To use this configuration file, users can uncomment the desired settings and modify them as needed. For example, to specify that the node should use the "digest" state type and the wallet should keep spent boxes, the user can uncomment the following lines:

```plaintext
# stateType = "digest"
# keepSpentBoxes = true
```

To specify a node name and a list of well-known nodes, the user can uncomment the following lines and fill in the appropriate values:

```plaintext
# nodeName = "my-node"
# knownPeers = ["IP1:port1", "IP2:port2"]
```

In the larger project, this configuration file serves as a way for users to customize the behavior of the Ergo node, wallet, and network settings. By providing a sample configuration file, the Ergo project makes it easier for users to understand the available options and modify them according to their requirements. This file is an essential part of the Ergo project, as it allows users to tailor the software to their specific needs and preferences, ensuring a smooth and efficient experience.
