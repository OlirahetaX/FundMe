from ape import project, networks
from scripts.helpful_scripts import get_Account, get_price_feed, is_local_network
from dotenv import load_dotenv

# Carga las variables de entorno del archivo .env
load_dotenv()

def deploy_fund_me():
    """
    Despliega el contrato FundMe.
    - En redes locales: no verifica en Etherscan
    - En redes públicas: verifica si está configurado
    """
    account = get_Account()
    price_feed = get_price_feed()
    
    # Determinar si debemos verificar el contrato
    verify = False
    if not is_local_network():
        try:
            active_network = networks.active_provider.network
            verify = active_network.config.get("verify", False)
            print(f"🔍 Verification {'enabled' if verify else 'disabled'} for {active_network.name}")
        except (KeyError, AttributeError) as e:
            print(f"⚠️  Error getting verify config: {e}")
            verify = False
    
    print(f"🚀 Deploying FundMe contract...")
    print(f"   Network: {networks.active_provider.network.name}")
    print(f"   Provider: {networks.active_provider.name}")
    print(f"   Account: {account.address}")
    print(f"   Price Feed: {price_feed}")
    
    fund_me = project.FundMe.deploy(
        price_feed,
        sender=account,
        publish=verify
    )
    
    print(f"✅ Contract deployed to: {fund_me.address}")
    print(f"   Minimum USD: 50")
    print(f"   Owner: {fund_me.owner()}")
    
    return fund_me


def main():
    deploy_fund_me()