[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/scala/org/ergoplatform/http/api/requests)

The code in the `.autodoc/docs/json/src/main/scala/org/ergoplatform/http/api/requests` folder contains case classes that represent various types of requests related to the Ergo platform. These requests are used to interact with the Ergo HTTP API, allowing users to execute ErgoScript contracts, extract prover hints from transactions, and more.

1. **CryptoResult.scala**: This file defines the `CryptoResult` case class, which represents the result of reducing an `ErgoTree` for a given context. It is used in the `/script/executeWithContext` endpoint of the Ergo HTTP API. The class has two fields: `value` (a `SigmaBoolean` representing the sigma-proposition to be proven) and `cost` (a `Long` representing the cost of the original script). This class is used to encapsulate the result of executing an Ergo script with a given context, returning the sigma-proposition and cost of the original script.

   Example usage:

   ```scala
   import org.ergoplatform.http.api.requests.CryptoResult
   import sigmastate.Values.SigmaBoolean

   val ergoTree = // create an ErgoTree
   val context = // create a context for the ErgoTree
   val result = // execute the ErgoTree with the given context
     CryptoResult(ergoTree.reduceToSigmaBoolean(context), ergoTree.cost(context))
   ```

2. **ExecuteRequest.scala**: This file defines the `ExecuteRequest` case class, which represents a request to execute a script in a given context. It takes three parameters: `script` (ErgoScript source code), `env` (a map of named constants for script compilation), and `ctx` (an instance of `ErgoLikeContext` representing the execution context).

   Example usage:

   ```scala
   import org.ergoplatform.http.api.requests.ExecuteRequest
   import org.ergoplatform.ErgoLikeContext

   val ctx = new ErgoLikeContext(...)
   val env = Map("x" -> 10, "y" -> 20)
   val request = ExecuteRequest("contract code here", env, ctx)
   executeScript(request)
   ```

3. **HintExtractionRequest.scala**: This file defines the `HintExtractionRequest` case class, which represents a request for extracting prover hints from a transaction in the Ergo platform. It takes several parameters, including `tx` (transaction), `real` (real signers of transaction inputs), `simulated` (simulated signers of transaction inputs), and optional `inputs` and `dataInputs` (hex-encoded input boxes bytes and data-input boxes bytes for the unsigned transaction).

   This class is used to extract prover hints from a transaction, which can then be used to create a proof of correctness for the transaction. The `real` and `simulated` parameters specify the actual and simulated signers of the transaction inputs, respectively.

In summary, the code in this folder provides essential components for interacting with the Ergo HTTP API, enabling users to execute ErgoScript contracts, extract prover hints from transactions, and more. These case classes serve as important building blocks for the larger Ergo platform project, facilitating the creation and verification of transactions and smart contracts.
