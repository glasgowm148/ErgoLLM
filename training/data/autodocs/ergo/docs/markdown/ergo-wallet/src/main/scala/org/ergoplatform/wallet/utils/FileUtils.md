[View code on GitHub](https://github.com/ergoplatform/ergo/ergo-wallet/src/main/scala/org/ergoplatform/wallet/utils/FileUtils.scala)

The code above defines a trait called `FileUtils` which provides utility methods for working with files and directories. This trait can be mixed in with other classes or traits to provide them with file-related functionality.

The `deleteRecursive` method takes a `File` object representing a directory and deletes all of its contents recursively. This method is useful for cleaning up temporary directories or removing the contents of a directory before copying new files into it.

The `createTempFile` method creates a new temporary file in the default temporary directory. The file name is generated randomly using alphanumeric characters and a specified length. The method returns a `java.io.File` object representing the newly created file. The file is marked for deletion on exit, which means that it will be automatically deleted when the JVM exits.

The `createTempDir` method creates a new temporary directory in the default temporary directory. The directory name is generated randomly using alphanumeric characters and a specified length. The method returns a `java.io.File` object representing the newly created directory. The directory is marked for deletion on exit, which means that it will be automatically deleted when the JVM exits.

Overall, this trait provides convenient methods for working with temporary files and directories. These methods can be used in a variety of contexts, such as testing, file processing, or data analysis. For example, a class that needs to create temporary files for storing intermediate results could mix in this trait to simplify the process of creating and managing those files.
## Questions: 
 1. What is the purpose of the `FileUtils` trait?
- The `FileUtils` trait provides utility methods for file and directory operations.

2. What does the `deleteRecursive` method do?
- The `deleteRecursive` method performs a recursive deletion of the content of a directory.

3. What is the purpose of the `createTempFile` and `createTempDir` methods?
- The `createTempFile` method creates a temporary file with a random prefix and suffix in a temporary directory, and returns the file object. The `createTempDir` method creates a temporary directory with a random prefix, and returns the directory object. Both methods ensure that the created file or directory is deleted on exit.