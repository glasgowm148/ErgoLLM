[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/ergo-wallet/src/main/scala/org/ergoplatform/utils)

The `ArithUtils` object in the `org.ergoplatform.utils` package provides utility methods for performing arithmetic operations on `Long` values, handling overflow cases correctly. These methods are likely used throughout the larger `ergo` project to perform arithmetic operations on `Long` values in a way that handles overflow correctly.

### ArithUtils.scala

This file contains two methods:

1. `addExact(a: Long, b: Long)`: Adds two `Long` values and returns the result. If the addition operation results in an overflow, the method returns `Long.MaxValue`. The method is implemented using bitwise operations to detect overflow. The `@inline` annotation is used to indicate that the method should be inlined by the compiler for performance reasons.

Example usage:

```scala
val a: Long = Long.MaxValue - 1
val b: Long = 2
val sum: Long = ArithUtils.addExact(a, b)
println(sum) // prints Long.MaxValue
```

2. `addExact(a: Long, b: Long, c: Long*)`: A variadic method that takes two or more `Long` values and adds them together. The method uses `foldLeft` to iterate over the `c` sequence and accumulate the sum of all the values. The `addExact` method is used to add each value to the accumulated sum, ensuring that overflow is detected and handled correctly.

Example usage:

```scala
val a: Long = Long.MaxValue - 1
val b: Long = 2
val c: Long = 3
val sum: Long = ArithUtils.addExact(a, b, c)
println(sum) // prints Long.MaxValue
```

3. `multiplyExact(a: Long, b: Long)`: Multiplies two `Long` values and returns the result. If the multiplication operation results in an overflow, the method returns `Long.MaxValue`. The method is implemented using the `java7.compat.Math.multiplyExact` method, which throws an exception if the multiplication overflows. The exception is caught and handled by returning `Long.MaxValue`.

Example usage:

```scala
val a: Long = Long.MaxValue / 2 + 1
val b: Long = 2
val product: Long = ArithUtils.multiplyExact(a, b)
println(product) // prints Long.MaxValue
```

These utility methods are useful for performing arithmetic operations on `Long` values that may be close to the maximum value of a `Long` or the square root of `Long.MaxValue`. By using these methods, developers can ensure that overflow cases are handled correctly, preventing unexpected behavior in the larger `ergo` project.
