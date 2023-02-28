from Scweet.scweet import scrape
from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers
from getNfInfo import get_nft_info
from getERC721 import getNFTownerERC721
from getERC1155 import getOwner
get_users_following(users=["@elonmusk"], env=".env", verbose=0,
                    headless=True,  wait=2, limit=1, file_path=None)
# for account in data:
#     nftInfo = get_nft_info("https://twitter.com" + account + '/nft')
#     if (nftInfo != False):
#         if (nftInfo[2] == "ERC1155"):
#             params = {
#                 "address": nftInfo[0],
#                 "token_id": nftInfo[1],
#                 "chain": "eth",
#                 "format": "decimal",
#                 "normalizeMetadata": True,
#             }
#             getOwner(params)
#         else:
#             getNFTownerERC721(nftInfo[0], nftInfo[1])
