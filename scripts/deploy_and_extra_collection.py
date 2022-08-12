from brownie import MarbleFactory, MirariMarbleCollection
from brownie import network, config, accounts
from scripts.deploy_factory import DEPLOYER_TEST_ADDR, CLIENT_TEST_ADDR, MIRARI_ADDR
from scripts.deploy_factory import deploy_to_testnet, get_acc

META_ARWEAVE_MANIFEST_HASH = 'vYYPN3MKBa7oojy7chE0AcIv0IkNJQ2hvlqLHf_aHwk'
META_BASE_URI = f'https://arweave.net/{META_ARWEAVE_MANIFEST_HASH}/'
META_BASE_NAME = 'MMHonorary'
META_EXT = '.json'
TOTAL_TOKENS = 12

format_uri_id = lambda i: i if len(str(i)) > 1 else f'0{i}'

get_uri = lambda i: (
    f'{META_BASE_URI}{META_BASE_NAME}{format_uri_id(i)}{META_EXT}'
)

def test_minting_extra_tokens(collection_addr):
    collection = MirariMarbleCollection.at(collection_addr)
    collection.transferOwnership(
        DEPLOYER_TEST_ADDR, {'from': CLIENT_TEST_ADDR}
    )
    for i in range(TOTAL_TOKENS):
        collection.mintNewMarble(
            CLIENT_TEST_ADDR, get_uri(i), {'from': DEPLOYER_TEST_ADDR}
        )
    tx = collection.transferOwnership(
        CLIENT_TEST_ADDR, {'from': DEPLOYER_TEST_ADDR}
    )
    tx.wait(1)

def deploy_to_testnet_full_test():
    deploy_to_testnet()
    colle_tx = MarbleFactory[-1].deployMainCollection({'from': CLIENT_TEST_ADDR})
    colle_tx.wait(1)
    new_colle = input('Introduce new collection addr: ')
    test_minting_extra_tokens(new_colle)



def mint_extra_tokens_in_mainnet():
    collection = MirariMarbleCollection[-1]
    print('Using this token:')
    print(collection)
    input('Is it correct?')
    for i in range(TOTAL_TOKENS):
        collection.mintNewMarble(
            MIRARI_ADDR, get_uri(i), {'from': get_acc()}
        )
    input('New tokens minted, continue?')
    tx = collection.transferOwnership(
        MIRARI_ADDR, {'from': get_acc()}
    )
    tx.wait(1)

def main():
    mint_extra_tokens_in_mainnet()


