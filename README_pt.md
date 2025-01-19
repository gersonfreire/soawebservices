# SOA WebServices SDK

[🇺🇸 English Version](README.md)

Um SDK e CLI em Python para interagir com a API do SOA WebServices ([Site do SOAWebservices](https://www.soawebservices.com.br/))

## Instalação

1. Clone o repositório
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente no [.env](vscode-file://vscode-app/c:/Program%20Files/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html):

```
BASE_URL=https://homologacao.soawebservices.com.br
PROD_BASE_URL=https://services.soawebservices.com.br
EMAIL=<seu-usuario-sowawebservices>
PASSWORD=<sua-senha-sowawebservices>
```

## Onde gerenciar sua conta e obter as credenciais:

* [Portal SOAWebServices](https://portal.soawebservices.com.br/Identity/Login)
* [Site do SOAWebservices](https://www.soawebservices.com.br/)

## Uso

### Como Biblioteca

```python
from soa_sdk.client import SOAWebServicesClient

# Inicializar cliente
cliente = SOAWebServicesClient()

# Obter saldo da conta
saldo = cliente.get_saldo()

# Obter extrato sintético
extrato = cliente.get_extrato_sintetico(2023, 12)

# Obter informações de NFe para pessoa física
nfe = cliente.get_pessoa_fisica_nfe("12345678900", "1990-01-01")
```

### Usando o CLI

```bash
# Obter saldo da conta
soa-cli saldo

# Obter extrato sintético
soa-cli extrato-sintetico --ano 2023 --mes 12

# Obter informações de NFe para pessoa física
soa-cli pessoa-fisica-nfe --documento 12345678900 --data-nascimento 1990-01-01

# Obter informações de NFe para pessoa jurídica
soa-cli pessoa-juridica-nfe --documento 12345678000190
```

## Funcionalidades

- Cobertura completa da API
- Registro automático em arquivo e console
- Validação de tipos usando Pydantic
- Interface CLI rica
- Configuração baseada em ambiente

## Registro de Logs

Os logs são gravados em

soa_sdk.log

 e rotacionados quando atingem 10MB de tamanho. Os últimos 5 arquivos de log são mantidos.

## Tratamento de Erros

O SDK inclui tratamento de erros abrangente e registro de logs. Todos os erros da API são registrados e lançados como exceções.

## Referências:

[Status dos serviços](https://status.i-stream.com.br/status/servicos)

[Documentação Swagger da API](https://services.soawebservices.com.br/documentacao/index.html)

[Novo CNPJ](https://github.com/gersonfreire/novo-cnpj)

[Telegram Bot](https://t.me/PessoaBot)

## Como contribuir

1. Faça um fork do repositório
2. Crie uma nova branch (`git checkout -b feature-branch`)
3. Faça suas alterações
4. Faça commit das suas alterações (`git commit -m 'Adicionar nova funcionalidade'`)
5. Envie para a branch (`git push origin feature-branch`)
6. Abra um Pull Request

---
