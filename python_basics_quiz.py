# creating a list to hold all the questions
questions = [
    "What is the correct file extension for a Python file?",
    "Which keyword is used to define a function in Python?",
    "What will print(type(5)) output?",
    "Which of the following is a valid variable name in Python?",
    "What does the len() function do?",
    "Which symbol is used for comments in Python?",
    "What will print(10 // 3) output?",
    "Which data type is used to store True or False values?",
    "What is the output of print(\"Hello\" + \"World\")?",
    "Which function is used to take input from the user in Python?"
]

# a list to hold the options to the questions respectively
options =[
    "a) .py b) .pt c) .python d) .pyt",
    "a) func b) define c) def d) function",
    "a) <class 'float'> b) <class 'int'> c) <class 'str'> d) <class 'bool'>",
    "a) 2name b) name_2 c) name-2 d) @name",
    "a) Adds numbers b) Counts characters/items c) Converts type d) Prints output",
    "a) // b) /* */ c) # d) --",
    "a) 3.33 b) 3 c) 4 d) 10",
    "a) int b) float c) bool d) str",
    "a) Hello World b) HelloWorld c) Hello+World d) Error",
    "a) scan() b) read() c) input() d) get()"
]

# an answer key list to hold correct responses to all the questions
correct_options =[
    'a',
    'c',
    'b',
    'b',
    'b',
    'c',
    'b',
    'c',
    'b',
    'c'
]

points = 0 # initializing a points variable to hold the total points 

for i in range(10):
    choice = ''
    print(i+1,'.',questions[i])
    print(options[i])
    choice = input("Enter your choice: ").lower().strip()
    if choice == correct_options[i]:
        points +=1

print()
print("Your total points are:",points)
