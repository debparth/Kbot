import requests
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

cid = input("Enter Kahoot Challenge ID: ")

response = requests.get("http://kahoot.it/rest/challenges/" + cid + "/answers")

save = open(dir_path + "\kahoot.json", "w+", encoding="cp437", errors="ignore")
save.write(response.text)
save.close()

with open(dir_path + "\kahoot.json") as response:
    kahoot_json = json.load(response)
    result = open(dir_path + "\kahoot_answer.txt", "w+", encoding="cp437", errors="ignore")
    result.write(" _   __      _                 _  \n| | / /     | |               | | \n| |/ /  __ _| |__   ___   ___ | |_\n|    \ / _` | '_ \ / _ \ / _ \| __/\n| |\  \ (_| | | | | (_) | (_) | | \n\_| \_/\__,_|_| |_|\___/ \___/ \__|\n\n\nBy Parth Mehta\n")

    count = 0

    for questions in kahoot_json["answers"]:
        result.write("Question " + str(count+1) + ": " + questions["question"]["title"] + "\n")
        for answers in questions["question"]["choices"]:
            if answers["correct"] == True:
                result.write("Answer: " + answers["answer"] + "\n")
        count += 1

response.close()
result.close()
print("Done!!")
os.startfile("kahoot_answer.txt")
os.remove("kahoot.json")