# lab 2

string1 = "   this is a string.  "
string2 = "  this is another string.  "

print("----2.2----")
string3=string1+string2 
print(string3)

print("----2.3----")
print(len(string1))
print(len(string2))
print("----")
print(string1.title())
print(string2.title())
print("----")
print(string1.lower())
print(string2.lower())
print("----")
print(string1.upper())
print(string2.upper())
print("----")
print(string1.lstrip())
print(string2.lstrip())
print("----")
print(string1.rstrip())
print(string2.rstrip())
print("----")
print(string1.strip())
print(string2.strip())
print("----")
print(string1.strip(' '))
print(string2.strip(' '))

print("----2.4----")
d = "qwerty"
ch = d[2]
print (ch)

print("----2.5----")
chm = d[1:3]
print(chm)

print("----2.6----")
chmm = d[:]
print(chmm)

print("----2.7----")
a=int (27)
b=int(33)
c= a // 10 
print(c)

print("----2.8----")
param = "string" + str(15)
print(param)

print("----2.9----")
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)

print("----2.10----")
a = 1/3
print("{:7.3f}".format(a))

print("----2.11----")
a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))
