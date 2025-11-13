T=(5,'Hello',1+3j,10,35,10)
print(T[4])
print(type(T))

print(type(T[0]))
print(T.count(10))

#index method
print(T.index(1+3j))

print(type(T))
T=(10)
print(type(T))

t=(10,20,30,40,50)
temp=list(t)
temp.append(60)
t=tuple(temp)
print(t)

a=(10,20,30)
b=(40,50,60)
print(a+b)