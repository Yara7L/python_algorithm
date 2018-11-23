def num_ways(n):
    if (n<=10):
        if(n==0):   return 0
        elif(n==1):
            return 0
        elif(n==2):
            return 1
        else:
            print(num_ways(n-1)+num_ways(n-2)) 
    else:
        print("n已超出100")

a=0
def test(num):
    global l
    global a
    a=a+1
    if num==0 or num==1:
        return 1
    if num>1:
        if l[num-2]==0:
            l[num-2] = test(num-2)
            return test(num-2) + test(num-1)
        return test(num-1)+l[num-2]
    return 0
num = 8
l = [int(k-k) for k in range(num)]
print(test(num))
print(a)

# if __name__=="__main__":
#     num_ways(3)
#     climbstairs(3)