The Ergo (reference client), ergoweb (ergoplatform.org), and sigmastate-interpreter are currently parsed and available for querying using [autodoc](https://github.com/context-labs/autodoc#get-started). 

Below is a basic example of how to get started, you can also just look through the markdown files in [training/output/autodocs](/training/output/autodocs) manually. 


## Querying


```
npm install -g @context-labs/autodoc
```

Create an `.env` file with your API key by running the following command

```
echo "OPENAI_API_KEY=<your-api-key>" > .env
```


Assuming you are in the directory for this repository, change into the directory you want to query 

```
cd training/outputs/autodocs/ergo
```

and start the query CLI

```
doc q
```

