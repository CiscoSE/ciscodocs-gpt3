import utils

api_key = utils.getApiKey("./config.json")

print(utils.deleteAllFiles(api_key))