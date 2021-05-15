# results=[]
# def maker():
#     while True:
#         say_something=input('Say something: ')
#         if say_something == "\end":
#             break
#         else:
#             results.append(sentence_maker(say_something))

#     print(" ".join(results))

# def sentence_maker(phrase):
#     interrogatives=("How","What","Why","When","Who")
#     capitalized=phrase.capitalize()
#     if capitalized.startswith(interrogatives):
#         return "{}?".format(capitalized)
#     else:
#         return "{}.".format(capitalized)
 

# maker()

# def foo(*args):
#     lst=[arg.upper() for arg in args]
#     lst.sort()
#     return lst

# print(foo('aaa','bb','ddd','ccc'))

# def foo(filepath):
#     with open(filepath) as myfile:
#         content=myfile.read()
#         return content

# print(foo("fruits.txt").count('a'))


# def foo(char,filepath):
#     with open(filepath) as file:
#         content=file.read()
    
#     print(content.count(char))    

# foo('e',"fruits.txt")


# with open("fruits.txt",'a+') as file:
#     file.seek(0,0)
#     content=file.read()
#     file.write(content)
#     file.seek(0,0)
#     file.write(content)

# import time
# import pandas

# while True:
#     with open("fruits.txt", "") as file:
#         file.seek(0)
#         content = file.read()
#         file.write('\n')
#         file.write(content)
#         time.sleep(5)
        
import pandas 
import time
import os

while True:
    if os.path.exists("temps_today.csv"):
        with open("temps_today.csv") as file:
            data=pandas.read_csv(file)
            print(data.mean())
    else:
        print('file not found')
    time.sleep(10)
