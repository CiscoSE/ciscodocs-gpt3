import utils

api_key = utils.getApiKey("./config.json")

print(utils.uploadFile("./docs/DNA_test.jsonl", api_key))