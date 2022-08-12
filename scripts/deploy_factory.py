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
ask_for_verify = lambda x: input(f'Should verify {x}? y/N: ').lower() == 'y'

def local_deploy():
    factory = MarbleFactory.deploy(
        {'from': get_acc('test1')},
         publish_source=ask_for_verify('MarbleFactory')
    )
    input('Factory deployed, continue?')
    tx = factory.transferOwnership(get_acc(), {'from': get_acc('test1')})
    tx.wait(1)
    tx = factory.deployMainCollection({'from': get_acc()})
    tx.wait(1)

DEPLOYER_TEST_ADDR = get_acc('test1')
CLIENT_TEST_ADDR = get_acc()

def deploy_to_testnet():
    factory = MarbleFactory.deploy(
        {'from': DEPLOYER_TEST_ADDR},
         publish_source=ask_for_verify('MarbleFactory')
    )
    input('Factory deployed, continue?')
    tx = factory.transferOwnership(CLIENT_TEST_ADDR, {'from': DEPLOYER_TEST_ADDR})
    tx.wait(1)

# Deploy factory from dev-acc, transferOwnership to mirari
def deploy_to_production():
    factory = MarbleFactory.deploy(
        {'from': get_acc()},
         publish_source=ask_for_verify('MarbleFactory')
    )
    input('Factory deployed, continue?')
    tx = factory.transferOwnership(MIRARI_ADDR, {'from': get_acc()})
    tx.wait(1)


def main():
    deploy_to_testnet()
    #deploy_to_production()

