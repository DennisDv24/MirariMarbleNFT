from brownie import MiraiMarble
from brownie import accounts, network, config
from scripts.deploy_and_mint import get_acc, from_me, deploy_token, MIRARI_ADDR
from web3 import Web3

EXAMPLE_URI = 'https://arweave.net/8avbVHlVIp5iS2pbCvDFhIZiSRPJnA4rt0YWINU0Jvo/MirariMarbleOG07.json'

GAS_PRICE = Web3.toWei(30, 'gwei')
gas_to_eth = lambda x: Web3.fromWei(x * GAS_PRICE, 'ether')


def estimate_gas():
    deploy_gas = MiraiMarble.deploy.estimate_gas(from_me)
    print(f'Deploy gas cost: {deploy_gas}')
    print(f'Current apx deployment price: {gas_to_eth(deploy_gas)} eth')
    token = deploy_token()
    mint_gas = token.mintNewMarble.estimate_gas(MIRARI_ADDR, EXAMPLE_URI, from_me)
    print(f'Mint gas cost: {mint_gas}')
    print(f'Current apx minting price: {gas_to_eth(mint_gas)} eth')
    print(f'10 mints price: {gas_to_eth(mint_gas) * 10} eth')
    ownership_gas = token.transferOwnership.estimate_gas(MIRARI_ADDR, from_me)
    print(f'Renouncement gas cost: {ownership_gas}')
    print(f'Current apx renouncement price: {gas_to_eth(ownership_gas)} eth')
    print(f'\nTotal estimation: {gas_to_eth(mint_gas * 10 + ownership_gas + deploy_gas)} eth')

    

def main():
    estimate_gas()
