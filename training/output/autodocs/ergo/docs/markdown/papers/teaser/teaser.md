[View code on GitHub](https://github.com/ergoplatform/ergo/papers/teaser/teaser.tex)

The code is a LaTeX document that provides an overview of the Ergo Platform project. The document is divided into several sections, each of which describes a key aspect of the project. 

The first section, "Vision," explains that the Ergo Platform is designed to be a decentralized blockchain platform that is useful for decentralized applications. The platform is designed to be a "blockchain 1.1" implementation, which means that it is a major update to blockchain technology rather than a revolutionary change. The section goes on to explain that the platform is designed to be survivable in the long-term, which is essential for it to be a powerful store of value.

The second section, "Consensus," describes the consensus protocol used by the Ergo Platform. The protocol, called Autolykos, is based on the Proof-of-Work (PoW) consensus algorithm. Autolykos is designed to prevent the centralization of the network around pool operators and ASIC manufacturers, which is a severe threat to long-term survivability. 

The third section, "Clients," explains that Ergo was designed to be maximally user-friendly in the sense of decentralization. Ergo blocks support NiPoPoW proofs, allowing light clients to synchronize with the network by downloading less than a megabyte of data. In addition, Ergo uses authenticated state, and for any transaction included, a client may download a proof of its correctness. Thus, regardless of the blockchain size, a regular user with a smart-phone can join the network and start using Ergo with the same security guarantees as a full node.

The fourth section, "Survivability," explains that long-term survivability and the confidence of users in the platform’s long-term survivability is essential for Ergo or any other cryptocurrency to be a store-of-value. To achieve survivability, Ergo provides economic improvements in addition to the technical ones, most central of which is a storage fee component which plays an important role for Ergo`s stability. 

The fifth section, "Economy," explains that Ergo emission will last for 8 years, and to fund the Ergo development, during the first 2.5 years, the part of the block reward that exceeds 67.5 will go to a treasury instead of a miner. Ergo emission will start from zero with no pre-mine. 

The sixth section, "Applicability," explains that DApps and offchain protocols may be implemented in a truly decentralized way due to light clients, however, they also require a useful and safe smart contract language. Ergo smart contracts are based on a Bitcoin-like UTXO model, where every output is protected by some script. 

The final section, "Conclusions," summarizes the key points of the document and highlights the most distinguishing characteristics of the Ergo Platform. 

Overall, this code provides a high-level overview of the Ergo Platform project, including its vision, consensus protocol, clients, survivability, economy, and applicability. It is intended to provide a general idea of the project and its main features, and more details about the platform can be found in the whitepaper, as well as in separate highly specialized papers covering key components of the platform.
## Questions: 
 1. What is the consensus protocol used by Ergo and how does it prevent centralization?
- Ergo uses the Autolykos consensus protocol, which is based on Proof-of-Work (PoW) but also incorporates memory-hard computations and a Schnorr signature variant to prevent the advantage of ASIC-equipped miners and pool operators. This returns Ergo to the original one-CPU-one-vote idea from the Bitcoin whitepaper.

2. How does Ergo ensure user-friendliness and decentralization for clients?
- Ergo blocks support NiPoPoW proofs, allowing light clients to synchronize with the network by downloading less than a megabyte of data. In addition, Ergo uses authenticated state and provides proofs of transaction correctness, allowing regular users with smartphones to join the network and use Ergo with the same security guarantees as a full node.

3. What economic improvements does Ergo provide for its stability and survivability?
- Ergo provides a storage fee component, where if an output remains in state for 4 years without being moved, a miner may charge a small fee for every byte kept in the state. This allows Ergo mining to always be stable, reduces hardware requirements for miners, and prevents steady decrease of circulating supply due to lost keys. Ergo emission will last for 8 years, with no pre-mine, and part of the block reward will go to a treasury to fund Ergo development.