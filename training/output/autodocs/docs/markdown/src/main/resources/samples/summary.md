[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/resources/samples)

The `local.conf.sample` file in the `samples` folder is a configuration file for the Ergo project, providing users with the ability to customize the behavior of the Ergo node and wallet. This file contains settings that can be uncommented and modified to overwrite default values. It is divided into three main sections: `ergo`, `wallet`, and `scorex`.

The `ergo` section contains settings related to the Ergo node, such as:

- The type of state to keep (`utxo` or `digest`)
- Whether the node is doing mining (`mining`)
- Whether to use an external miner (`useExternalMiner`)
- Specifying a public key for mining rewards (`miningPubKeyHex`)

For example, to enable mining, a user could uncomment the `mining` setting and set it to `true`.

The `wallet` section contains settings related to the Ergo wallet, such as:

- The language to be used in the mnemonic seed (`mnemonicSeedLanguage`)
- Whether to keep spent boxes or delete them immediately (`keepSpentBoxes`)

The `scorex` section contains settings related to the Scorex framework, which is used by Ergo. It allows users to:

- Specify the node name to send during handshake (`nodeName`)
- Provide a list of well-known nodes (`knownPeers`)
- Specify the network address to bind to (`bindAddress`)
- Specify the network address for the REST API (`apiAddress`)
- Provide an API key hash (`apiKeyHash`)

For example, a user could change the network address for the REST API by modifying the `apiAddress` setting.

Overall, this configuration file enables users to customize the behavior of the Ergo node and wallet to suit their needs. By modifying the settings in this file, users can configure their Ergo node to perform specific tasks, such as mining or connecting to specific peers. This file is an essential part of the Ergo project, as it allows for easy customization and configuration of the Ergo node and wallet.

Here's an example of how to enable mining and set a custom mining public key:

```conf
ergo {
  # Uncomment the line below to enable mining
  mining = true

  # Set your custom mining public key
  miningPubKeyHex = "your_public_key_here"
}
```

And here's an example of how to change the REST API network address:

```conf
scorex {
  restApi {
    # Set a custom network address for the REST API
    bindAddress = "0.0.0.0:9053"
  }
}
```
