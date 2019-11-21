with open("input.txt", "w") as file1:

    file1.write((input("What is the question?\n") + "\n"))
    file1.write(str(input("The correct answer is?\n") + "\n"))
    file1.write(str(input("Fake answer 1 is?\n") + "\n"))
    file1.write(str(input("Fake answer 2 is?\n") + "\n"))
    file1.write(str(input("Fake answer 3 is?\n") + "\n"))

file1.close()
