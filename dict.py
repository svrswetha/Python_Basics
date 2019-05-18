dic = {}

lists = []

dic[1] = "Yes"
dic['1'] = "No"

print(dic[1])


print(dic['1'])

class my_class:
    def __init__(self):
        self.data= "data"

instance = my_class()

dic['object'] = instance
print(dic['object'].data)

print(dic.keys())

print(dic.items())

print(dic)

class_names = ["jack","bob","mary","jeff","ann","pierre","martha","clause","pablo","susan","gustav"]

def create_dataset():
    import random
    num_entries = 500000
    f = open("data.txt","w")
    for i in range(num_entries):
        current = random.choice(class_names)
        f.write(current+"\n")
    f.close()


def read_dataset_list():
    class_counts = []
    for c in class_names:
        class_counts.append(0)
    with open("data.txt") as f:
        for line in f:
            line = line.strip()
            if line !="":
                class_counts[class_names.index(line)]+=1
    print(class_counts)

def read_dataset_dict():
    class_counts = {}
    for c in class_names:
        class_counts[c] = 0
    with open("data.txt") as f:
        for line in f:
            line = line.strip()
            if line != "":
                class_counts[line] +=1
    print(class_counts)

import  time
t0 = time.time()
create_dataset()
t1 = time.time()
print("Data Set Creation time %0.1f seconds\n"%(t1-t0))

t00 = time.time()
read_dataset_list()
t11 = time.time()
print("Reading the dataset by list time %0.1f seconds"%(t11-t00))

t000 = time.time()
read_dataset_dict()
t111 = time.time()
print("Reading the dataset by dic time taken %0.1f seconds"%(t111-t000))

