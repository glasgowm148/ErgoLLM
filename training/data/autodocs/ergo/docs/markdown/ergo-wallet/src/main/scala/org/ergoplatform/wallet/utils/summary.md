[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/ergo-wallet/src/main/scala/org/ergoplatform/wallet/utils)

The `FileUtils.scala` file in the `org.ergoplatform.wallet.utils` package provides a trait called `FileUtils` that offers utility methods for working with files and directories. This trait can be mixed in with other classes or traits to provide them with file-related functionality, making it a useful component in various contexts such as testing, file processing, or data analysis.

One of the key methods in this trait is `deleteRecursive`, which takes a `File` object representing a directory and deletes all of its contents recursively. This method is particularly useful for cleaning up temporary directories or removing the contents of a directory before copying new files into it. For example, if you have a directory that needs to be cleared before new data is added, you can use this method as follows:

```scala
import org.ergoplatform.wallet.utils.FileUtils

class DirectoryCleaner extends FileUtils {
  def cleanDirectory(dir: File): Unit = {
    deleteRecursive(dir)
  }
}
```

Another important method provided by this trait is `createTempFile`, which creates a new temporary file in the default temporary directory. The file name is generated randomly using alphanumeric characters and a specified length. The method returns a `java.io.File` object representing the newly created file. The file is marked for deletion on exit, which means that it will be automatically deleted when the JVM exits. This method can be used to create temporary files for storing intermediate results, as shown in the following example:

```scala
import org.ergoplatform.wallet.utils.FileUtils

class TempFileCreator extends FileUtils {
  def createTempFileWithContent(content: String): File = {
    val tempFile = createTempFile()
    val writer = new PrintWriter(tempFile)
    writer.write(content)
    writer.close()
    tempFile
  }
}
```

Lastly, the `createTempDir` method creates a new temporary directory in the default temporary directory. The directory name is generated randomly using alphanumeric characters and a specified length. The method returns a `java.io.File` object representing the newly created directory. The directory is marked for deletion on exit, which means that it will be automatically deleted when the JVM exits. This method can be used to create temporary directories for storing files during processing, as demonstrated in the following example:

```scala
import org.ergoplatform.wallet.utils.FileUtils

class TempDirCreator extends FileUtils {
  def createTempDirForFiles(files: Seq[File]): File = {
    val tempDir = createTempDir()
    files.foreach(file => Files.copy(file.toPath, tempDir.toPath.resolve(file.getName)))
    tempDir
  }
}
```

In summary, the `FileUtils` trait provides convenient methods for working with temporary files and directories, which can be used in various parts of the Ergo project to simplify file management and processing tasks.
