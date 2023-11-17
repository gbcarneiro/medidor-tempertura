# Backend

O backend dessa aplicação foi construído em [Flask]() e consiste em duas rotas principais:

```
    add/temperature [POST]
    get/temperature [GET]
```


## Adicionar temperatura (add/temperature)

Body request
```json
{
    "temperature": 50.0
}
```

Body response
```json
{
    "id": "655772d8acdfe320ae5b0cc2",
    "message": "Document inserted successfully",
    "success": true
}
```


## Obter temperatura mais recente
```json
{
  "date": "17/11/2023",
  "hour": "11:31",
  "temperature": 24
}
```

## Demo

A aplicação pode ser acessada através do link abaixo: 

https://flask-hello-world-eight-black.vercel.app/get/temperature 

Utilize uma ferramenta como o [Postman]() e envie para a rota POST:

https://flask-hello-world-eight-black.vercel.app/add/temperature


## Rode localmente

```bash
npm i -g vercel
vercel dev
```

Your Flask application is now available at `http://localhost:3000`.