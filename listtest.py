import utils

api_key = utils.getApiKey("./config.json")

print(utils.listFiles(api_key))