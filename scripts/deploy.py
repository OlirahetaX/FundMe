from ape import project, networks

from scripts.helpful_scripts import get_Account, get_price_feed
from dotenv import load_dotenv

# Carga las variables de entorno del archivo .env
load_dotenv()

def deploy_fund_me():
    account = get_Account()
    price_feed = get_price_feed() 
    
    # Leer si la red debe verificar o no
    verify = False
    try:
        # Acceder a la configuración de la RED activa, no del ecosistema
        active_network = networks.active_provider.network
        print("Network name:", active_network.name)
        print("Ecosystem:", active_network.ecosystem.name)
        
        # Buscar en la configuración de networks del ape-config.yaml
        verify = active_network.config.get("verify", False)
        print("Verify:", verify)
    except (KeyError, AttributeError) as e:
        print(f"Error getting verify config: {e}")
        verify = False
    
    fund_me = project.FundMe.deploy(
        price_feed,
        sender=account,
        publish=verify
    )
    print(f"Contract deployed to: {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()