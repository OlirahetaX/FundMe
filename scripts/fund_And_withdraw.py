from ape import project
from scripts.helpful_scripts import get_Account

from web3 import Web3

def fund():
    fund_me = project.FundMe.deployments[-1]
    account = get_Account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print("funding")
    fund_me.fund(sender=account, value=Web3.to_wei(0.0001,"ether"))

def withdraw():
    fund_me = fund_me = project.FundMe.deployments[-1]
    account = get_Account()
    print("Withdrawing")
    fund_me.withdraw(sender=account)
    
def main():
    fund()
    withdraw()
