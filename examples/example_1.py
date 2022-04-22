"""
Example no.1
============

Just an example.

AUTHOR
    mgpai22@GitHub

CREATED AT
    Wed. 20 Apr. 2022 23:43
"""
# Import `ergpy`
from ergpy import helper_functions, appkit

# Create connection to the blockchain
node_url: str = "http://213.239.193.208:9052/" # MainNet or TestNet
ergo = appkit.ErgoAppKit(node_url=node_url)

# Wallet mnemonic
wallet_mnemonic = ""

# (optional) If you have a mnemonic password
# mnemonicPassword = "my password" 

"""
Note how the following parameters are inputed :
- In simple send, 3WwdX would get 0.22 ERG, 3WwuG9 would get 0.33 ERG, 3Wxk5o would get 0.11 ERG
- In token send, 3WwdX would get 0.22 ERG and tokens A, B, C, 3WwuG9 would get 0.33 ERG and token D and so on
"""
receiver_addresses = [
    "3WwdXmYP39DLmDWJ6grH9ArXbWuCt2uGAh46VTfeGPrHKJJY6cSJ",
    "3WwuG9amNVDwkJdgT5Ce7aJCfeoafVmd9tag9AEiAZwgPi7pYX3w",
    "3Wxk5oofZ3Laq2CpFW4Fi9YQiaep9bZr6QFg4s4xpzz4bi9tZq2U"
]

amount = [0.22, 0.33, 0.11]

tokens = [
    ["tokenID_A", "tokenID_B", "tokenID_C"],
    ["tokenID_D"],
    ["tokenID_E", "tokenID_F"]
]

nftName = "pythonWrapper NFT"
description = "created by MGpai's python wrapper"
imageLink = "ipfs://bafkreihvadi66kddokso7x2i4kmqjhj5e3j44rn347i7drghekr2mfw3nu"
imageHash = appkit.sha256caster("f500d1ef286372a4efdf48e299049d3d26d3ce45bbe7d1f1c4c722a3a616db6d")


"""
base64 reduced transactions are also possible, the only current problem is the boxes are preselected so
if another tx gets processed before submitting the base64 tx, it will not go through.
Just add the `base64reduced=True` to get this

Example
-------
```
print(helperMethods.simpleSend(ergo=ergo,
    amount=amount,
    walletMnemonic=wallet_mnemonic,
    receiverAddresses=receiver_addresses,
    base64reduced=True
))
````
Note
----
    Specifying `senderAddress` is also possible. Once specified, the boxes will be selected from this address and change
    will be sent here as well. Make sure the prover index is specified as well (same index as address derivation).

"""
# print(helper_functions.getWalletAddress(ergo=ergo, amount=5, walletMnemonic=wallet_mnemonic))
# print(helper_functions.getBoxInfo(ergo=ergo, index=0, senderAddress=receiver_addresses[0]))
# print(helper_functions.simpleSend(ergo=ergo, amount=amount, walletMnemonic=wallet_mnemonic, receiverAddresses=receiver_addresses))
# print(helper_functions.sendToken(ergo=ergo, amount=amount, receiverAddresses=receiver_addresses, tokens=tokens, walletMnemonic=wallet_mnemonic))
# print(helper_functions.createToken(ergo=ergo, tokenName=nftName, description=description, tokenAmount=1, tokenDecimals=0, walletMnemonic=wallet_mnemonic))
# print(helper_functions.createNFT(ergo=ergo, nftName=nftName, description=description, imageLink=imageLink, imageHash=imageHash, walletMnemonic=wallet_mnemonic))