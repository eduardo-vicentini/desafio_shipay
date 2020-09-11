#!/usr/bin/python3
# coding: UTF-8

import unittest

from helpers import parser, identificacao_valida

class Tests(unittest.TestCase):

    json = {
        "estabelecimento": "402.198.033-00", 
        "cliente": "402.198.033-00", 
        "valor": 10,
        "descricao": "Teste"
    }

    estabelecimento_invalido = '000.000'
    cliente_invalido = '000.000'
    valor_invalido = 'aa'
    
    def test_parser_estabelecimento_invalido(self):
        """Teste para estabelecimento invalido"""
        json = dict(self.json)
        json['estabelecimento'] = self.estabelecimento_invalido
        data = parser(json)

        self.assertEqual(self.estabelecimento_invalido, data[1])
        self.assertFalse(data[0])
    
    def test_parser_cliente_invalido(self):
        """Teste para cliente invalido"""
        json = dict(self.json)
        json['cliente'] = self.cliente_invalido
        data = parser(json)

        self.assertEqual(self.cliente_invalido, data[2])
        self.assertFalse(data[0])

    def test_parser_valor_invalido(self):
        """Teste para valor invalido"""
        json = dict(self.json)
        json['valor'] = self.valor_invalido
        data = parser(json)

        self.assertEqual(0, data[3])
        self.assertFalse(data[0])

    def test_parser_estabelecimento_vazio(self):
        """Teste para nota sem estabelecimento"""
        json = dict(self.json)
        del json['estabelecimento']
        data = parser(json)

        self.assertEqual('-', data[1])
        self.assertFalse(data[0])

    def test_parser_cliente_vazio(self):
        """Teste para nota sem cliente"""
        json = dict(self.json)
        del json['cliente']
        data = parser(json)

        self.assertEqual('-', data[2])
        self.assertFalse(data[0])

    def test_parser_valor_vazio(self):
        """Teste para nota sem valor"""
        json = dict(self.json)
        del json['valor']
        data = parser(json)

        self.assertEqual(0, data[3])
        self.assertFalse(data[0])

    def test_parser_descricao_vazia(self):
        """Teste para nota sem descricao"""
        json = dict(self.json)
        del json['descricao']
        data = parser(json)

        self.assertEqual('-', data[4])
        self.assertFalse(data[0])


if __name__ == "__main__":
    unittest.main()