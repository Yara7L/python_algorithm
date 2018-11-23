# _*_ coding:utf-8 _*_
# 冒泡排序：重复走访要排序的数列，一次比较两个元素。
def bubble_sort(lists):
    '''冒泡排序'''
    print("bubble sort :==========\n")
    count=len(lists)
    flag=True
    for i in range(0,count):
        flag=False
        for j in range(i+1,count):
            if lists[i]>lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
                flag=True
        print(lists)
        if flag==False: 
            break
    print(lists)
    return lists

# 选择排序：每次找出最小的元素，直至排序完毕
def select_sort(lists):
    '''选择排序'''
    count=len(lists)
    for i in range(0,count):
        min=i
        for j in range(i+1,count):
            if lists[min]>lists[j]:
                min=j
        lists[min],lists[i]=lists[i],lists[min]
        print(lists)
    return lists

# 插入排序：将一个数据插入已排好序（从后向前扫描）的里面，稳定的。
def insert_sort(lists):
    '''插入排序'''
    print("insert sort:=======\n")
    count=len(lists)
    # for i in range(1,count):
    #     key=lists[i]
    #     j=i-1
    #     while j>=0:
    #         if lists[j]>key:
    #             lists[j+1]=lists[j]
    #             lists[j]=key
    #         j=j-1
    #     print(lists)
    # print(lists)

    for i in range(1,count):
        if lists[i]<lists[i-1]:
            key=lists[i]
            index=i #待插入的下标
            for j in range(i-1,-1,-1): #i-1，循环到0
                if lists[j]>key:
                    lists[j+1]=lists[j]
                    index=j  #记录待插入的下标
                else:
                    break
            lists[index]=key
        print(lists)
    return lists

# 希尔排序：递减增量排序，分组插入排序，不稳定，步长决定复杂度。
def shell_sort(lists):
    '''希尔排序'''
    print("shell_sort :============\n")
    count=len(lists)
    step=2
    group=count//step #初始步长
    while group>0:
        for i in range(0,group):#每一列进行插入排序
            j=i+group
            while j<count:
                k=j-group
                key=lists[j]
                while k>=0:
                    if lists[k]>key:
                        lists[k+group]=lists[k]
                        lists[k]=key
                    k=k-group
                j=j+group
            print(lists)
        group=group//step #重新设置步长
    return lists

# 归并排序，分治法，递归分解数组再合并数组，将已有序的子序列合并（先子序列有序，再使子序列间有序）
def merge(left, right):
    # 将两个有序数组left[]和right[]合并成一个大的有序数组
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    print(result)
    return result
def merge_sort(lists):
    # 归并排序
    if len(lists) <= 1:
        return lists
    num = int(len(lists) / 2) #二分分解
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right) #合并数组

# 快速排序：选择一个基数，分区，左小右大，左右区间再分区，进行快速排序。
def quick_sort(lists):
    return qsort(lists,0,len(lists)-1)
def qsort(lists,left,right):
    '''快速排序'''
    if left>=right:
        return lists
    key=lists[left]  #取最左边为基准数
    lp=left #左指针
    rp=right #右指针
    while lp<rp:
        while lp<rp and lists[rp]>=key:
            rp-=1
        lists[lp]=lists[rp]
        while lp<rp and lists[lp]<=key:
            lp+=1
        lists[rp]=lists[lp]
    lists[rp]=key
    print(lists)
    qsort(lists, left, lp - 1)
    qsort(lists, rp + 1, right)
    return lists

# 堆排序，二叉堆，top k问题，父节点大于等于子节点，每个节点左右子树都是二叉堆。
# 构造最大堆，堆排序，最大堆调整
'''
def adjust_heap(lists,i,size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)
def build_heap(lists, size):
    for i in range(0, (size/2))[::-1]:
        adjust_heap(lists, i, size)
def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
'''
def heap_sort(ary) :
    n = len(ary)
    first = int(n/2-1)       #最后一个非叶子节点
    for start in range(first,-1,-1) :     #构造大根堆
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):           #堆排，将大根堆转换成有序数组
        ary[end],ary[0] = ary[0],ary[end]
        max_heapify(ary,0,end-1)
    return ary
#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary,start,end):
    root = start
    while True :
        child = root*2 +1               #调整节点的子节点
        if child > end : break
        if child+1 <= end and ary[child] < ary[child+1] :
            child = child+1             #取较大的子节点
        if ary[root] < ary[child] :     #较大的子节点成为父节点
            ary[root],ary[child] = ary[child],ary[root]     #交换
            root = child
        else :
            break

# 基数排序，分配式排序，桶子法，稳定排序，时间复杂度为O (nlog(r)m)，其中r为所采取的基数，而m为堆数，
import math
def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            bucket[j/(radix**(i-1)) % (radix**i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists

if __name__=="__main__":
    a=[6,1,5,3,2,4]
    bubble_sort(a)
    insert_sort(a)
    shell_sort(a)
    select_sort(a)
    merge_sort(a)
    quick_sort(a)


