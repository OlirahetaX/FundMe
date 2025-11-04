from ape import accounts, networks, project

from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 2000

PRICE_FEEDS = {
    "sepolia": "0x694AA1769357215DE4FAC081bf1f309aDC325306",
    "mainnet": "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419",
}

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["local", "development", "anvil", "hardhat", "foundry", "mainnet-fork", "sepolia-fork"]
    
def get_Account():
    """
    Devuelve una cuenta de test para redes locales o la cuenta real para redes públicas.
    """
    network_name = networks.active_provider.network.name.lower()
    provider_name = networks.active_provider.name.lower()
    
    # Si estamos en una red local o de desarrollo
    if any(env in network_name or env in provider_name for env in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
        print(f"🔧 Using test account on {network_name}")
        return accounts.test_accounts[0]
    else:
        # Para redes reales, carga tu cuenta
        print(f"🔑 Loading account for {network_name}")
        return accounts.load("miCuenta")

def is_local_network():
    """
    Verifica si estamos en una red local.
    """
    network_name = networks.active_provider.network.name.lower()
    provider_name = networks.active_provider.name.lower()
    
    return any(env in network_name or env in provider_name for env in LOCAL_BLOCKCHAIN_ENVIRONMENTS)
    
def get_price_feed():
    """
    Devuelve el contrato de price feed adecuado.
    - Para redes locales: despliega un MockV3Aggregator
    - Para redes públicas: usa la dirección del price feed real
    """
    if is_local_network():
        print("📡 Deploying mock price feed for local network...")
        account = get_Account()
        
        # Verifica si ya existe un mock deployado
        if len(project.MockV3Aggregator.deployments) > 0:
            mock = project.MockV3Aggregator.deployments[-1]
            print(f"✅ Using existing mock at {mock.address}")
            return mock.address
        
        # Despliega un nuevo mock
        # STARTING_PRICE en USD con 8 decimales (ej: 2000 * 10^8)
        initial_price = STARTING_PRICE * (10 ** DECIMALS)
        mock = project.MockV3Aggregator.deploy(
            DECIMALS, 
            initial_price, 
            sender=account
        )
        print(f"✅ Mock deployed at {mock.address}")
        return mock.address
    else:
        # Red pública - usa el price feed real
        network_name = networks.active_provider.network.name.lower()
        price_feed_address = PRICE_FEEDS.get(network_name, PRICE_FEEDS["sepolia"])
        print(f"📡 Using real price feed at {price_feed_address}")
        return price_feed_address