def get_intger(help_text="give me a number:"):
    return int(input(help_text))


age = get_intger("give me your age: ")
grade = get_intger()

if age < 15:
    print(age)
    print("Your age is:" + str(age))
print("you are in grade:  " + str(grade))
