[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/papers/yellow/pow)

The `pow` folder in the Ergo project contains code and documentation related to the Autolykos Proof-of-Work (PoW) algorithm used in the Ergo cryptocurrency. The Autolykos PoW algorithm is memory-hard and non-outsourceable, which aims to maintain decentralization and reduce the advantage of ASIC-equipped miners.

The `ErgoPow.tex` file describes the Autolykos PoW algorithm, its two versions, and the main differences between them. It also provides two main algorithms: Solution Verification and Block Mining. The Solution Verification algorithm checks if a given solution is valid, while the Block Mining algorithm is used by miners to find a valid solution for a new block. The Autolykos PoW algorithm is efficient in terms of solution size and verification time.

The `compile.sh` script is responsible for compiling the `ErgoPow.tex` LaTeX document into a PDF file called `ErgoPow.pdf`. This script can be used by developers and contributors to compile the document for distribution or publication. To use the script, run the following command in the same directory as the `ErgoPow.tex` file:

```bash
./compile.sh
```

The `references.bib` file contains a list of references related to the Ergo project, covering various topics related to blockchain technology, such as proof-of-work algorithms, mining hardware, and security issues. Studying these references can help developers gain a deeper understanding of the challenges and opportunities of building decentralized applications on the Ergo platform.

For example, developers working on the Ergo project might use the Autolykos PoW algorithm to implement mining functionality in the Ergo blockchain. They can refer to the `ErgoPow.tex` document to understand the algorithm's design and use the Solution Verification and Block Mining algorithms as a basis for their implementation. Additionally, they can use the `compile.sh` script to generate an up-to-date PDF version of the `ErgoPow.tex` document for easy reference or sharing with other team members.

In summary, the `pow` folder provides valuable resources for developers working on the Ergo project, specifically related to the Autolykos PoW algorithm. By understanding the algorithm and its implications for decentralization and ASIC resistance, developers can contribute to the development of a secure and flexible environment for decentralized applications on the Ergo platform.
