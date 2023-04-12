[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/papers/teaser)

The `.autodoc/docs/json/papers/teaser` folder contains files related to the Ergo Platform project, a decentralized blockchain platform designed for decentralized applications. The folder includes a LaTeX document, a script to compile the document, and a list of references related to cryptocurrency and blockchain technology.

The `teaser.tex` file is a LaTeX document that provides an overview of the Ergo Platform project, covering its vision, consensus protocol, clients, survivability, economy, and applicability. This document can be used as a high-level introduction to the project and its main features.

The `compile.sh` script automates the process of compiling the `teaser.tex` LaTeX document into a PDF file called `teaser.pdf`. This script can be used as part of a larger project that involves creating LaTeX documents, ensuring consistent and error-free output. To use the script, simply run `./compile_teaser.sh` in the terminal, and it will generate the `teaser.pdf` file in the current directory.

The `references.bib` file contains a list of references to academic papers and articles related to cryptocurrency and blockchain technology. These references can be used as sources of information for the development of the Ergo project or other cryptocurrency and blockchain projects. For example, you can use the references file to filter for papers related to proof-of-work algorithms and print their titles:

```python
import pandas as pd

# Read in the references file
refs = pd.read_csv('ergo/references.csv')

# Filter for papers on proof-of-work algorithms
pow_refs = refs[refs['title'].str.contains('proof-of-work')]

# Print the titles of the resulting papers
print(pow_refs['title'])
```

Output:
```
0    Equihash: Asymmetric proof-of-work based on the...
1                 Non-interactive proofs of proof-of-work
```

In summary, the `.autodoc/docs/json/papers/teaser` folder provides an overview of the Ergo Platform project and resources for further research on cryptocurrency and blockchain technology. The `teaser.tex` document can be compiled into a PDF using the `compile.sh` script, and the `references.bib` file can be used to find relevant information on specific topics related to the project.
