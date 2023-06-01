[View code on GitHub](https://github.com/ergoplatform/ergo/papers/yellow/peerManagement.tex)

# Peer Management Protocol

The `peer management protocol` is a module that manages the peers in a network. A peer is defined as a pair of IP address and port number. The module defines a `peer management structure` that consists of three sets: `good peers`, `banned peers`, and `connected peers`. The `good peers` set contains the peers that are currently considered good and can be connected to. The `banned peers` set contains the peers that are banned from the network due to some misbehavior. The `connected peers` set contains the peers that are currently connected to the network.

The module also defines a `penalty` structure that contains a description of the misbehavior and a penalty score. The penalty score is a number that defines how bad the misbehavior is. The penalties are divided into four categories: `NonDeliveryPenalty`, `MisbehaviorPenalty`, `SpamPenalty`, and `PermanentPenalty`. The `NonDeliveryPenalty` is applied when a peer fails to deliver a requested modifier in time. The `MisbehaviorPenalty` is applied when a modifier delivered by a peer is found to be invalid. The `SpamPenalty` is applied when a peer delivers a non-requested modifier. The `PermanentPenalty` is applied to peers that deviate from the network protocol.

Once a penalty is applied, the penalized peer is added to the `penalty book`. The `penalty book` is a mapping of IP addresses to penalty scores and timestamps. Penalties of the same type are not applied to the same peer repeatedly within a safe interval. The safe interval is a delay between penalty applications. Once a peer accumulates a critical penalty score, it is added to the `blacklist`. The `blacklist` is a mapping of IP addresses to timestamps until which the peer is banned.

The module also defines a `peer discovery protocol` that requests new peers from a source and inserts them into the `good peers` set. The source can be another peer, a trusted central server, or an untrusted communication channel like IRC or Twitter.

Overall, the `peer management protocol` module provides a way to manage the peers in a network by penalizing misbehaving peers and banning them if necessary, discovering new peers, and maintaining a list of good peers that can be connected to.
## Questions: 
 1. What is the purpose of the peer management structure and what are its components?
   
   The peer management structure is used to manage peers in the network and consists of three sets: good peers (G), banned peers (B), and connected peers (C). Good peers are those that are currently active and trusted, banned peers are those that have been penalized and are temporarily banned, and connected peers are those that are currently connected to the node.
   
2. What are the different types of penalties and when are they applied?
   
   There are four types of penalties: NonDeliveryPenalty, MisbehaviorPenalty, SpamPenalty, and PermanentPenalty. NonDeliveryPenalty is applied when a peer fails to deliver a requested modifier in time, MisbehaviorPenalty is applied when a delivered modifier is found to be invalid, SpamPenalty is applied when a non-requested modifier is delivered, and PermanentPenalty is applied when a peer deviates from the network protocol. Penalties of the first three types are not applied repeatedly to the same peer within a safe interval.
   
3. How does the peer discovery protocol work and what are the possible sources of new peers?
   
   The peer discovery protocol requests new peers from a source and adds them to the set of good peers. The source can be another peer, a trusted central server, or an untrusted communication channel such as IRC or Twitter.