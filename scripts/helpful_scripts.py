from ape import accounts, networks, project

from web3 import Web3


DECIMALS = 8
STARTING_PRICE = 2000

PRICE_FEEDS = {
    "sepolia": "0x694AA1769357215DE4FAC081bf1f309aDC325306",
    "mainnet": "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419",
}

def get_Account():
    # Verifica si estamos en una red local/development
    if networks.active_provider.network.name in ["local", "development"] or "anvil" in networks.active_provider.name.lower():
        return accounts.test_accounts[0]
    else:
        # Para redes reales, carga tu cuenta
        return accounts.load("miCuenta")

def get_price_feed():
    """Devuelve el contrato de price feed adecuado."""
    network_name = networks.active_provider.network.name.lower()

    # Si es una red de desarrollo, desplegamos el Mock
    if "local" in network_name or "development" in network_name or "anvil" in networks.active_provider.name.lower():
        account = get_Account()
        mock = project.MockV3Aggregator.deploy(DECIMALS, Web3.to_wei(STARTING_PRICE, "ether"), sender=account)
        return mock.address
    else:
        # Si es una red real, usamos el diccionario
        return PRICE_FEEDS.get(network_name, PRICE_FEEDS["sepolia"])