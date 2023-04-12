[View code on GitHub](https://github.com/ergoplatform/ergo/ergo-wallet/src/main/scala/org/ergoplatform/wallet/AssetUtils.scala)

The `AssetUtils` object contains utility functions for working with assets in the Ergo platform. The functions are designed to work with `TokensMap`, which is a type alias for `Map[ModifierId, Long]`. The `ModifierId` is a unique identifier for a transaction output, and the `Long` value represents the amount of the asset held in that output.

The `mergeAssetsMut` function takes a mutable map `into` and one or more `TokensMap` instances `from`. It merges the `from` maps into the `into` map, adding the amounts of each asset together if the asset already exists in the `into` map, or creating a new entry if the asset does not exist. This function modifies the `into` map in place.

Example usage:
```scala
import org.ergoplatform.wallet.AssetUtils

val into = collection.mutable.Map(
  Array[Byte](1, 2, 3) -> 100L,
  Array[Byte](4, 5, 6) -> 200L
)
val from1 = Map(
  Array[Byte](1, 2, 3) -> 50L,
  Array[Byte](7, 8, 9) -> 300L
)
val from2 = Map(
  Array[Byte](4, 5, 6) -> 150L,
  Array[Byte](10, 11, 12) -> 400L
)

AssetUtils.mergeAssetsMut(into, from1, from2)

// into now contains:
// Map(
//   Array[Byte](1, 2, 3) -> 150L,
//   Array[Byte](4, 5, 6) -> 350L,
//   Array[Byte](7, 8, 9) -> 300L,
//   Array[Byte](10, 11, 12) -> 400L
// )
```

The `mergeAssets` function is similar to `mergeAssetsMut`, but it returns a new `TokensMap` instead of modifying an existing one. It takes an initial `TokensMap` and one or more `TokensMap` instances to merge into it.

Example usage:
```scala
import org.ergoplatform.wallet.AssetUtils

val initialMap = Map(
  Array[Byte](1, 2, 3) -> 100L,
  Array[Byte](4, 5, 6) -> 200L
)
val map1 = Map(
  Array[Byte](1, 2, 3) -> 50L,
  Array[Byte](7, 8, 9) -> 300L
)
val map2 = Map(
  Array[Byte](4, 5, 6) -> 150L,
  Array[Byte](10, 11, 12) -> 400L
)

val merged = AssetUtils.mergeAssets(initialMap, map1, map2)

// merged is now:
// Map(
//   Array[Byte](1, 2, 3) -> 150L,
//   Array[Byte](4, 5, 6) -> 350L,
//   Array[Byte](7, 8, 9) -> 300L,
//   Array[Byte](10, 11, 12) -> 400L
// )
```

The `subtractAssets` function takes an initial `TokensMap` and one or more `TokensMap` instances to subtract from it. It returns a new `TokensMap` with the amounts of each asset subtracted. If an asset does not exist in the initial map, an exception is thrown. If the amount to subtract is negative or greater than the amount in the initial map, an exception is thrown. If the amount to subtract is equal to the amount in the initial map, the asset is removed from the result map.

Example usage:
```scala
import org.ergoplatform.wallet.AssetUtils

val initialMap = Map(
  Array[Byte](1, 2, 3) -> 100L,
  Array[Byte](4, 5, 6) -> 200L
)
val map1 = Map(
  Array[Byte](1, 2, 3) -> 50L,
  Array[Byte](7, 8, 9) -> 300L
)
val map2 = Map(
  Array[Byte](4, 5, 6) -> 150L,
  Array[Byte](10, 11, 12) -> 400L
)

val subtracted = AssetUtils.subtractAssets(initialMap, map1, map2)

// subtracted is now:
// Map(
//   Array[Byte](1, 2, 3) -> 50L,
//   Array[Byte](4, 5, 6) -> 50L
// )
```

The `subtractAssetsMut` function takes a mutable map `from` and a `TokensMap` `subtractor`. It subtracts the amounts of each asset in the `subtractor` map from the `from` map, modifying the `from` map in place. If an asset does not exist in the `from` map, an exception is thrown. If the amount to subtract is equal to the amount in the `from` map, the asset is removed from the map.

Example usage:
```scala
import org.ergoplatform.wallet.AssetUtils

val from = collection.mutable.Map(
  Array[Byte](1, 2, 3) -> 100L,
  Array[Byte](4, 5, 6) -> 200L
)
val subtractor = Map(
  Array[Byte](1, 2, 3) -> 50L,
  Array[Byte](7, 8, 9) -> 300L
)

AssetUtils.subtractAssetsMut(from, subtractor)

// from is now:
// Map(
//   Array[Byte](1, 2, 3) -> 50L,
//   Array[Byte](4, 5, 6) -> 200L
// )
```
## Questions: 
 1. What is the purpose of the `AssetUtils` object?
    
    The `AssetUtils` object provides utility functions for merging and subtracting token maps.

2. What is the difference between `mergeAssetsMut` and `mergeAssets`?
    
    `mergeAssetsMut` takes a mutable map as its first argument and modifies it in place, while `mergeAssets` returns a new map without modifying the original.

3. What happens if a token to subtract is not found in the initial map in `subtractAssets`?
    
    An `IllegalArgumentException` is thrown with a message indicating that the token was not found in the initial map.