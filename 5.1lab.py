'''n= int(input("Введите кол-во слов:"))
long = " "
for i in range (n):
    word = input (f"Введите слово {i+1}:")
    long += word + " "
print ("Строка: ", long)'''

'''word = " "
long = " "
while word != "стоп":
    word = input ("Введите слово (стоп - завершает) : ")
    if word!= "стоп" :
        long += word + " "
if long =="стоп":
    print ("Держи строку:", long)
else:
    print("Пусто")'''

'''while True:
    word = input ("Введите слово (стоп - завершает) : ")
    if word.lower() == "стоп":
        break
    if "ф" in word.lower():
        print ('Ого! Это редкое слово!')
    else:
        print ('Эх, это не очень редкое слово...')'''

import random
prav_answer = 0
neprav_answer = 0

while neprav_answer < 3:
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    answer = input (f"{num1} + {num2} = ")
    if answer.isdigit():
        if int(answer) == num1 + num2 :
            print("правильно")
            prav_answer +=1
        else:
            print("неправильно")
            neprav_answer +=1
    else:
        print("введи число")
        neprav_answer +=1
print(f"Игра закончена. Правильных ответы : {prav_answer}")