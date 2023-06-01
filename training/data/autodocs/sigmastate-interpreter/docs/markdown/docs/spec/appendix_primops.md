[View code on GitHub](sigmastate-interpreterhttps://github.com/ScorexFoundation/sigmastate-interpreter/docs/spec/appendix_primops.tex)

This code defines a table of predefined global functions, along with their mnemonics, signatures, and descriptions. The table is generated from sigma operation descriptors and includes functions such as SelectField, SomeValue, NoneValue, and Collection. 

The purpose of this code is to provide a reference for developers working on the larger project to easily access and utilize these predefined functions. By including the signatures and descriptions, developers can quickly understand the inputs and outputs of each function and how they can be used in their code. 

For example, a developer may need to extract a specific field from a tuple. They can use the SelectField function by passing in the tuple and the index of the desired field. The function will return the value of that field. 

Overall, this code serves as a helpful tool for developers to efficiently use the predefined global functions in their code.
## Questions: 
 1. What is the purpose of this code file?
- This code file defines a table of predefined global functions for a programming language called \langname.

2. What is the format of the table in this code file?
- The table is a longtable with four columns: Code, Mnemonic, Signature, and Description. The first three columns contain text, while the last column can contain a paragraph of text.

3. Where does the data for the table come from?
- The data for the table is autogenerated from sigma operation descriptors and is located in two separate files: "predeffunc_rows.tex" and "predeffunc_sections.tex".