flowerbed = [0,0,1,0]
n = 1

left = 0
right = 0
count = 0

if flowerbed[0] == 0:
    while flowerbed[right] != 1:
        right += 1
    count = (right - left) // 2 + count

    right = 0
while right < len(flowerbed)-1:
    while flowerbed[left] != 1:
        left += 1
    right  = left + 1
    while flowerbed[right] != 1 and right < len(flowerbed)-1:
        right += 1
    print(right)
    count = (right - left - 2) // 2 + count

    left = right
    right = left + 1
if flowerbed[len(flowerbed)-1] == 0:
    left = len(flowerbed) - 2
    while flowerbed[left] != 1:
        left = left - 1
    count = (len(flowerbed) - 1 - left) // 2 + count