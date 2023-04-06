[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/ergo-wallet/src/main/java/org/ergoplatform/wallet/interface4j/crypto)

The `.autodoc/docs/json/ergo-wallet/src/main/java/org/ergoplatform/wallet/interface4j/crypto` folder contains two Java classes, `ErgoSignature` and `ErgoUnsafeProver`, which provide functionality for signing and verifying messages and transactions in the Ergo platform.

`ErgoSignature` is a wrapper over a Schnorr signature implementation in Scala. It provides two methods, `sign` and `verify`, for signing and verifying messages using a private key and a public key, respectively. The `sign` method takes a message as a byte array and a private key as a `BigInteger`, while the `verify` method takes a message, a signature, and a public key as input parameters. These methods can be used in conjunction with other classes in the project to provide secure and efficient transaction signing and verification.

Example usage of `ErgoSignature`:

```java
byte[] message = "Hello, world!".getBytes();
BigInteger privateKey = new BigInteger("123456789");
ErgoSignature ergoSignature = new ErgoSignature();
byte[] signature = ergoSignature.sign(message, privateKey);

SecP256K1Point publicKey = ... // get public key from somewhere
boolean isValid = ergoSignature.verify(message, signature, publicKey);
```

`ErgoUnsafeProver` is a wrapper over a naive implementation of an Ergo prover. It provides two methods for signing all inputs of a given unsigned transaction. The first method takes an `UnsignedErgoLikeTransaction` and a `DLogProtocol.DLogProverInput` as input parameters, while the second method takes an `UnsignedErgoLikeTransaction` and a `Map` of `String` keys and `DLogProtocol.DLogProverInput` values as input parameters. Both methods return a signed transaction of type `ErgoLikeTransaction`. This class can be used in the larger Ergo project to facilitate the creation and signing of transactions.

Example usage of `ErgoUnsafeProver`:

```java
UnsignedErgoLikeTransaction unsignedTx = new UnsignedErgoLikeTransaction();
// add inputs and outputs to unsignedTx

DLogProtocol.DLogProverInput sk = new DLogProtocol.DLogProverInput();
// set sk to the private key of the signer

ErgoUnsafeProver prover = new ErgoUnsafeProver();
ErgoLikeTransaction signedTx = prover.prove(unsignedTx, sk);
// signedTx is the signed transaction
```

In summary, the code in this folder provides functionality for signing and verifying messages and transactions in the Ergo platform. Developers can use these classes to create and sign transactions, as well as verify the validity of signatures in the context of the Ergo project.
