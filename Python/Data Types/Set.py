set1={1,2,3,5,'Hello',23}
print(set1)

set1.add(2024)
print("After add:",set1)

set1.update([600,400])
print("After update:",set1)

set1.remove(600)
print("After remove:",set1)

set1.discard(50000)
print("After discard:",set1)

set1.pop()
print("After pop:",set1)

set1.clear()
print("After clear:",set1)

set2={10,20,"Hello",'Hello',30,40,10}
print("Set2:",set2)
print(type(set2))