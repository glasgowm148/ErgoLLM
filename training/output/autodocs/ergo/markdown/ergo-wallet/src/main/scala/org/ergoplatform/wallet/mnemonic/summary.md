[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/ergo-wallet/src/main/scala/org/ergoplatform/wallet/mnemonic)

The `org.ergoplatform.wallet.mnemonic` package contains two main files: `Mnemonic.scala` and `WordList.scala`. These files provide functionality for generating and converting BIP39 mnemonic phrases, which can be used as seeds for generating cryptographic keys in the Ergo project.

`Mnemonic.scala` defines the `Mnemonic` class, which is responsible for generating and converting mnemonic phrases. It takes two parameters: `languageId` (a string identifying the language to be used in the mnemonic phrase) and `strength` (the number of bits in the seed). The class has two methods: `generate` (generates a new mnemonic phrase from system randomness) and `toMnemonic` (generates a new mnemonic phrase from a given entropy). Both methods return a `Try[SecretString]` object containing the generated mnemonic phrase.

The `Mnemonic` object contains several constants related to the BIP39 standard and a `toSeed` method, which takes a `SecretString` object containing the mnemonic phrase and an optional `SecretString` object containing the passphrase. It returns the encoded secret key as an array of bytes.

`WordList.scala` defines the `WordList` class and an object with methods to load word lists from text files. The `WordList` class contains a sequence of strings representing words and a delimiter string. The object provides a list of available languages and a method to load a word list for a given language.

The `load` method takes a `languageId` string as input and returns a `Try[WordList]`. It matches the `languageId` against a list of available languages and loads the corresponding text file using the `resourceLoader` method. The loaded file is then parsed into a sequence of strings using the `loadFile` method and wrapped in a `WordList` object with the appropriate delimiter.

These files can be used in the larger project to provide a secure and standardized way of generating and converting mnemonic phrases. For example, to generate a new mnemonic phrase in English with a strength of 128 bits, you can use the following code:

```scala
import org.ergoplatform.wallet.mnemonic.Mnemonic

val mnemonicTry = Mnemonic("english", 128).generate()
mnemonicTry match {
  case Success(mnemonic) => println(mnemonic)
  case Failure(exception) => println(exception.getMessage)
}
```

To load the English word list and print its words to the console, you can use the following code:

```scala
import org.ergoplatform.wallet.mnemonic.WordList

val wordListTry = WordList.load("english")
wordListTry match {
  case Success(wordList) => println(wordList.words)
  case Failure(exception) => println(exception.getMessage)
}
```

Overall, the `org.ergoplatform.wallet.mnemonic` package provides functionality for generating and converting BIP39 mnemonic phrases, which can be used as seeds for generating cryptographic keys in the Ergo project.
