import re

def parser(d):
    """
    Receives a dictionary and parse to fit the
    structure necessary for the database.

    Returns: (aceito, estabelecimento, cliente, valor, descricao)
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