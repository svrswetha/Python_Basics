a = []

print(a)
a = [1]

print(a)

a = [1,2,3]

print(a)
a = [1,"1"]
print(a)

a.append(4)
a.append(5)
a.append(6)

print(a)

a.insert(1,"2")

print(a)

a = [6,7,8]
b= [5,4,3]
b.extend(a)

print(b)

print(a[0:3])

print(a[:3])

print(a[3:])

print(a[:])

a[0] = 7
print(a)

ai = [1,2,3]

print(ai)
# Iterating over list
for ele in ai:
    print(ele)

print("same as above")
for i in range(len(ai)):
    print(ai[i])

bi = [4,5,6]
for elem_a, elem_b in zip(ai,bi):
    print("%d,%d"%(elem_a,elem_b))

print(ai)
del ai[0]
print(ai)
ai = [1,2,3,4]
# print(ai.pop())
print(ai)

print(ai.index(3))

# print(ai.index(5))

try:
    print(ai.index(5))
except:
    print("element not in list")

# Sorting

ai = [4,3,2,1]
print(ai)
ai.sort()
print(ai)


def f(x):
    return x**2
# b = [1,7,4,3,9]
# a =[f(x) for x in b]
# print(a)
a = [f(x) for x in range(10)]
print(a)

a = [1,2,3,4]
print(a)
a.reverse()
print(a)

a = [1,4,3,4]

print(a.count(4))

class example:
    def __init__(self):
        self.value = 10

a = []
for _ in range(10):
    new_examaple= example()
    a.append(new_examaple)

print(a)