nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

nums1[m:] = nums2

""" for i, ch in enumerate(nums2):
    nums1[m+i] = ch """
nums1.sort()

print(nums1)