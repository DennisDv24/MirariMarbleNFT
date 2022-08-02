from brownie import MiraiMarble
from brownie import accounts, network, config
from scripts.deploy_and_mint import get_acc, from_me, deploy_token
from web3 import Web3

GAS_PRICE = Web3.toWei(30, 'gwei')

def estimate_gas():
    gas = MiraiMarble.deploy.estimate_gas(from_me)
    eth_price = Web3.fromWei(gas * GAS_PRICE, 'ether')
    print(f'Gas cost: {gas}')
    print(f'Current apx price for this contract: {eth_price}')
    token = deploy_token()
    gas = token.mintNewMarble.estimate_gas(get_acc(), '', from_me)
    eth_price = Web3.fromWei(gas * GAS_PRICE, 'ether')
    print(f'Gas cost: {gas}')
    print(f'Current apx price for this contract: {eth_price}')
    

def main():
    estimate_gas()
