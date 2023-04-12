[View code on GitHub](https://github.com/ergoplatform/ergo/src/main/scala/org/ergoplatform/nodeView/wallet/IdUtils.scala)

The `IdUtils` object in the `wallet` package of the `ergo` project provides utility methods for encoding and decoding box and token IDs. 

The `EncodedBoxId` type is defined as a `TaggedType` with a `String` underlying type. This allows for type safety when passing around encoded box IDs. The `EncodedTokenId` type is defined as a `ModifierId`, which is a type alias for `Digest32`. 

The `encodedBoxId` method takes a `BoxId` and returns an `EncodedBoxId` by encoding the `BoxId` using the `Algos.encode` method. The `decodedBoxId` method takes an `EncodedBoxId` and returns a `BoxId` by decoding the `EncodedBoxId` using the `Algos.decode` method and wrapping the resulting `Array[Byte]` in an `ADKey`. If decoding fails, an error is thrown.

Similarly, the `encodedTokenId` method takes a `TokenId` and returns an `EncodedTokenId` by encoding the `TokenId` using the `Algos.encode` method. The `decodedTokenId` method takes an `EncodedTokenId` and returns a `TokenId` by decoding the `EncodedTokenId` using the `Algos.decode` method and wrapping the resulting `Array[Byte]` in a `Digest32`. If decoding fails, an error is thrown.

These utility methods can be used throughout the `ergo` project to encode and decode box and token IDs as needed. For example, if a method requires an encoded box ID as input, it can call the `encodedBoxId` method to encode the `BoxId` before passing it in. Similarly, if a method returns an encoded token ID, it can use the `encodedTokenId` method to encode the `TokenId` before returning it.
## Questions: 
 1. What is the purpose of the `IdUtils` object?
    - The `IdUtils` object provides methods for encoding and decoding box and token IDs in the Ergo platform.
2. What is the purpose of the `EncodedBoxId` and `EncodedTokenId` types?
    - The `EncodedBoxId` type is a tagged type that represents an encoded box ID as a string. The `EncodedTokenId` type is a modifier ID that represents an encoded token ID.
3. What hashing and encoding algorithms are used in this code?
    - The code uses the `Algos` object from the `org.ergoplatform.settings` package to encode and decode box and token IDs. It also uses the `ADKey` and `Digest32` classes from the `scorex.crypto.authds` and `scorex.crypto.hash` packages, respectively.