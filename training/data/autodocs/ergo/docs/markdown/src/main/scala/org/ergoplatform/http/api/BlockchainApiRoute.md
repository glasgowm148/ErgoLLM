[View code on GitHub](https://github.com/ergoplatform/ergo/src/main/scala/org/ergoplatform/http/api/BlockchainApiRoute.scala)

`BlockchainApiRoute` is a class that provides HTTP API endpoints for querying various aspects of the Ergo blockchain. It is designed to work with the Ergo platform and uses the Actor model for concurrency and message passing. The class takes three parameters: `readersHolder`, `ergoSettings`, and `indexer`.

The class defines several directives to handle input parameters, such as `paging`, `sortMarshaller`, and `sortDir`. These directives are used to extract and validate input parameters from the HTTP request.

The main functionality of the class is exposed through the `route` method, which defines the HTTP API endpoints. These endpoints include:

- `getIndexedHeightR`: Returns the indexed height of the blockchain.
- `getTxByIdR`: Returns a transaction by its ID.
- `getTxByIndexR`: Returns a transaction by its index.
- `getTxsByAddressR`: Returns transactions associated with a given address.
- `getTxRangeR`: Returns a range of transactions.
- `getBoxByIdR`: Returns a box by its ID.
- `getBoxByIndexR`: Returns a box by its index.
- `getBoxesByAddressR`: Returns boxes associated with a given address.
- `getBoxesByAddressUnspentR`: Returns unspent boxes associated with a given address.
- `getBoxRangeR`: Returns a range of boxes.
- `getBoxesByErgoTreeR`: Returns boxes associated with a given ErgoTree.
- `getBoxesByErgoTreeUnspentR`: Returns unspent boxes associated with a given ErgoTree.
- `getTokenInfoByIdR`: Returns token information by its ID.
- `getAddressBalanceTotalR`: Returns the total balance for a given address.

Each of these endpoints is implemented as a separate method in the class, which uses the `readersHolder`, `ergoSettings`, and `indexer` to query the blockchain and return the requested information. The methods use `Future` to handle asynchronous operations and return the results as JSON objects.

For example, the `getTxsByAddress` method takes an `ErgoAddress`, `offset`, and `limit` as input parameters and returns a `Future` containing a tuple with a sequence of `IndexedErgoTransaction` objects and a long value representing the total number of transactions associated with the address. The method uses the `getHistory` method to obtain an `ErgoHistoryReader` instance and then retrieves the transactions using the `retrieveTxs` method of the `IndexedErgoAddress` class.

In summary, the `BlockchainApiRoute` class provides a set of HTTP API endpoints for querying various aspects of the Ergo blockchain, such as transactions, boxes, and balances. It uses the Actor model and `Future` for concurrency and asynchronous operations, and returns the results as JSON objects.
## Questions: 
 1. **Question**: What is the purpose of the `BlockchainApiRoute` class and what are its main functionalities?
   **Answer**: The `BlockchainApiRoute` class is responsible for handling HTTP API requests related to the Ergo blockchain. It provides various routes to fetch information such as transactions, boxes, token information, and address balances from the blockchain.

2. **Question**: What is the role of the `SortDirection` object and its associated types?
   **Answer**: The `SortDirection` object defines the sorting direction for certain API requests, such as retrieving unspent boxes by address. It has three possible values: `ASC` for ascending order, `DESC` for descending order, and `INVALID` for an invalid sorting direction.

3. **Question**: How does the `getAddressBalanceTotal` function work and what does it return?
   **Answer**: The `getAddressBalanceTotal` function takes an ErgoAddress as input and returns a Future containing a tuple of two `BalanceInfo` objects. The first `BalanceInfo` object represents the confirmed balance for the given address, while the second `BalanceInfo` object represents the unconfirmed balance (from the mempool) for the given address.