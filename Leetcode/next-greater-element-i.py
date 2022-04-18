def nextGreaterElement(nums1, nums2):
    left = 0
    list1 = []
    while left < len(nums1):
        right = 0
        while right < len(nums2)-1:
            if nums2[right] == nums1[left]:
                for i in range(right+1, len(nums2)):
                    if nums2[i] > nums1[left]:
                        list1.append(nums2[i])
                        break
            right = right + 1
        print(right)
        if right == len(nums2)-1:
            list1.append(-1)
        left = left + 1
    return list1

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))