def binary_search(list,item):
    low=0
    high=len(list)-1

    while low<=high:
        mid=(low+high)//2
        guess=list[mid]
        if guess==item:
            return mid
        if guess>item:
            high=mid-1
        else:
            low=mid+1
    return None

my_list=[1,3,5,7,9]
print(binary_search(my_list,5))
print(binary_search(my_list,-1))


def findsmallest(arr):
    samllest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i]<samllest:
            smallest=arr[i]
            smallest_index=1
    return smallest_index

def selectionsort(arr):
    newarr=[]
    for i in range(len(arr)):
        smallest=findsmallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr

print(selectionsort([5,3,6,2,10]))

def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)

print(factorial(3))


graph={}
graph["you"]=["alice","bob","claire"]
graph["bob"]=["anuj","peggy"]
graph["alice"]=["peggy"]
graph["claire"]=["thom","jonny"]
graph["anuj"]=[]
graph["peggy"]=[]
graph["thom"]=[]
graph["jonny"]=[]

from collections import deque


def search(name):
    search_queue=deque()
    search_queue+=graph[name]
    searched=[]
    while search_queue:
        person=search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person+" is a mango seller")
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False

def person_is_seller(name):
    return name[-1]=='m'

search("you")