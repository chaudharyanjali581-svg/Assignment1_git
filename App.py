#Question 1
with open("demo.txt","r") as f:
    data=f.read()
    print(data)

#Question 2
#mymod.py(module)
def countlines(filename):
    with open(filename,'r') as f:
        return len(f.readlines())

def countchars(filename):
    with open(filename,'r') as f:
        return len(f.read())

def test(filename):
    print(f"lines:{countlines(filename)}")
    print(f"characters:{countchars(filename)}")

#sample.txt(file)

"""hello,this is test file.
it has multiple lines.
python is fun"""

#main.py
import mymod
mymod.test('sample.txt')

#Question 3
from mymod import countlines,countchars,test
filename='sample.txt'
test(filename)


from mymod import *
filename='sample.txt'
test(filename)

#Question 4
#mymod.py(added a line)
if __name__=="__main__":
    filename="sample.txt"
    test(filename)

#main.py
import mymod

#Question 5
#myclient.py(module)
import mymod
fname=input("enter filename:")
mymod.test(fname)


from mymod import*
fname=input("enter filename:")
test(fname)

#Question 6
#mypkg(mymod.py)
from mypkg import mymod
fname =input("enter filename:")
mymod.test(fname)


#Question 7
with open("demo.txt","r") as f:
    line=f.readline()
    print(line)

#Question 8
with open("demo.txt","a") as f:
    f.write("this is new line")
    print(f.write)

#Question 9
with open("demo.txt","r") as f:
    line=f.readlines()
    print(line)

#Question 10
with open("demo.txt", "r") as f:
    for line in f:
        reversed_line = line.strip()[::-1]
        print(reversed_line)

#Question 11
l=["it","is","file","read"]
with open("demo.txt","w") as f:
    for i in l:
        f.write(i+"\n")

#Question 12
with open("demo.txt","r") as f:
    file=f.readlines()
n_lines=len(file)
n_words=0
n_chars=0
for i in file:
    n_chars+=len(i)
    n_words+=len(i.split())
print("number of lines:",n_lines)
print("number of words:",n_words)
print("number of characters:",n_chars)

#Question 13
with open("demo.txt","w") as f:
    while True:
        s=input("enter a sentence(type 'END' to stop):")
        if s=="END":
            break
        f.write(s+"\n")

print("\nSentences starting with an uppercase letter:")
with open("demo.txt", "r") as f:
    for line in f:
        if line and line[0].isupper():
            print(line.strip())

#Question 14
import pickle

n=int(input("enter number of records:"))
with open("items.txt","wb") as f:
    for i in range(n):
        item_no=int(input("enter item no:"))
        item_name=input("enter item name:")
        qty=int(input("enter quantity:"))
        price=float(input("enter price:"))
        record=[item_no,item_name,qty,price]
        pickle.dump(record,f)

print("\nStored Records:\n")
with open("items.txt","rb") as f:
    while True:
        try:
            item_no,item_name,qty,price=pickle.load(f)
            amount=qty*price
            print(f"item no:{item_no}")
            print(f"item name:{item_name}")
            print(f"quantity:{qty}")
            print(f"price:{price}")
            print(f"amount:{amount}\n")
        except EOFError:
            break









    
