# SOA WebServices SDK

A Python SDK and CLI for interacting with SOA WebServices API.

References:

* [Services status](https://status.i-stream.com.br/status/servicos)
* [API Swagger docs](https://services.soawebservices.com.br/documentacao/index.html)

* https://portal.soawebservices.com.br/Identity/Login
* https://www.soawebservices.com.br/

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables in `.env`:

```
BASE_URL=https://services.soawebservices.com.br
EMAIL=your_email
PASSWORD=your_password
LOG_LEVEL=INFO
```

## Usage

### As a Library

```python
from soa_sdk.client import SOAWebServicesClient

# Initialize client
client = SOAWebServicesClient()

# Get account balance
balance = client.get_saldo()

# Get synthetic statement
statement = client.get_extrato_sintetico(2023, 12)

# Get NFe information for individual
nfe = client.get_pessoa_fisica_nfe("12345678900", "1990-01-01")
```

### Using the CLI

```bash
# Get account balance
soa-cli saldo

# Get synthetic statement
soa-cli extrato-sintetico --ano 2023 --mes 12

# Get NFe information for individual


# Get NFe information for company
soa-cli pessoa-juridica-nfe --documento 12345678000190
```

## Features

- Complete API coverage
- Automatic logging to file and console
- Type validation using Pydantic
- Rich CLI interface
- Environment-based configuration

## Logging

Logs are written to `logs/soa_sdk.log` and rotated when they reach 10MB in size. The last 5 log files are kept.

## Error Handling

The SDK includes comprehensive error handling and logging. All API errors are logged and raised as exceptions.
