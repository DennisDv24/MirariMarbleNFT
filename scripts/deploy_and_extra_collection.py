from brownie import MarbleFactory, MirariMarbleCollection
from brownie import network, config, accounts
from scripts.deploy_factory import DEPLOYER_TEST_ADDR, CLIENT_TEST_ADDR
from scripts.deploy_factory import deploy_to_testnet, get_acc

EXAMPLE_URI = ''

def test_minting_extra_tokens(collection_addr):
    collection = MirariMarbleCollection.at(collection_addr)
    collection.transferOwnership(
        DEPLOYER_TEST_ADDR, {'from': CLIENT_TEST_ADDR}
    )
    # NOTE in production it would be a loop that would
    # deploy a lot of new marbles, this is only
    # for testing if the opensea front-end ownership works 
    # right after multiple ownership transfers
    collection.mintNewMarble(CLIENT_TEST_ADDR, EXAMPLE_URI)
    collection.transferOwnership(
        CLIENT_TEST_ADDR, {'from': DEPLOYER_TEST_ADDR}
    )


def mint_extra_mainnet():
    pass

def main():
    deploy_to_testnet()
    colle = MarbleFactory[-1].deployMainCollection({'from': CLIENT_TEST_ADDR})
    test_minting_extra_tokens(colle)
    #deploy_to_production()
