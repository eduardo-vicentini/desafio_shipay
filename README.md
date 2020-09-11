To set the environment:

    export FLASK_APP=application.py

Run the application in the flask server:

    flask run

Build the docker:

    docker build -t dockerhub-username/repositorio .

Run the docker:

    ./run_docker.sh


## Testes

Os testes unitários estão no arquivo tests.py. Para rodar:

    python tests.py

## Api

Essa é uma API que recebe requisições HTTP do tipo POST
na url: api/v1/transicao

A requisição precisa ser do tipo JSON com a estrutura:

    {
    "estabelecimento": "45.283.163/0001-67",
    "cliente": "094.214.930-01",
    "valor": 590.01,
    "descricao": "Almoço em restaurante chique pago via Shipay!"
    }
    
A resposta retornada será aceita ou não:

    {
    "aceito": true
    }

Todas essas requisições serão permanecidas em um banco de dados
sqlite3.