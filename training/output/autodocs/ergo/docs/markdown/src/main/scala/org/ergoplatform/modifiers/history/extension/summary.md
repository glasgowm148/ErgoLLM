[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/scala/org/ergoplatform/modifiers/history/extension)

The code in this folder is responsible for handling the `Extension` and `ExtensionCandidate` classes, which are used to store key-value data in Ergo blocks. These classes are essential for storing additional data in Ergo blocks, such as system parameters, interlinks vectors, and validation rules.

`Extension.scala` defines the `Extension` class, which represents a key-value storage section of an Ergo block. It extends the `ExtensionCandidate` class and implements the `NonHeaderBlockSection` trait. The class contains utility methods and constants for working with key-value records, such as `kvToLeaf`, which converts a key-value record to a byte array, and `merkleTree`, which calculates the Merkle root of the key-value storage section.

`ExtensionCandidate.scala` defines the `ExtensionCandidate` class, which is a section of an extension block that holds key-value data. It is useful when a header is not formed yet. The class provides methods for manipulating the data, such as creating Merkle trees and proofs, and concatenating multiple `ExtensionCandidate` objects.

`ExtensionSerializer.scala` is responsible for serializing and deserializing `Extension` objects. It provides the `serialize` and `parse` methods, which allow `Extension` objects to be serialized and deserialized for storage and transmission.

Here's an example of how these classes might be used:

```scala
val fields = Seq((Array[Byte](0, 1), Array[Byte](1, 2, 3)), (Array[Byte](0, 2), Array[Byte](4, 5, 6)))
val extCandidate = ExtensionCandidate(fields)
val merkleTree = extCandidate.merkleTree
val digest = extCandidate.digest
val interlinksMerkleTree = extCandidate.interlinksMerkleTree
val interlinksDigest = extCandidate.interlinksDigest
val ext = extCandidate.toExtension(ModifierId @@ Array.fill(32)(1: Byte))
val newFields = Seq((Array[Byte](0, 3), Array[Byte](7, 8, 9)))
val newExtCandidate = ExtensionCandidate(newFields)
val concatenated = extCandidate ++ newExtCandidate
val proof = extCandidate.proofFor(Array[Byte](0, 1))
val batchProof = extCandidate.batchProofFor(Array[Byte](1, 2), Array[Byte](2, 3))

// Serialize and deserialize an Extension object
val extension = Extension(headerId, fields, Some(size))
val writer = new ByteArrayOutputStream()
ExtensionSerializer.serialize(extension, writer)
val bytes = writer.toByteArray()

// ...

val reader = new ByteArrayInputStream(bytes)
val extension2 = ExtensionSerializer.parse(reader)
```

In summary, the code in this folder is crucial for handling key-value data in Ergo blocks, providing methods for creating, manipulating, and serializing `Extension` and `ExtensionCandidate` objects. This functionality is essential for storing additional data in Ergo blocks and ensuring the integrity of the data through Merkle trees and proofs.
