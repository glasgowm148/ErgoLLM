# Running locally

## Prerequistes 

```
git clone https://github.com/arc53/DocsGPT.git
cd DocsGPT
```

Replace `custom_string` with your API key and execute the following command

```
sed "s/<your_api_key>/${custom_string}/g" docker-compose.yaml
```

## Getting Started

Create an `.env` file with your API key by running the following command

```
echo "OPENAI_API_KEY=<your-api-key>" > .env
```

Start docker from within the DocsGPT directory

```
docker-compose build && docker-compose up
```

Navigate to [localhost:5173](http://localhost:5173/)

## Data

You can pre-load the training data stored in [training](/training/output/docsgpt/) by moving the `index` files to the `application/` folder. (Overwrite the existing ones)

### Training on new data

Place the files you want to train on in `input/`

Currently supported: .rst, .md, .pdf, .docx, .csv, .epub, .html

Create an `.env` file with your API key by running the following command

```
echo "OPENAI_API_KEY=<your-api-key>" > .env
```

Run `ingest.py` and will tell you how much it will cost and ask if you want to proceed.

```
python ingest.py ingest
```

> You may need to use `python3 ingest.py ingest` or `python3.9 ingest.py ingest` if you encounter errors here. 

After this completes, you should see new `index.faiss` and `index.pkl` files appear in `output/` which you should move to `application/` 

Once you run it will use new context that is relevant to your documentation Make sure you select default in the dropdown in the UI

