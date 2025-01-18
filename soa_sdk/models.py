from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class Credentials(BaseModel):
    email: str
    password: str   

class SaldoRequest(BaseModel):
    credenciais: Credentials

    def dict(self, *args, **kwargs):
        original_dict = super().dict(*args, **kwargs)
        return {
            "Credenciais": {
                "Email": original_dict['credenciais']['email'],
                "Senha": original_dict['credenciais']['password']
            }
        }   

class ExtratoSinteticoRequest(BaseModel):
    credenciais: Credentials
    ano: int
    mes: int

class ExtratoAnaliticoRequest(BaseModel):
    credenciais: Credentials
    ano: int
    mes: int
    dia: int

class CNHRequest(BaseModel):
    credenciais: Credentials
    cnh_frente: str
    cnh_verso: str

class PessoaFisicaNFeRequest(BaseModel):
    credenciais: Credentials
    documento: str
    data_nascimento: Optional[str]

class PessoaJuridicaNFeRequest(BaseModel):
    credenciais: Credentials
    documento: str

class ProcessosRequest(BaseModel):
    credenciais: Credentials
    documento: str
    destino: str

class KycRequest(BaseModel):
    credenciais: Credentials
    documento: str
    telefone: str
    data_nascimento: datetime
    cep: str
    logradouro_numeral: int