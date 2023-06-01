[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/it/scala/org/ergoplatform/it/util)

The `util.scala` file in the `org.ergoplatform.it.util` package provides two implicit classes, `TimerExt` and `RichEither`, which offer utility methods for scheduling tasks and error handling in the Ergo project.

`TimerExt` extends the `io.netty.util.Timer` class and adds a `schedule` method. This method takes a function `f` returning a `Future[A]` and a `delay` of type `FiniteDuration`. It schedules the execution of the function `f` after the specified `delay` duration. When the timer expires, a new `Promise[A]` is created and completed with the result of the function `f`. If an exception occurs during the execution of `f`, the `Promise` is failed with the exception. The method returns the `Future[A]` associated with the `Promise`. This can be useful for scheduling tasks to be executed after a certain delay in the Ergo project. For example:

```scala
import org.ergoplatform.it.util._

val timer: Timer = ...
val delay = 5.seconds
val futureResult: Future[Int] = timer.schedule(() => Future.successful(42), delay)
```

`RichEither` extends the `Either[String, A]` class and adds two methods, `toFuture` and `get`. The `toFuture` method converts the `Either` to a `Future[A]`. If the `Either` is a `Left` with a `String` error message, it is converted to a `Try` with a new `Exception` and then to a `Future` with `Future.fromTry`. If the `Either` is a `Right` with a value of type `A`, it is converted to a `Future` with `Future.successful`. This simplifies error handling by converting an `Either` to a `Future`. For example:

```scala
import org.ergoplatform.it.util._

val either: Either[String, Int] = Right(42)
val futureResult: Future[Int] = either.toFuture
```

The `get` method returns the value of type `A` if the `Either` is a `Right`. If the `Either` is a `Left`, it throws a new `Exception` with the error message. This can be used to extract the value of type `A` from a `Right` `Either`. For example:

```scala
import org.ergoplatform.it.util._

val either: Either[String, Int] = Right(42)
val result: Int = either.get
```

These utility methods provide useful abstractions for common tasks in the Ergo project, such as scheduling tasks with a delay and handling errors with `Either` and `Future`.
