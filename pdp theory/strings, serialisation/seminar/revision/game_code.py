import yaml
import json

with open("game.yaml", "r") as file:
    easy_mode_data = yaml.safe_load(file)

#extract
intro_msg = easy_mode_data['easy_mode']['intro']
lives = easy_mode_data['easy_mode']['lives']
questions = easy_mode_data['easy_mode']['questions']
exit_msg = easy_mode_data['easy_mode']['exit_message']

print("\n",intro_msg.upper())
print("\nNumber of lives:", lives)

for i, q_data in enumerate(questions, start=1):
    print(f"\nHere is your Question {i}:", q_data['question'])
    user_ans = input("Enter your answer: ")

    if user_ans == q_data['answer']:
        print("Well done, you are right")
    else:
        print(f"Wrong ans, ans is {q_data['answer']} ")
        lives -= 1
        print("Remaining Lives:", lives)
        if lives == 0:
            print("\nYou ran out of lives. Game over")
            break

print("\n",exit_msg.upper())

'''with open("sample.yml", "r") as file:
    yaml_file = yaml.safe_load(file)

with open("sample.json", "w") as json_file:
    json.dump(yaml_file, json_file)

with open("sample.json", "r") as json_file:
    sample_json = json.load(json_file)

print(sample_json)'''