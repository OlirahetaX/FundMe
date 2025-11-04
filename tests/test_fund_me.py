from scripts.helpful_scripts import get_Account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from ape import networks, accounts
import pytest

def test_can_fund_and_withdraw():
    account = get_Account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund(sender=account, value = entrance_fee)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw(sender=account)
    assert fund_me.addressToAmountFunded(account.address) == 0
    
def test_only_owner_can_withdraw():
    if networks.active_provider.network.name.lower() not in [env.lower() for env in LOCAL_BLOCKCHAIN_ENVIRONMENTS]:
        pytest.skip("Only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts.test_accounts[1]
    with pytest.raises(Exception) as exc_info:
        fund_me.withdraw(sender=bad_actor)
    