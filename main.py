import utils
import os

with open("./file_id", "r") as file:
    file_id = file.read()

api_key = utils.getApiKey("./config.json")

os.system("cls")
question_text = ""
while (question_text != "/q"):
    question_text = input("Please ask a question (type /q to quit): ")
    if question_text == "/q":
        continue
    print(utils.answerQuestion(question_text, file_id, api_key))
    print("\n")

os.system("cls")