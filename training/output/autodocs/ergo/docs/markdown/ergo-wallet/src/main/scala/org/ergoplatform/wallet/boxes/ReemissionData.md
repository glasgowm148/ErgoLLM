[View code on GitHub](https://github.com/ergoplatform/ergo/ergo-wallet/src/main/scala/org/ergoplatform/wallet/boxes/ReemissionData.scala)

The `ReemissionData` class in the `org.ergoplatform.wallet.boxes` package is used to store re-emission settings needed to construct transactions in the Ergo platform. Re-emission refers to the process of creating a new token from an existing one, which can be useful for various purposes such as incentivizing certain behaviors or creating new assets.

The `ReemissionData` class has two fields: `reemissionNftId` and `reemissionTokenId`, both of type `ModifierId`. These fields represent the IDs of the NFT (non-fungible token) and token that will be used for re-emission. 

This class is useful for constructing transactions that involve re-emission, as it provides the necessary information to create new tokens. However, it should be noted that this class does not have all the data needed to obtain a re-emission contract. If a re-emission contract is needed, it must be provided from outside the class.

Here is an example of how this class might be used in a larger project:

```scala
import org.ergoplatform.wallet.boxes.ReemissionData
import scorex.util.ModifierId

val nftId: ModifierId = ModifierId("nft123")
val tokenId: ModifierId = ModifierId("token456")
val reemissionData = ReemissionData(nftId, tokenId)

// Use reemissionData to construct a transaction involving re-emission
```

In this example, we create a new `ReemissionData` object with the IDs of the NFT and token that will be used for re-emission. This object can then be used to construct a transaction that involves re-emission.
## Questions: 
 1. What is the purpose of the `ReemissionData` case class?
   - The `ReemissionData` case class is used to store re-emission settings needed to construct transactions, except for ones using re-emission contract.

2. What are `reemissionNftId` and `reemissionTokenId`?
   - `reemissionNftId` and `reemissionTokenId` are both instances of `ModifierId` and represent the IDs of the re-emission NFT and token, respectively.

3. Can this class be used for transactions using re-emission contract?
   - No, this class does not have all the needed data to obtain re-emission contract. However, it is possible to use re-emission contracts in apps using Ergo Wallet API by providing re-emission contract from outside.