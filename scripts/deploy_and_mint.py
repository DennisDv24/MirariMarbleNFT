from brownie import MiraiMarble
from brownie import accounts, network, config


MIRARI_ADDR = '0xbb884cfc40c40a7bafc12f54d4d511406f3969cf'

LOCAL_ENVS = ['development', 'ganache']

META_BASE_URI = 'https://arweave.net/8avbVHlVIp5iS2pbCvDFhIZiSRPJnA4rt0YWINU0Jvo/'


META_BASE_NAME = 'MirariMarbleOG0'
ITERATIONS = 10

get_acc = lambda: accounts[0] if (
    network.show_active() in LOCAL_ENVS
) else accounts.add(config['wallets']['from_key'])

from_me = {'from': get_acc()}

should_verify = config['networks'][network.show_active()].get('verify', False)

deploy_token = lambda: MiraiMarble.deploy(from_me, publish_source = should_verify)

def mint_tokens_with(mint_function):
    input('Continue?')
    for i in range(ITERATIONS):
        input('Continue?')
        mint_function(
            MIRARI_ADDR,
            f'{META_BASE_URI}{META_BASE_NAME}{i}.json',
            from_me
        )
    


def deploy():
    mint_tokens_with(deploy_token().mintNewMarble)
    input('All minted, transfer ownerhisp?')
    MiraiMarble[-1].transferOwnership(MIRARI_ADDR, from_me).wait(1)

def main():
    deploy()
