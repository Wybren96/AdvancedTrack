import random
asked_data = open("input.txt", "r")

new_list = [line.rstrip() for line in asked_data.readlines()]

print(new_list[0] + '\n')
correct_answer = new_list[1]

question_list = new_list[1:]

randomized_list = random.sample(question_list, 4)

for i in randomized_list:
    print(i)

print('\n')
answer = input("What is your answer?:\n")

if answer == correct_answer:
    print("Good Job!")
else: print("False!")