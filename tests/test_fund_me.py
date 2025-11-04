from scripts.helpful_scripts import get_Account
from scripts.deploy import deploy_fund_me

def test_can_fund_and_withdraw():
    account = get_Account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund(sender=account, value = entrance_fee)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw(sender=account)
    assert fund_me.addressToAmountFunded(account.address) == 0