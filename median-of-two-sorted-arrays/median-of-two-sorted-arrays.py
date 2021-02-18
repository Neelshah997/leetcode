class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = []
        i = 0
        j = 0
        while(i<len(nums1) and j<(len(nums2))):
            if nums1[i]<nums2[j]:
                temp.append(nums1[i])
                i+=1
            else:
                temp.append(nums2[j])
                j+=1
        while(i<len(nums1)):
            temp.append(nums1[i])
            i+=1
        while(j<len(nums2)):
            temp.append(nums2[j])
            j+=1
        print(temp)
        if len(temp)%2==0:
            return (temp[len(temp)//2]+temp[len(temp)//2-1])/2
        return temp[len(temp)//2]