[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/target/scala-2.12/classes/samples)

The `local.conf.sample` file in the Ergo project serves as a template for users to customize various settings related to the Ergo node, wallet, and the underlying Scorex framework. By uncommenting and modifying the appropriate settings, users can tailor the Ergo project to their specific needs.

The configuration file is divided into two main sections: `ergo` and `scorex`.

### Ergo Section

The `ergo` section contains settings related to the Ergo node and wallet.

#### Node Subsection

The `node` subsection allows the user to specify the type of state to be kept by the node. The two options are `utxo` and `digest`. If `utxo` is selected, the node will keep the full UTXO set, which allows for the validation of arbitrary blocks and the generation of ADProofs. If `digest` is selected, the node will only keep the state root hash and validate transactions via ADProofs.

Example:

```conf
ergo {
  node {
    stateType = "utxo"
  }
}
```

#### Mining Settings

The `mining` and `useExternalMiner` settings allow the user to specify whether the node is doing mining and whether an external miner is being used. The `miningPubKeyHex` setting allows the user to specify the public key to which mining rewards will be dedicated.

Example:

```conf
ergo {
  mining = true
  useExternalMiner = false
  miningPubKeyHex = "your_public_key_here"
}
```

#### Wallet Subsection

The `wallet` subsection contains settings related to the Ergo wallet. The `mnemonicPhraseLanguage` setting allows the user to specify the language to be used in the mnemonic seed. The `keepSpentBoxes` setting allows the user to specify whether used boxes should be saved or deleted immediately.

Example:

```conf
ergo {
  wallet {
    mnemonicPhraseLanguage = "english"
    keepSpentBoxes = true
  }
}
```

### Scorex Section

The `scorex` section contains settings related to the Scorex framework, which is used by the Ergo project.

#### Network Subsection

The `network` subsection allows the user to specify the node name to be sent during handshake, a list of well-known nodes, and the network address to bind to.

Example:

```conf
scorex {
  network {
    nodeName = "your_node_name_here"
    knownPeers = ["peer1", "peer2"]
    bindAddress = "0.0.0.0:9001"
  }
}
```

#### RestApi Subsection

The `restApi` subsection allows the user to specify the network address to bind to and an API key hash.

Example:

```conf
scorex {
  restApi {
    bindAddress = "0.0.0.0:9052"
    apiKeyHash = "your_api_key_hash_here"
  }
}
```

By customizing the settings in the `local.conf.sample` file, users can configure the Ergo node and wallet to suit their requirements, such as specifying the type of state to be kept by the node, the language to be used in the mnemonic seed, and the network address to bind to.
