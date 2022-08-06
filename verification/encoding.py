# NOTE you should use web3js encoding or directly get the ABI args from
# the deployed contract bytecode. Also, see ../scripts/get_verification.py
# to get SIJ for factory deployed contract verification

arg1 = 'Mirari Marble'
arg2 = 'MM'

get_hex = lambda s: s.encode('utf-8').hex()
add_zeros = lambda s: ('0' * (257 - len(s))) + s

print('ABI encoded ARGS:')
print(add_zeros(get_hex(arg1)) + add_zeros(get_hex(arg2)))

