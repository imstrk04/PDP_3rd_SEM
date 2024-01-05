# importing yaml
import yaml

#load easy mode details from YAML File
with open("game.yaml", "r") as file:
    easy_mode_data = yaml.safe_load(file)

#Extract easy mode data
intro = easy_mode_data['easy_mode']['intro']
lives = easy_mode_data['easy_mode']['lives']
questions = easy_mode_data['easy_mode']['questions']
exit_msg = easy_mode_data['easy_mode']['exit_message']



print(intro.upper())
print("Number of lives:", lives)

for i, q_data in enumerate(questions, start=1):
    print(f"Question {i}: {q_data['question']}")
    user_ans = input("Enter your ans: ").lower()

    if user_ans == q_data['answer']:
        print("Well done, right ans")
    else:
        print(f"Wrong ans, ans is {q_data['answer']}")
        lives -= 1
        print("Lives Left:", lives)
        if lives == 0:
            print("Ran out of lives, game over")

print(exit_msg.upper())
