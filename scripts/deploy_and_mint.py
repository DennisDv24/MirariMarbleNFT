from brownie import MiraiMarble
from brownie import accounts, network, config


LOCAL_ENVS = ['development', 'ganache']

URI_0 = "ar://j-vjjM_X0Gfx9dnbca70iR4wALflrD_mAUK67uFKlTs"

def get_acc():
    if network.show_active() in LOCAL_ENVS:
        return accounts[0]
    return accounts.add(config['wallets']['from_key'])

def deploy():
    acc = get_acc()
    token = MiraiMarble.deploy({'from': acc})
    print(f'You have: {token.balanceOf(acc)} tokens')
    tx = token.mintNewMarble(
        acc,
        URI_0,
        {'from': acc}
    )
    tx.wait(1)
    print(f'You have: {token.balanceOf(acc)} tokens')

def main():
    deploy()
