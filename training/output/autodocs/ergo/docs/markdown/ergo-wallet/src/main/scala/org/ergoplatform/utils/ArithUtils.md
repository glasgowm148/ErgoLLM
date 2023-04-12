[View code on GitHub](https://github.com/ergoplatform/ergo/ergo-wallet/src/main/scala/org/ergoplatform/utils/ArithUtils.scala)

The `ArithUtils` object in the `org.ergoplatform.utils` package provides two methods for performing arithmetic operations on `Long` values. The first method, `addExact`, adds two `Long` values and returns the result. If the addition operation results in an overflow, the method returns `Long.MaxValue`. The method is implemented using bitwise operations to detect overflow. The `@inline` annotation is used to indicate that the method should be inlined by the compiler for performance reasons.

The second method, `addExact(a: Long, b: Long, c: Long*)`, is a variadic method that takes two or more `Long` values and adds them together. The method uses `foldLeft` to iterate over the `c` sequence and accumulate the sum of all the values. The `addExact` method is used to add each value to the accumulated sum, ensuring that overflow is detected and handled correctly.

The second method, `multiplyExact`, multiplies two `Long` values and returns the result. If the multiplication operation results in an overflow, the method returns `Long.MaxValue`. The method is implemented using the `java7.compat.Math.multiplyExact` method, which throws an exception if the multiplication overflows. The exception is caught and handled by returning `Long.MaxValue`.

These methods are likely used throughout the larger `ergo` project to perform arithmetic operations on `Long` values in a way that handles overflow correctly. The `addExact` method is particularly useful for adding values that may be close to the maximum value of a `Long`, while the `multiplyExact` method is useful for multiplying values that may be close to the square root of `Long.MaxValue`. Here is an example usage of the `addExact` method:

```
val a: Long = Long.MaxValue - 1
val b: Long = 2
val c: Long = 3
val sum: Long = ArithUtils.addExact(a, b, c)
println(sum) // prints Long.MaxValue
```
## Questions: 
 1. What does the `addExact` method do?
   - The `addExact` method adds two long values and returns `Long.MaxValue` if there was any long overflow.
2. What does the `multiplyExact` method do?
   - The `multiplyExact` method multiplies two long values and returns `Long.MaxValue` if there was any long overflow.
3. Why is the `multiplyExact` method using a try-catch block?
   - The `multiplyExact` method is using a try-catch block to catch any `Throwable` exception that may occur when using the `java7.compat.Math.multiplyExact` method.