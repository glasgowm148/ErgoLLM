[View code on GitHub](https://github.com/ergoplatform/ergo/src/it/scala/org/ergoplatform/it/StateRecoveryDigestNodeSpec.scala)

The `StateRecoveryDigestNodeSpec` class is a test suite that verifies the state recovery functionality of the Ergo blockchain platform. The test suite is a part of the `ergo` project and is located in the `org.ergoplatform.it` package. The test suite extends the `AnyFlatSpec` class and uses the `IntegrationSuite` trait to provide a set of helper methods for testing Ergo nodes.

The `StateRecoveryDigestNodeSpec` test suite defines a set of constants that are used to configure the test scenario. These constants include the target height for the miner node, the target height for the follower node, the local volumes for the miner and follower nodes, and the remote volume for the Docker container. The test scenario involves the following steps:

1. Start up one node and let it mine {approxMinerTargetHeight} blocks;
2. Shut it down and copy its history to testing node's directory;
3. Start mining node again;
4. Start testing node and wait until it gets synced with the mining node + {approxFollowerTargetHeight}
   - it would require testing node to recover state correctly and apply new blocks on top of it;

The test scenario is implemented in the `it should "Startup with only history available" in` test case. The test case starts a miner node using the `docker.startDevNetNode` method and waits for it to reach the target height using the `waitForHeight` method. Once the miner node reaches the target height, the test case stops the miner node using the `docker.stopNode` method and copies its history to the follower node's directory using the `FileUtils.copyDirectoryToDirectory` method. The test case then starts a new miner node and waits for it to reach the target height plus two blocks. Finally, the test case starts a follower node and waits for it to reach the target height plus five blocks.

The `StateRecoveryDigestNodeSpec` test suite is an important part of the `ergo` project as it verifies the state recovery functionality of the Ergo blockchain platform. The test suite ensures that the platform can recover from a failure and continue to operate correctly. Developers can use the test suite to verify the correctness of their implementation and ensure that it meets the requirements of the Ergo platform.
## Questions: 
 1. What is the purpose of the `StateRecoveryDigestNodeSpec` class?
- The `StateRecoveryDigestNodeSpec` class is a test suite that tests the state recovery and syncing functionality of two nodes in the `ergo` project.

2. What is the significance of the `approxMinerTargetHeight` and `approxFollowerTargetHeight` variables?
- The `approxMinerTargetHeight` and `approxFollowerTargetHeight` variables are used to set the target heights for the miner and follower nodes respectively. The follower node waits until it has synced with the miner node up to `approxFollowerTargetHeight` blocks.

3. What is the purpose of the `Async.async` and `Async.await` calls in the `it should "Startup with only history available"` test case?
- The `Async.async` and `Async.await` calls are used to perform asynchronous operations in the test case. The `Async.async` method creates a new asynchronous block, and the `Async.await` method suspends the execution of the block until the asynchronous operation completes.