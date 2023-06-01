[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/scala/org/ergoplatform/nodeView/wallet/scanning)

The code in this folder is responsible for scanning the Ergo blockchain for specific boxes based on user-defined criteria. It provides classes and methods for creating, serializing, and deserializing scans, as well as defining scanning predicates to filter boxes based on various conditions.

The `Scan` class wraps information about a user scan, which provides scanning rules for specific boxes and works with boxes found by the node. The `ScanRequest` class encodes an API request to create a scan. The `ScanSerializer` object defines methods for serializing and parsing `Scan` objects, and the `ScanJsonCodecs` object defines JSON codecs for `Scan` and `ScanRequest` objects.

The `ScanWalletInteraction` object defines an enumeration of three possible values for a flag that determines how a scan interacts with an in-built P2PK wallet. Developers can use this object to set the interaction flag for a scan and determine whether boxes found during the scan should be added to the wallet.

The `ScanningPredicate` trait and its subtypes define a set of scanning predicates that can be used to filter ErgoBoxes based on certain criteria. These scanning predicates provide a flexible and powerful way to filter ErgoBoxes based on various criteria, such as containing a specific asset or having a certain value in a register.

The `ScanningPredicateJsonCodecs` object contains implicit encoders and decoders for the `ScanningPredicate` trait and its subtypes, enabling encoding and decoding of `ScanningPredicate` objects to and from JSON format. The `ScanningPredicateSerializer` object is responsible for serializing and deserializing `ScanningPredicate` objects in binary format.

Example usage:

```scala
import org.ergoplatform.nodeView.wallet.scanning._

// Create a ContainsAssetPredicate to find boxes containing a specific asset
val assetId = "someAssetId"
val predicate = ContainsAssetPredicate(assetId)

// Create a Scan object with the predicate and other parameters
val scanId = 1
val scanDescription = "Scan for boxes containing asset"
val scanInteraction = ScanWalletInteraction.Shared
val removeOffchain = false
val scan = Scan(scanId, scanDescription, predicate, scanInteraction, removeOffchain)

// Serialize and deserialize the Scan object
val json = scan.asJson
val decodedScan = json.as[Scan]

// Use the Scan object to search for boxes in the Ergo blockchain
val boxes = searchForBoxes(scan)
```

In the larger Ergo project, this code enables users to scan the blockchain for specific boxes and interact with the p2pk-wallet. For example, a user could create a scan to search for boxes that contain a specific token or have a certain value. The `Scan` object would contain the rules for this search, and the `ScanRequest` object would encode an API request to create the scan. The `ScanSerializer` object would handle serialization and parsing of `Scan` objects, and the `ScanJsonCodecs` object would handle JSON encoding and decoding of `Scan` and `ScanRequest` objects.
