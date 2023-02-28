from web3 import Web3
w3 = Web3(Web3.HTTPProvider("https://eth.llamarpc.com/"))
abi = '[{"inputs":[{"internalType":"uint256","name":"i","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"nonpayable","type":"function"}]'
def getNFTownerERC721(contractAddress, tokenId):
    contract = w3.eth.contract(
        address=contractAddress,
    abi=abi
    )
    return contract.functions.ownerOf(tokenId).call()
