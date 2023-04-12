[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/it/scala/org/ergoplatform/it)

The code in the `.autodoc/docs/json/src/it/scala/org/ergoplatform/it` folder focuses on integration testing for the Ergo blockchain platform. It contains test suites that verify various aspects of the platform, such as node synchronization, wallet functionality, and state recovery. The test suites use the `IntegrationSuite` trait, which provides a Docker-based environment for running the tests and utility methods for managing nodes and interacting with the Ergo blockchain network.

For example, the `DeepRollBackSpec.scala` test suite checks the ability of the Ergo blockchain to handle deep rollbacks and reconcile after a fork. It simulates a scenario where two nodes in the network have different blockchain histories due to a fork and verifies that the nodes can switch to the longer chain.

The `ForkResolutionSpec.scala` test suite verifies the fork resolution mechanism of the Ergo blockchain by simulating a fork scenario and verifying that the nodes reach consensus on the correct chain.

The `KnownNodesSpec.scala` test suite ensures that the nodes in the Ergo blockchain network can communicate with each other and that the network is functioning correctly.

The `LongChainSyncSpec.scala` test suite tests the synchronization of a long chain of blocks between two nodes in the Ergo blockchain network, ensuring that the nodes are able to synchronize with each other.

The `NodeRecoverySpec.scala` test suite verifies that a node can recover after an unexpected shutdown and maintain a consistent state.

The `OpenApiSpec.scala` test suite checks whether the OpenAPI specification of the Ergo node's API is correct, ensuring that the Ergo node's API conforms to the OpenAPI specification for interoperability with other systems.

The `PrunedDigestNodeSyncSpec.scala` and `PrunedDigestNodeSync2Spec.scala` test suites verify the synchronization of a pruned digest node with a mining node, ensuring that the digest node can synchronize up to a certain height without loading full blocks that should be pruned.

The `StateRecoveryDigestNodeSpec.scala` test suite verifies the state recovery functionality of the Ergo blockchain platform, ensuring that the platform can recover from a failure and continue to operate correctly.

The `UtxoStateNodesSyncSpec.scala` test suite checks the synchronization of UTXO state nodes in the Ergo platform, ensuring that the UTXO state is consistent across all nodes.

These test suites are crucial for ensuring the correct functioning of the Ergo blockchain platform and can be run as part of the project's continuous integration process to ensure that changes to the codebase do not break the platform.
