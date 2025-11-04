from ape import project
from scripts.helpful_scripts import get_Account
from scripts.deploy import deploy_fund_me

def get_contract():
    """
    Obtiene el contrato FundMe. Si no existe, lo despliega.
    """
    if len(project.FundMe.deployments) > 0:
        print(f"📋 Using existing deployment at {project.FundMe.deployments[-1].address}")
        return project.FundMe.deployments[-1]
    else:
        print("📋 No deployment found, deploying new contract...")
        return deploy_fund_me()

def fund():
    """
    Envía fondos al contrato FundMe.
    """
    fund_me = get_contract()
    account = get_Account()
    entrance_fee = fund_me.getEntranceFee()
    
    print(f"💰 Entrance fee: {entrance_fee / 1e18:.6f} ETH")
    print(f"   Funding contract...")
    
    tx = fund_me.fund(sender=account, value=entrance_fee)
    
    print(f"✅ Funded! Transaction: {tx.txn_hash}")
    print(f"   Amount funded by {account.address}: {fund_me.addressToAmountFunded(account.address) / 1e18:.6f} ETH")

def withdraw():
    """
    Retira fondos del contrato FundMe (solo owner).
    """
    fund_me = project.FundMe.deployments[-1]
    account = get_Account()
    
    balance_before = account.balance
    contract_balance = fund_me.balance
    
    print(f"💸 Withdrawing {contract_balance / 1e18:.6f} ETH from contract...")
    
    tx = fund_me.withdraw(sender=account)
    
    balance_after = account.balance
    
    print(f"✅ Withdrawn! Transaction: {tx.txn_hash}")
    print(f"   Account balance change: {(balance_after - balance_before) / 1e18:.6f} ETH")
    print(f"   Contract balance: {fund_me.balance / 1e18:.6f} ETH")
    
def main():
    fund()
    withdraw()