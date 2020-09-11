#!/usr/bin/python3
# coding: UTF-8

import re

def parser(d):
    """Recebe um dicionário e transforma para poder ser
    adicionado na base de dados.
    O input para correto funcionamento precisa ter:
    estabelecimento, cliente, valor e descrição.
    Também tem que ter os valores conforme a classe
    Transaction definido no models.py.

    Retorna (aceito, estabelecimento, cliente, valor, descricao).
    """
    aceito = True

    try:
        estabelecimento = d['estabelecimento']
    except KeyError:
        estabelecimento = '-'
        aceito = False

    try:
        cliente = d['cliente']
    except KeyError:
        cliente = '-'
        aceito = False
    
    try:
        valor = float(d['valor'])
    except (KeyError, ValueError):
        valor = 0
        aceito = False

    try:
        descricao = d['descricao']
    except KeyError:
        descricao = '-'
        aceito = False

    # Converter para a precisão correta
    valor = round(valor, 2)

    if aceito:
        aceito = identificacao_valida(cliente)
    if aceito:
        aceito = identificacao_valida(estabelecimento)

    return (aceito, estabelecimento, cliente, valor, descricao)


def identificacao_valida(num):
    """
    Testa se o número do cpf ou cnpj é válido.
    """
    num = re.sub('[\-./]', '', num)

    if len(num) == 11 or len(num) == 14:
        return True
    
    return False