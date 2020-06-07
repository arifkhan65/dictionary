person={'name': 'ab', 'age': 50}
person['car']= 'audi'
print(person)
person1={'name': 'abc', 'age': 50,'mobile':'samsung', 'number':5}
person.update(person1)
print(person)
del person ['age']
print(person)
print('age' in person1)
n=int(input('input a number: '))
d=dict()
for x in range (1,n+1):
    d[x]=x*x
print(d)
y=int(sum(d.values()))
print(y)

z=1
for i in d:
    z=z*d[i]
print(z)
x5=input('I want to delete: ')
del person1[x5]
print(person1)
a=['food','cloth','home']
b=['basic','need','human']
c=zip(b,a)
d=dict(c)
print(d)