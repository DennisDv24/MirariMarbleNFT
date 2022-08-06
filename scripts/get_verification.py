import json
from brownie import MirariMarbleCollection

def main():
    with open('Registry.json', 'w') as f:
        f.write(
            json.dumps(
                MirariMarbleCollection.get_verification_info()['standard_json_input']
            )
        )
