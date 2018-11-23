# 题目
# 给定一个整数数组，判断是否存在重复元素。
# 如果任何值在数组中出现至少两次，函数应该返回 true。如果每个元素都不相同，则返回 false。

# 集合查找，判断元素是否重复
# 先排序操作，再遍历，查看元素是否重复
# set，集合中不包含重复的元素
# ？？？可以用hash，统计每个数目的数量即可，找出出现一次的数。
class Solution:
    def contain_duplicates(self,arr):
        """
        :type arr: list[int]
        :rtypr: boolean
        """
        length=len(arr)
        i=0
        while i<length-1:
            k=arr[i]
            j=i
            while j<length-1:
                j+=1
                if k==arr[j]: 
                    break
            if k==arr[j]: 
                break
            i+=1
        if i==length-1:
            print(arr)
            return False
        else:
            print(arr[j])
            return True
        
    def contain_duplicates_set(self,arr):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(arr)) == len(arr):
            return False
        else:
            return True

if __name__=="__main__":
    test=Solution()
    arr=[1,2,2,4,5]
    # test.contain_duplicates(arr)
    test.contain_duplicates_set(arr)

