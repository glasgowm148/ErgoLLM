[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/ergo-wallet/src/main/java/org/ergoplatform/wallet/interface4j)

The `SecretString` class in the `.autodoc/docs/json/ergo-wallet/src/main/java/org/ergoplatform/wallet/interface4j` folder is a utility class that provides a more secure way of handling secret data than using a `char[]` directly. It can be used in the larger Ergo project to handle sensitive data such as passwords, private keys, and other secret information.

For example, to create a `SecretString` instance from a password, you can use the following code:

```java
char[] password = {'p', 'a', 's', 's', 'w', 'o', 'r', 'd'};
SecretString secretPassword = SecretString.create(password);
```

You can then use the `SecretString` instance to access and manipulate the secret data. For instance, to check if the secret data has been erased, you can use the `isErased()` method:

```java
boolean isErased = secretPassword.isErased();
```

The `crypto` subfolder contains two Java classes, `ErgoSignature` and `ErgoUnsafeProver`, which provide functionality for signing and verifying messages and transactions in the Ergo platform.

For example, to sign a message using `ErgoSignature`, you can use the following code:

```java
byte[] message = "Hello, world!".getBytes();
BigInteger privateKey = new BigInteger("123456789");
ErgoSignature ergoSignature = new ErgoSignature();
byte[] signature = ergoSignature.sign(message, privateKey);
```

To verify the signature, you can use the `verify` method:

```java
SecP256K1Point publicKey = ... // get public key from somewhere
boolean isValid = ergoSignature.verify(message, signature, publicKey);
```

To sign an unsigned transaction using `ErgoUnsafeProver`, you can use the following code:

```java
UnsignedErgoLikeTransaction unsignedTx = new UnsignedErgoLikeTransaction();
// add inputs and outputs to unsignedTx

DLogProtocol.DLogProverInput sk = new DLogProtocol.DLogProverInput();
// set sk to the private key of the signer

ErgoUnsafeProver prover = new ErgoUnsafeProver();
ErgoLikeTransaction signedTx = prover.prove(unsignedTx, sk);
// signedTx is the signed transaction
```

In summary, the code in this folder and its subfolder provides functionality for handling secret data and signing and verifying messages and transactions in the Ergo platform. Developers can use these classes to create and sign transactions, as well as verify the validity of signatures in the context of the Ergo project.
