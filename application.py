#!/usr/bin/python3
# coding: UTF-8

import os

from flask import Flask, jsonify, request
from tempfile import mkdtemp

from database import Base, engine, SessionLocal
from helpers import parser
from models import Transaction

# Configure application
app = Flask(__name__)

# Create database if not exists
if not os.path.isfile("transaction.db"):
    Base.metadata.create_all(bind=engine)

# Start the conection with the db
db = SessionLocal()


@app.route("/api/v1/transacao", methods=["POST"])
def transaction_api():
    """
    Returns a JSON response when accessed by a POST method
    with the structure:
        # JSON POST:
        {
        "estabelecimento": "45.283.163/0001-67",
        "cliente": "094.214.930-01",
        "valor": 590.01,
        "descricao": "Almoço em restaurante chique pago via Shipay!"
        }
    
    The response is:
        {
        "aceito": true
        }

    All the informations about this transaction will be persisted in the
    database from the db variable.
    """
    if request.method != "POST":
        return jsonify({'error': "HTTP method not supported!"})

    # Handle empty requests
    if not request.json:
        return jsonify({'error': 'no request received'})


    parsed_data = parser(request.json)  

    aceito, estabelecimento, cliente, valor, descricao = parsed_data

    transaction_db = Transaction(
        estabelecimento=estabelecimento,
        cliente=cliente,
        valor=valor,
        descricao=descricao,
        aceito=aceito
    )

    db.add(transaction_db)
    db.commit()

    return jsonify({'aceito': aceito})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)