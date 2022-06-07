# coding=utf-8
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

print("---List---")
list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
print(dir(list))
help(list.insert)
help(list.append)
help(list.sort)
help(list.remove)
help(list.reverse)

list1[4] = 15
list1.append(22)
list1.insert(5,6)
list1.pop(len(list1)-1)
print(list1)

print("---SortList___")
list1.sort(reverse=True)
print(list1)

list2 = [3,5,6,2,33,6,11]
lis = sorted(list2)
print(list2)
print(lis)

print("---Tuple---")
print(dir(tuple))
help(tuple.index)
help(tuple.count)

seq = (2,8,23,97,92,44,17,39,11,12)
print(seq.count(8))
print(seq.index(44))
listseq = list(seq)
print(type(listseq))
print(listseq)
listseq.sort()
listseq.append(17)
print(listseq)

print("---Dictionary---")
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D['food'])
D['quantity'] += 10
print(D['quantity'])

dp = {}
dp['name'] = input('Name:')
dp['age'] = input('Age:')
print(dp)

print("---Data---")
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
 'job': ['dev', 'mgr'],
 'age': 25}

print(rec['name']['firstname'], ' ',rec['name']['lastname'])
print(rec['name']['firstname'])
print(rec['job'])
rec['job'].append('janitor')
print(rec)
