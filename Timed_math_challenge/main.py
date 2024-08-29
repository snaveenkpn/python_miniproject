import random
import time

MIN_VALUE = 3
MAX_VALUE = 12
OPERATOR = ["+", "-", "*"]
question = 10

def function():
    left_value = random.randint(MIN_VALUE, MAX_VALUE)

    right_value = random.randint(MIN_VALUE, MAX_VALUE)

    Operator = random.choice(OPERATOR)

    maths = str(left_value) + Operator + str(right_value)

    answer = eval(maths)

    return maths, answer

wrong = 0

start_time = time.time()

for i in range (question):

    maths, answer = function()
    

    while True:
        ques = input("what is the answer for "+ maths + ": ")
        if ques == str(answer):
            break
        wrong += 1

end_time = time.time()

total_time = round(end_time - start_time, 2)

print(f"Total time taken for completion {question} question was {total_time} seconds,  total wrong attempt was {wrong}"  )



    

