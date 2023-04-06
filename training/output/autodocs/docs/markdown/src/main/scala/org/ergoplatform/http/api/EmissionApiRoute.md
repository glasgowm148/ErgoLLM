[View code on GitHub](https://github.com/ergoplatform/ergo/src/main/scala/org/ergoplatform/http/api/EmissionApiRoute.scala)

The `EmissionApiRoute` class is an API route for the Ergo blockchain that provides information about the emission of new coins. The class extends the `ErgoBaseApiRoute` class and takes an `ErgoSettings` object as a parameter. It defines two API methods: `emissionAt` and `scripts`.

The `emissionAt` method takes an integer parameter `height` and returns an `ApiResponse` containing information about the emission at the given height. This information is obtained by calling the `emissionInfoAtHeight` method, which takes the height, an `EmissionRules` object, and a `ReemissionSettings` object as parameters. The `emissionInfoAtHeight` method calculates the miner reward, total coins issued, total remaining coins, and re-emission amount for the given height using the `EmissionRules` and `ReemissionSettings` objects.

The `scripts` method returns an `ApiResponse` containing information about the emission and re-emission related scripts as P2S addresses. The `Pay2SAddress` method is used to convert the scripts to P2S addresses.

The `EmissionApiRoute` object defines a `EmissionInfo` case class and an `encoder` for this class. The `EmissionInfo` case class is a data container for the `emissionAt` API request output. It contains emission info for a block at a given height, including the height, miner reward, total coins issued, total remaining coins, and re-emission amount. The `encoder` is used to encode the `EmissionInfo` object as a JSON object.

Overall, this class provides a way to retrieve information about the emission of new coins on the Ergo blockchain. It can be used by clients to monitor the emission of new coins and to calculate the miner reward for a given height.
## Questions: 
 1. What is the purpose of the `EmissionApiRoute` class?
- The `EmissionApiRoute` class is an API route that displays emission and re-emission related information for the Ergo blockchain.

2. What is the `emissionAt` method used for?
- The `emissionAt` method is an API method that displays emission data for a given block height.

3. What is the purpose of the `EmissionInfo` case class?
- The `EmissionInfo` case class is a data container for emission data for a block at a given height, including miner reward, total coins issued, total remaining coins, and re-emission tokens issuance (if EIP-27 is activated).