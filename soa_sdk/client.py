import os
from typing import Dict, Any, Optional
from datetime import datetime
import requests
from dotenv import load_dotenv
from .logger import setup_logger
from .models import *

class SOAWebServicesClient:
    
    def __init__(self):
        load_dotenv()
        self.logger = setup_logger(__name__)
        self.base_url = os.getenv('BASE_URL')
        self.credentials = Credentials(
            email=os.getenv('EMAIL'),
            password=os.getenv('PASSWORD')
        )     
        
        if not all([self.base_url, self.credentials.email, self.credentials.password]):
            raise ValueError("Missing required environment variables")

    def _make_request(self, endpoint: str, data: Dict[str, Any], endpoint_url: str = None) -> Dict[str, Any]:
        """Make HTTP request to the API."""
        
        url = f"{self.base_url}{endpoint}" if not endpoint_url else endpoint_url
        
        self.logger.info(f"Making request to {url}")
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            self.logger.info(f"Request to {endpoint} successful")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed: {str(e)}")
            raise

    def get_saldo(self) -> Dict[str, Any]:
        """Get account balance."""
        
        endpoint = "/api/v2/Administracao/Saldo"
        
        # Endpoint de saldo só existe em ambiente de produção        
        prod_base_url =  os.getenv('PROD_BASE_URL')
        endpoint_url = f"{prod_base_url}{endpoint}"
        
        data = SaldoRequest(credenciais=self.credentials).dict()      
        
        return self._make_request(endpoint, data, endpoint_url)

    def get_extrato_sintetico(self, ano: int, mes: int) -> Dict[str, Any]:
        """Get synthetic statement."""
        endpoint = "/api/v2/Administracao/ExtratoSintetico"
        data = ExtratoSinteticoRequest(
            credenciais=self.credentials,
            ano=ano,
            mes=mes
        ).dict()
        return self._make_request(endpoint, data)

    def get_extrato_analitico(self, ano: int, mes: int, dia: int) -> Dict[str, Any]:
        """Get analytical statement."""
        endpoint = "/api/v2/Administracao/ExtratoAnalitico"
        data = ExtratoAnaliticoRequest(
            credenciais=self.credentials,
            ano=ano,
            mes=mes,
            dia=dia
        ).dict()
        return self._make_request(endpoint, data)

    def analyze_cnh(self, cnh_frente: str, cnh_verso: str) -> Dict[str, Any]:
        """Analyze CNH documents."""
        endpoint = "/api/v2/AI/CNH"
        data = CNHRequest(
            credenciais=self.credentials,
            cnh_frente=cnh_frente,
            cnh_verso=cnh_verso
        ).dict()
        return self._make_request(endpoint, data)

    def get_pessoa_fisica_nfe(self, documento: str, data_nascimento: Optional[str] = None) -> Dict[str, Any]:
        """Get NFe information for individual."""
        endpoint = "/api/v2/CDC/PessoaFisicaNFe"
        data = PessoaFisicaNFeRequest(
            credenciais=self.credentials,
            documento=documento,
            data_nascimento=data_nascimento
        ).dict()
        return self._make_request(endpoint, data)

    def get_pessoa_juridica_nfe(self, documento: str) -> Dict[str, Any]:
        """Get NFe information for company."""
        endpoint = "/api/v2/CDC/PessoaJuridicaNFe"
        data = PessoaJuridicaNFeRequest(
            credenciais=self.credentials,
            documento=documento
        ).dict()
        return self._make_request(endpoint, data)

    def get_processos(self, documento: str, destino: str) -> Dict[str, Any]:
        """Get legal processes."""
        endpoint = "/api/v2/Juridica/Processos"
        data = ProcessosRequest(
            credenciais=self.credentials,
            documento=documento,
            destino=destino
        ).dict()
        return self._make_request(endpoint, data)

    def validate_kyc(self, documento: str, telefone: str, data_nascimento: datetime,
                    cep: str, logradouro_numeral: int) -> Dict[str, Any]:
        """Validate KYC information."""
        endpoint = "/api/v2/Telcos/Kyc"
        data = KycRequest(
            credenciais=self.credentials,
            documento=documento,
            telefone=telefone,
            data_nascimento=data_nascimento,
            cep=cep,
            logradouro_numeral=logradouro_numeral
        ).dict()
        return self._make_request(endpoint, data)
