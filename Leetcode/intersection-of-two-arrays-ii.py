def intersect(nums1, nums2):
    list1 = []
    len1 = len(nums1)
    len2 = len(nums2)
    len_min = min(len1, len2)
    if len_min == len1:
        for i in range(len1):
            if nums1[i] in nums2:
                list1.append(nums1[i])
                nums2.remove(nums1[i])
    else:
        for i in range(len2):
            if nums2[i] in nums1:
                list1.append(nums2[i])
                nums1.remove(nums2[i])
    return list1

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1, nums2))