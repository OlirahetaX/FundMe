# FundMe - Proyecto Blockchain con Ape

Proyecto de aprendizaje para interactuar con la blockchain usando Ape Framework, Chainlink Price Feeds y Anvil/Foundry para desarrollo local.

## 🛠️ Instalación

### 1. Instalar dependencias de Python

```bash
pip install eth-ape
pip install ape-solidity
pip install ape-foundry
pip install python-dotenv
```

### 2. Instalar Foundry (incluye Anvil)

```bash
curl -L https://foundry.paradigm.xyz | bash
foundryup
```

### 3. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
ETHERSCAN_API_KEY=tu_api_key_aqui
```

### 4. Compilar contratos

```bash
ape compile
```

## 🚀 Uso

### Desarrollo Local con Anvil

Anvil es más rápido que Hardhat y viene con Foundry. Es perfecto para desarrollo y testing.

**Iniciar Anvil:**

```bash
anvil
```

En otra terminal, despliega el contrato:

```bash
ape run deploy --network ethereum:local:foundry
```

**Funding y Withdraw:**

```bash
ape run fund_And_withdraw --network ethereum:local:foundry
```

**Ejecutar tests:**

```bash
ape test --network ethereum:local:foundry
```

### Despliegue en Sepolia

**1. Crear cuenta en Ape:**

```bash
ape accounts import miCuenta
```

Sigue las instrucciones y guarda tu private key de forma segura.

**2. Desplegar:**

```bash
ape run deploy --network ethereum:sepolia
```

**3. Funding y Withdraw:**

```bash
ape run fund_And_withdraw --network ethereum:sepolia
```

## 📁 Estructura del Proyecto

```
ape_fund_me/
├── contracts/
│   ├── FundMe.sol           # Contrato principal
│   └── test/
│       └── MockV3Aggregator.sol  # Mock para testing
├── scripts/
│   ├── deploy.py            # Script de despliegue
│   ├── fund_And_withdraw.py # Interacción con el contrato
│   └── helpful_scripts.py   # Utilidades
├── tests/
│   └── test_fund_me.py      # Tests automatizados
├── ape-config.yaml          # Configuración de Ape
└── .env                     # Variables de entorno
```

## 🔍 Características

- **Chainlink Price Feeds**: Obtiene el precio de ETH/USD en tiempo real
- **Mínimo de financiación**: 50 USD en ETH
- **Owner Controls**: Solo el owner puede retirar fondos
- **Testing automatizado**: Tests con pytest
- **Mock Contracts**: Para desarrollo local sin necesidad de oráculos reales

## 📝 Comandos Útiles

### Testing

```bash
# Ejecutar todos los tests
ape test

# Ejecutar tests en verbose
ape test -v

# Ejecutar un test específico
ape test tests/test_fund_me.py::test_can_fund_and_withdraw
```

### Console interactiva

```bash
# Console local
ape console --network ethereum:local:foundry

# Console en Sepolia
ape console --network ethereum:sepolia
```

### Ver información de la red

```bash
ape networks list
```

## 🎯 Ventajas de Anvil vs Hardhat

1. **Velocidad**: Anvil es significativamente más rápido
2. **Integración**: Parte del ecosistema Foundry
3. **Forking**: Forkea mainnet/testnet fácilmente
4. **Sin dependencias JS**: Todo en Rust
5. **Mejor performance**: Menos consumo de recursos

## 🔗 Resources

- [Ape Framework Docs](https://docs.apeworksuite.io/)
- [Foundry Book](https://book.getfoundry.sh/)
- [Chainlink Price Feeds](https://docs.chain.link/data-feeds/price-feeds/addresses)
- [Sepolia Faucet](https://sepoliafaucet.com/)

## ⚠️ Notas Importantes

- Nunca subas tu `.env` al repositorio
- Guarda tus claves privadas de forma segura
- En Sepolia, necesitas ETH de prueba (usa faucets)
- El contrato requiere mínimo 50 USD en ETH para financiar
