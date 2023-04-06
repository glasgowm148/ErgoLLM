[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/resources/node2)

The `application.conf` file in the `.autodoc/docs/json/src/main/resources/node2` folder is a configuration file for setting up a local node in the Ergo project for testing purposes. It contains various settings related to the node, wallet, chain, network, and REST API, which can be modified to suit the needs of the project.

For example, the `node` section contains settings related to the node's mining behavior. By default, the `mining` setting is set to true, which means that the node is actively mining blocks. If you want to disable mining, you can set this value to false:

```conf
node {
  mining = false
}
```

The `wallet` section contains settings related to the wallet used for testing. The `testMnemonic` setting specifies the mnemonic seed used in the wallet for tests. If you want to use a different mnemonic seed, you can update this value:

```conf
wallet {
  testMnemonic = "your mnemonic seed here"
}
```

The `chain` section contains settings related to the chain. The `monetary` section contains settings related to the monetary policy of the chain. If you want to change the miner reward delay, you can update the `minerRewardDelay` setting:

```conf
chain {
  monetary {
    minerRewardDelay = 10
  }
}
```

The `scorex` section contains settings related to the network and REST API. The `bindAddress` setting specifies the IP address and port number where the node will bind to. If you want to change the bind address, you can update this value:

```conf
scorex {
  bindAddress = "0.0.0.0:9001"
}
```

The `restApi` section contains settings related to the REST API. The `bindAddress` setting specifies the IP address and port number where the API will bind to. If you want to change the API bind address, you can update this value:

```conf
scorex {
  restApi {
    bindAddress = "0.0.0.0:9002"
  }
}
```

In summary, the `application.conf` file in the `.autodoc/docs/json/src/main/resources/node2` folder is a configuration file that sets up a local node for testing purposes in the Ergo project. It contains various settings that can be modified to suit the needs of the project, such as node mining behavior, wallet settings, chain settings, network settings, and REST API settings. By modifying these settings, developers can customize the behavior of the local node for their specific testing requirements.
