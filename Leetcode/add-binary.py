a = "11"
b = "1"

dec_a = 0
for each in a:
    dec_a = 2 * dec_a + int(each)
print(dec_a)
dec_b = 0
for each in b:
    dec_b = 2 * dec_b + int(each)
print(dec_b)
dec_sum = dec_a + dec_b

list1 = []
while dec_sum != 0:
    remain = dec_sum % 2
    dec_sum = dec_sum // 2
    list1.append(remain)
list1 = list1[: : -1]
ans = "".join(str(each) for each in list1)
print(ans)