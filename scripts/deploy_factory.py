from brownie import MarbleFactory
from brownie import network, config, accounts

LOCAL_ENVS = ['development', 'ganache']

def get_acc(wallet_name = None):
    if network.show_active() in LOCAL_ENVS: 
        return accounts[0]
    if wallet_name:
        return accounts.add(config['wallets'][wallet_name])
    return accounts.add(config['wallets']['from_key'])

MIRARI_ADDR = '0xbb884cfc40c40a7bafc12f54d4d511406f3969cf'

should_verify = config['networks'][network.show_active()].get('verify', False)


# Deploy factory from dev-acc, transferOwnership to mirari
def main():
    factory = MarbleFactory.deploy(
        {'from': get_acc('test1')},
         publish_source=should_verify
    )
    input('Factory deployed, continue?')
    tx = factory.transferOwnership(get_acc(), {'from': get_acc('test1')})
    tx.wait(1)
