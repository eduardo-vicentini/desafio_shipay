## Docker

Para rodar a aplicação no docker:

    chmod +x run_docker.sh
    ./run_docker.sh

## Servidor gunicorn

Rode o servidor executando o comando:

    chmod +x run_server.sh
    ./run_server.sh

## Configuração para rodar diretamente do flask

Configure o ambiente:

    export FLASK_APP=application.py

Rode o flask para começar a ouvir por requisições:

    flask run


## Testes

Os testes unitários estão no arquivo tests.py. Para rodar:

    python tests.py

Para rodar um request POST padrão:

    chmod +x request_test.sh
    ./requests_test.sh

## API

Essa é uma API que recebe requisições HTTP do tipo POST
na url: api/v1/transicao

A requisição precisa ser do tipo JSON, com a estrutura:

    {
    "estabelecimento": "45.283.163/0001-67",
    "cliente": "094.214.930-01",
    "valor": 590.01,
    "descricao": "Almoço em restaurante chique pago via Shipay!"
    }
    
A resposta retornada será se ela foi aceita:

    {
    "aceito": true
    }

Todas essas requisições serão permanecidas em um banco de dados
sqlite3, seja ela aceita ou não.

### Exemplo

Um exemplo de uma requisição bem sucedida seria:

    curl -X POST "http://0.0.0.0:5000/api/v1/transacao" \
    -H "Content-Type: application/json" --data \
    '{"estabelecimento":"45.283.1630001-67", "cliente":"10003800054",
    "valor":"100.52", "descricao":"nova descricção"}'

ou:

    curl -X POST "http://0.0.0.0:5000/api/v1/transacao" \
    -H "Content-Type: application/json" --data \
    '{"estabelecimento":"45.283.163/0001-67", "cliente":"100.038.000-54",
    "valor":"100.52", "descricao":"nova descricção"}' 

O retorno será:

    {"aceito":true}