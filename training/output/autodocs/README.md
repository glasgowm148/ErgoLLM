# README

The subfolders in this section were generated with [autodocs](https://github.com/context-labs/autodoc)

Below is a basic example of how to get started, you can also just look through the markdown files in [training/output/autodocs](/training/output/autodocs) manually. 


```
# Autodoc requires Node v18.0.0 or greater. v19.0.0+ is recommended. 
node -v
# Install the Autodoc CLI tool as a global NPM module:
npm install -g @context-labs/autodoc
```


Right now Autodoc only supports OpenAI. Make sure you have have your OpenAI API key exported in your current session:


```
export OPENAI_API_KEY=<YOUR_KEY_HERE>
```

To start the Autodoc query CLI, run the following command from within the directory you want to query (ie [ergo-appkit](ergo-appkit/))

```
doc q
```

From within the folders in this directory. 

![](/training/output/autodocs/example.png)


