# FundMe - Blockchain Crowdfunding Contract

A decentralized crowdfunding smart contract built with Solidity, using the Ape Framework for development and testing. This project integrates Chainlink Price Feeds to handle ETH/USD conversions and uses Anvil/Foundry for local blockchain development.

## 🎯 Features

- **Chainlink Price Feeds**: Real-time ETH/USD price conversion
- **Minimum Funding**: Enforces a $50 USD minimum contribution in ETH
- **Owner Controls**: Only the contract owner can withdraw funds
- **Automated Testing**: Comprehensive test suite with pytest
- **Mock Contracts**: Local development without real oracles
- **Mainnet Fork Support**: Test with real mainnet data locally

## 🛠️ Tech Stack

- **Smart Contracts**: Solidity ^0.8.19
- **Framework**: Ape (eth-ape)
- **Local Blockchain**: Anvil (Foundry)
- **Price Oracles**: Chainlink
- **Testing**: pytest
- **Networks**: Local, Sepolia Testnet, Mainnet Fork

## 📋 Prerequisites

- Python 3.8+
- Node.js (optional, for some dependencies)
- Git

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/fundme-ape.git
cd fundme-ape
```

### 2. Install Python dependencies

```bash
pip install eth-ape
pip install ape-solidity
pip install ape-foundry
pip install python-dotenv
```

### 3. Install Foundry (includes Anvil)

```bash
curl -L https://foundry.paradigm.xyz | bash
foundryup
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
ETHERSCAN_API_KEY=your_api_key_here
```

### 5. Compile contracts

```bash
ape compile
```

## 📁 Project Structure

```
fundme-ape/
├── contracts/
│   ├── FundMe.sol              # Main crowdfunding contract
│   └── test/
│       └── MockV3Aggregator.sol # Mock oracle for testing
├── scripts/
│   ├── deploy.py               # Deployment script
│   ├── fund_And_withdraw.py    # Interaction script
│   └── helpful_scripts.py      # Utility functions
├── tests/
│   └── test_fund_me.py         # Automated tests
├── ape-config.yaml             # Ape configuration
├── .env                        # Environment variables (create this)
└── README.md
```

## 💻 Usage

### Local Development with Anvil

Anvil is faster than Hardhat and comes with Foundry - perfect for development and testing.

**Start Anvil:**

```bash
anvil
```

**In another terminal, deploy the contract:**

```bash
ape run deploy --network ethereum:local:foundry
```

**Fund and withdraw:**

```bash
ape run fund_And_withdraw --network ethereum:local:foundry
```

**Run tests:**

```bash
ape test --network ethereum:local:foundry
```

### Mainnet Fork Testing

Test with real mainnet data without spending real ETH:

**Start Anvil with mainnet fork:**

```bash
anvil --fork-url https://eth-mainnet.g.alchemy.com/v2/YOUR_ALCHEMY_KEY
```

**Deploy on fork:**

```bash
ape run deploy --network ethereum:mainnet-fork:foundry
```

### Deployment to Sepolia Testnet

**1. Create an Ape account:**

```bash
ape accounts import myAccount
```

Follow the prompts and securely save your private key.

**2. Get Sepolia ETH:**

Use a faucet: https://sepoliafaucet.com/

**3. Deploy:**

```bash
ape run deploy --network ethereum:sepolia
```

**4. Interact with the contract:**

```bash
ape run fund_And_withdraw --network ethereum:sepolia
```

## 🧪 Testing

### Run all tests

```bash
ape test
```

### Verbose output

```bash
ape test -v
```

### Run specific test

```bash
ape test tests/test_fund_me.py::test_can_fund_and_withdraw
```

### Test coverage

```bash
ape test --coverage
```

## 🔍 Key Functions

### FundMe Contract

- `fund()` - Send ETH to the contract (minimum $50 USD equivalent)
- `withdraw()` - Owner-only function to withdraw all funds
- `getEntranceFee()` - Calculate minimum ETH required for $50 USD
- `getConversionRate(uint256 ethAmount)` - Convert ETH amount to USD
- `getPrice()` - Get current ETH/USD price from Chainlink

## 📊 Network Configuration

The project supports multiple networks configured in `ape-config.yaml`:

- **Local**: Development with Anvil/Foundry
- **Sepolia**: Ethereum testnet
- **Mainnet Fork**: Local fork of Ethereum mainnet

Price feed addresses:
- Sepolia: `0x694AA1769357215DE4FAC081bf1f309aDC325306`
- Mainnet: `0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419`

## 🎮 Interactive Console

### Local console

```bash
ape console --network ethereum:local:foundry
```

### Sepolia console

```bash
ape console --network ethereum:sepolia
```

### Example commands in console

```python
# Get deployed contract
fund_me = project.FundMe.deployments[-1]

# Check entrance fee
entrance_fee = fund_me.getEntranceFee()
print(f"Entrance fee: {entrance_fee / 1e18} ETH")

# Fund the contract
account = accounts.test_accounts[0]
fund_me.fund(sender=account, value=entrance_fee)

# Check balance
balance = fund_me.addressToAmountFunded(account.address)
print(f"Funded: {balance / 1e18} ETH")
```

## 🔗 Useful Commands

### View available networks

```bash
ape networks list
```

### View accounts

```bash
ape accounts list
```

### View deployments

```bash
ape deployments list
```

## ⚡ Advantages of Anvil vs Hardhat

1. **Speed**: Significantly faster transaction processing
2. **Integration**: Part of the Foundry ecosystem
3. **Forking**: Easy mainnet/testnet forking
4. **No JS dependencies**: Built in Rust
5. **Better performance**: Lower resource consumption
6. **State management**: Advanced state manipulation features

## 🔐 Security Notes

- ⚠️ Never commit your `.env` file
- 🔑 Store private keys securely (use Ape accounts, not raw keys)
- 🧪 Always test on testnet before mainnet deployment
- 💰 The contract requires minimum $50 USD in ETH to fund
- 👤 Only the owner can withdraw funds

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📚 Resources

- [Ape Framework Documentation](https://docs.apeworksuite.io/)
- [Foundry Book](https://book.getfoundry.sh/)
- [Chainlink Price Feeds](https://docs.chain.link/data-feeds/price-feeds/addresses)
- [Sepolia Faucet](https://sepoliafaucet.com/)
- [Solidity Documentation](https://docs.soliditylang.org/)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/fundme-ape](https://github.com/yourusername/fundme-ape)

## 🙏 Acknowledgments

- Patrick Collins for the original FundMe concept
- Chainlink for the decentralized oracle network
- ApeWorX team for the amazing development framework
- Foundry team for Anvil and the Foundry suite

---

⭐ If you found this project helpful, please give it a star!
