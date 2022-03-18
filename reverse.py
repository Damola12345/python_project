# python program
# command line arguments
## reverse vowel in an argument


a   =input()
l   =""

# this is taking out and storing the vowels 
for i in a:
    if i in 'aeiouAEIOU':
        l+=i
        
new_a = ""
# this is reversing the vowels 
for k in a:
    if k in "aeiouAEIOU":
        new_a += l[-1]
        l = l[:-1] # everything except the last one items
    else:
        new_a+=k
print(new_a)




    






























