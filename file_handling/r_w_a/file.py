# reading ,writing , appending files in python
#reading a python file in the same dir 
"""f = open("msg.txt", "r")

content = f.read()
print(content)

f.close()"""



#writing to a python file in the same dir 
"""with open('py.txt', 'w') as f:
    f.write('python is awesome\n')
    f.write('love this language')"""


#append to a python file in the same dir 
with open('py.txt', 'a') as f:
    f.write('\npython is used for automation')




