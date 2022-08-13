from brownie import MirariMarbleCollection
from brownie import accounts
from scripts.deploy_factory import get_acc, MIRARI_ADDR

META_PREFIX = 'https://arweave.net/'
URI_1 = 'mdgytwnJbGH_DrF72dwBcjvRufXppdA3vOt6SEYyt0A'
URI_2 = 'pCdBvNJ3F4t0DOjnUoA2r9dmpKP4ECqR7evM0L2JU0Y'

def testnet_mint():
    colle = MirariMarbleCollection[-1]
    print(colle)
    input('Right collection?')
    acc = get_acc()
    print(acc)
    input('Right account?')
    print('Minting extra 2 tokens')
    colle.mintNewMarble(
        acc, f'{META_PREFIX}{URI_1}', {'from': acc}
    )
    tx = colle.mintNewMarble(
        acc, f'{META_PREFIX}{URI_2}', {'from': acc}
    )
    tx.wait(1)

def mainnet_mint():
    colle = MirariMarbleCollection[-1]
    print(colle)
    input('Right collection?')
    acc = get_acc()
    print(acc)
    input('Right account?')
    print('Minting extra 2 tokens')
    colle.mintNewMarble(
        MIRARI_ADDR, f'{META_PREFIX}{URI_1}', {'from': acc}
    )
    colle.mintNewMarble(
        MIRARI_ADDR, f'{META_PREFIX}{URI_2}', {'from': acc}
    )
    input('Minting complete, transfer ownership back?')
    tx = colle.transferOwnership(MIRARI_ADDR, {'from': acc})
    tx.wait(1)

def main():
    mainnet_mint()


