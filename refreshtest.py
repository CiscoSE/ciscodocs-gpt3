import utils

api_key = utils.getApiKey("./config.json")

utils.deleteAllFiles(api_key)

print(utils.file2jsonl("./sources/DNA_datasheet.txt", "./docs/DNA_test.jsonl"))

file_id = utils.uploadFile("./docs/DNA_test.jsonl", api_key)

with open("./file_id", "w") as file:
    file.write(file_id)