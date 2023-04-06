[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/ergo-wallet/src/main/scala/org/ergoplatform/contracts)

The `ReemissionContracts.scala` file in the `org.ergoplatform.contracts` package is a crucial component of the Ergo platform, as it provides the necessary contracts for re-emission rewards. These contracts incentivize miners and promote network security, which is essential for the overall stability and growth of the Ergo ecosystem.

The file contains the `ReemissionContracts` trait, which acts as a container for two re-emission related contracts: `payToReemission` and `reemissionBoxProp`. The `payToReemission` contract is used to lock boxes that miners pay to the re-emission contract according to EIP-27. The `reemissionBoxProp` contract is used to lock boxes that contain re-emission rewards.

The trait also includes several helper methods and variables, such as `reemissionRewardPerBlock`, `reemissionNftIdBytes`, `reemissionStartHeight`, `extractTokens`, and `v1Tree`. These methods and variables are used to facilitate the implementation of the re-emission contracts and ensure their proper functioning.

The `payToReemission` contract is used to merge multiple boxes locked by this contract with the re-emission box. It is locked by a script that checks that the first (re-emission) output contains the re-emission NFT (in the first position). This contract ensures that the re-emission rewards are correctly distributed to miners.

The `reemissionBoxProp` contract is used to lock boxes that contain re-emission rewards. It is locked by a script that checks various conditions, such as the presence of the re-emission NFT, the miner's output script, the re-emission output's height, and the miner's reward condition. This contract ensures that the re-emission rewards are securely locked and can only be accessed by miners who meet the specified conditions.

In the larger Ergo project, these contracts can be used to implement the re-emission rewards mechanism, which is an essential part of the platform's incentive structure. For example, a developer might use the `ReemissionContracts` trait to create a new re-emission contract for a specific mining pool or to update the re-emission reward per block.

Here's a code example of how the `ReemissionContracts` trait might be used:

```scala
import org.ergoplatform.contracts.ReemissionContracts

object MyReemissionContract extends ReemissionContracts {
  // Customize re-emission reward per block
  override val reemissionRewardPerBlock: Long = 1000000

  // Create a new payToReemission contract
  val myPayToReemissionContract = payToReemission

  // Create a new reemissionBoxProp contract
  val myReemissionBoxPropContract = reemissionBoxProp
}
```

In summary, the `ReemissionContracts.scala` file provides the necessary contracts and helper methods for implementing re-emission rewards in the Ergo platform. These contracts play a vital role in incentivizing miners and promoting network security, making them an essential component of the Ergo ecosystem.
