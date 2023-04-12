[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/ergo-wallet/src/main/scala/org/ergoplatform/wallet/crypto)

The `org.ergoplatform.wallet.crypto` package in the Ergo wallet project contains cryptographic utilities for encryption, decryption, and digital signatures. These utilities are essential for securing sensitive data and ensuring the integrity of messages in the Ergo wallet project.

The `AES` object provides methods for encrypting and decrypting data using the Advanced Encryption Standard (AES) algorithm in Galois/Counter Mode (GCM) with no padding. This secure encryption and decryption functionality can be used to protect sensitive data, such as a user's private key, before storing it in the wallet database and decrypting it when needed for signing transactions. Example usage:

```scala
val data = "Sensitive data".getBytes
val password = "Strong password".getBytes
val salt = "Random salt".getBytes
val iv = "Initialization vector".getBytes

val (ciphertext, authTag) = AES.encrypt(data, password, salt, iv)
val decryptedDataTry = AES.decrypt(ciphertext, password, salt, iv, authTag)
```

The `ErgoSignature` object implements the Schnorr signature scheme, providing `sign` and `verify` methods for signing messages and verifying their signatures. This can be used to sign transactions in a cryptocurrency system or authenticate users in a distributed system. Example usage:

```scala
val msg = "Hello, world!".getBytes
val sk = BigInt("1234567890abcdef", 16)
val pk = dlogGroup.exponentiate(dlogGroup.generator, sk.bigInteger)

val signature = ErgoSignature.sign(msg, sk)
val isValid = ErgoSignature.verify(msg, signature, pk)
```

The `HmacSHA512` object generates keyed hashes using the HMAC-SHA512 algorithm, which can be used for authentication and verification purposes, such as password storage, message authentication, and digital signatures. Example usage:

```scala
val key = "Secret key".getBytes
val data = "Message to be hashed".getBytes

val hmacHash = HmacSHA512.hash(key, data)
```

These cryptographic utilities work together to provide a secure foundation for the Ergo wallet project, ensuring the confidentiality and integrity of sensitive data and messages. Developers can use these utilities to implement secure storage, authentication, and verification mechanisms in the larger Ergo project.
