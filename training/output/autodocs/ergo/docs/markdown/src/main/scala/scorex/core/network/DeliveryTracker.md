[View code on GitHub](https://github.com/ergoplatform/ergo/src/main/scala/scorex/core/network/DeliveryTracker.scala)

The `DeliveryTracker` class in the `scorex.core.network` package is responsible for tracking the status of modifiers in a blockchain-based project. Modifiers can have one of the following states: Unknown, Requested, Received, Held, Invalid. The class maintains these states in the `requested`, `received`, and `invalid` collections.

The primary purpose of this class is to manage the lifecycle of modifiers as they transition between states. In a typical success path, a modifier will transition from Unknown -> Requested -> Received -> Held. If something goes wrong, the modifier may transition back to Unknown or Invalid states.

The `DeliveryTracker` class provides several methods to manage and query the status of modifiers, such as `setRequested`, `setInvalid`, `setHeld`, `setUnknown`, and `setReceived`. These methods are used to update the status of a modifier and perform necessary actions, such as canceling requests or updating the internal collections.

Additionally, the class provides methods to query the number of modifiers to download (`headersToDownload` and `modifiersToDownload`) and the status of a specific modifier (`status`).

The `DeliveryTracker` class is not thread-safe and should be used only as a local field of an actor. Its methods should not be called from lambdas, `Future`, `Future.map`, etc.

Here's an example of how the `DeliveryTracker` class might be used in a larger project:

```scala
val deliveryTracker = new DeliveryTracker(cacheSettings, desiredSizeOfExpectingModifierQueue)

// Set a modifier as requested
deliveryTracker.setRequested(typeId, id, supplier, checksDone)(schedule)

// Set a modifier as received
deliveryTracker.setReceived(id, modifierTypeId, sender)

// Set a modifier as held
deliveryTracker.setHeld(id, modifierTypeId)

// Set a modifier as invalid
deliveryTracker.setInvalid(id, modifierTypeId)

// Get the status of a modifier
val modifierStatus = deliveryTracker.status(modifierId, modifierTypeId, modifierKeepers)
```

The `DeliveryTracker` class is an essential component in managing the state of modifiers in a blockchain-based project, ensuring that modifiers are correctly processed and transitioned between states.
## Questions: 
 1. **What is the purpose of the `DeliveryTracker` class?**

   The `DeliveryTracker` class is responsible for tracking the status of modifiers in a network. It keeps track of modifiers in different states such as Unknown, Requested, Received, Held, and Invalid. It also provides methods to transition between these states and performs checks to ensure that the transitions are valid.

2. **How does the `DeliveryTracker` handle invalid modifiers?**

   The `DeliveryTracker` uses a Bloom Filter based cache (`invalidModifierCache`) to store invalid modifier ids. When a modifier is marked as invalid, it is added to this cache. The cache has a configurable size and expiration time, which can be set in the `NetworkCacheSettings`.

3. **What is the purpose of the `isCorrectTransition` function?**

   The `isCorrectTransition` function checks if a transition between two modifier statuses is valid. It ensures that the modifier follows the correct state transition rules, such as going from Unknown to Requested, Requested to Received, and so on. If an invalid transition is detected, it logs an error message to help developers identify the issue.