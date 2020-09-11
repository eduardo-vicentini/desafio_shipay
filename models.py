#!/usr/bin/python3
# coding: UTF-8

from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.types import Boolean, DateTime, Float, Integer, String

from database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    estabelecimento = Column(String, default='-')
    cliente = Column(String, default='-')
    valor = Column(Float, default=0)
    descricao = Column(String, default='-')
    aceito = Column(Boolean)
    created_at = Column(DateTime, default=datetime.now)