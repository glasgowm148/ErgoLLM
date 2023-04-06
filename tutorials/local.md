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

Start docker

```
docker-compose build && docker-compose up
```

Navigate to [localhost:5173](http://localhost:5173/)