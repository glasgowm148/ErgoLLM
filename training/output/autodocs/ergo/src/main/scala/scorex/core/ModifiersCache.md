[View code on GitHub](https://github.com/ergoplatform/ergo/src/main/scala/scorex/core/ModifiersCache.scala)

The code defines two traits, `ModifiersCache` and `LRUCache`, which are used to store persistent modifiers that have not yet been applied to the history of a blockchain. The `ModifiersCache` trait is not thread-safe and should only be used as a local field of an actor. It contains a mutable map that stores key-value pairs of modifier IDs and block sections, respectively. The `modifierById` method returns an option of the modifier with the given ID. The `size` method returns the number of elements in the cache. The `maxSize` method defines the maximum number of elements that can be stored in the cache. The `findCandidateKey` method returns an option of the best candidate to be applied, based on an interface to the blockchain history. The `onPut` and `onRemove` methods are called when an element is added or removed from the cache, respectively. The `cleanOverfull` method removes elements from the cache when it is overfull. The `put` method adds an element to the cache if it does not already exist. The `remove` method removes an element from the cache. The `popCandidate` method returns an option of the best candidate to be applied and removes it from the cache.

The `LRUCache` trait extends the `ModifiersCache` trait and adds an eviction queue to implement a least-recently-used (LRU) cache. The `onPut` method enqueues the key to the eviction queue and removes any keys that are not in the cache and exceed the maximum size of the cache plus a cleaning threshold. The `cleanOverfull` method removes elements from the cache until the size is less than or equal to the maximum size of the cache or the eviction queue is empty. 

These traits are used to manage the storage of persistent modifiers in the Ergo blockchain project. The `ModifiersCache` trait provides a basic cache implementation, while the `LRUCache` trait adds an LRU eviction policy to the cache. These traits can be used by actors in the project to store and manage modifiers that have not yet been applied to the blockchain history. For example, an actor responsible for validating and applying new blocks to the blockchain history could use these traits to store and manage the modifiers that have not yet been applied.
## Questions: 
 1. What is the purpose of the `ModifiersCache` trait?
- The `ModifiersCache` trait is a cache that stores persistent modifiers that have not been applied to history yet.

2. What is the difference between `onPut` and `onRemove` methods?
- The `onPut` method is called when a new element is added to the cache, while the `onRemove` method is called when an element is removed from the cache.

3. What is the purpose of the `LRUCache` trait?
- The `LRUCache` trait extends the `ModifiersCache` trait and implements a Least Recently Used (LRU) cache eviction strategy, where the least recently used elements are removed from the cache when it is overfull.