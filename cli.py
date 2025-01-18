from types import NoneType
import click
from datetime import datetime
from rich.console import Console
from rich.table import Table
from soa_sdk.client import SOAWebServicesClient

console = Console()

@click.group()
def cli():
    """SOA WebServices CLI"""
    pass

@cli.command()
def saldo():
    """Get account balance"""
    client = SOAWebServicesClient()
    result = client.get_saldo()
    # result = client.get_balance_rest()
    
    table = Table(title="Account Balance")
    table.add_column("Saldo")
    table.add_row(str(result.get('Saldo', 'N/A')))
    console.print(table)

@cli.command()
@click.option('--ano', type=int, required=True, help='Year')
@click.option('--mes', type=int, required=True, help='Month')
def extrato_sintetico(ano: int, mes: int):
    """Get synthetic statement"""
    client = SOAWebServicesClient()
    result = client.get_extrato_sintetico(ano, mes)
    
    table = Table(title="Synthetic Statement")
    table.add_column("Total Quantity")
    table.add_column("Total Value")
    table.add_row(
        str(result.get('ConsumoQuantidadeTotal', 'N/A')),
        str(result.get('ConsumoValorTotal', 'N/A'))
    )
    console.print(table)

@cli.command()
@click.option('--documento', required=True, help='Document number')
@click.option('--data-nascimento', help='Birth date (YYYY-MM-DD)')
def pessoa_fisica_nfe(documento: str, data_nascimento: str):
    """Get NFe information for individual"""
    client = SOAWebServicesClient()
    result = client.get_pessoa_fisica_nfe(documento, data_nascimento)
    
    table = Table(title="Individual NFe Information")
    table.add_column("Field")
    table.add_column("Value")
    
    for key, value in result.items():
        if isinstance(value, (str, int, float, NoneType)):
            table.add_row(key, str(value))
    
    console.print(table)

@cli.command()
@click.option('--documento', required=True, help='Document number')
def pessoa_juridica_nfe(documento: str):
    """Get NFe information for company"""
    client = SOAWebServicesClient()
    result = client.get_pessoa_juridica_nfe(documento)
    
    table = Table(title="Company NFe Information")
    table.add_column("Field")
    table.add_column("Value")
    
    for key, value in result.items():
        if isinstance(value, (str, int, float)):
            table.add_row(key, str(value))
    
    console.print(table)

cli.add_command(pessoa_fisica_nfe, name='pessoafisicanfe')

if __name__ == '__main__':
    cli()
