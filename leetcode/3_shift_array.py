# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

# 示例 1:
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]

# 示例 2:
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]

# 说明:
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的原地算法。

class Solution:
    def shift(self,arr,k):
        """
        :type arr:list[int]
        :type k:int
        """
        length=len(arr)
        if length<=1:
            print(arr[0])
            return length
        j=1
        if k>=0:
            while j<=k:
                i=length-1
                med=arr[-1]
                while i>=1:
                    arr[i]=arr[i-1]
                    i-=1
                arr[0]=med
                print("第{0}轮".format(j))
                for ii in range (0,length):
                    print(arr[ii])
                j+=1

    def rotate(self,arr,k):
        """
        :type arr:list[int]
        :type k:int
        """
        length=len(arr)
        # arr[:]=arr[-k:]+arr[:length-k] 
        arr[:]=arr[length-k:]+arr[:length-k] 
        print(arr)

    def convert(self,arr,start,end):
        k=0
        temp=0
        while k<(end-start+1)/2:
            temp = arr[start+k]
            arr[start+k] = arr[end-k]
            arr[end-k] = temp
            k+=1
        print(arr)

    def shift_convert(self,arr,k):
        self.convert(arr,0,len(arr)-1)
        self.convert(arr,0,k-1)
        self.convert(arr,k,len(arr)-1)
        print(arr)


if __name__=="__main__":
    arr=[1,2,3,4,5]
    k=2
    test=Solution()
    # test.shift(arr,k)  
    # test.rotate(arr,k)
    # test.convert(arr,0,4)
    test.shift_convert(arr,2)

