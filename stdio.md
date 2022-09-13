## 一行输入
#### 两个字符串
```python
a, b = input().split()
```
#### 多个字符串
```python
l1 = list(input().split())
```
#### 两个数字
```python
a, b = map(int, input().split())
```
#### 多个数字
```python
l1 = list(map(int, input().split()))
```
## 多行输入
#### 行数已知
```python
n = int(input())
l1 = []
for _ in range(n):
  l1.append(list(map(int, input().split()))) （扩充到原列表则使用extend）
```
#### 行数未知
```python
l1 = []
while 1:
  s = input()
  if s != "":
    l1.append(list(map(int, s.split())))
  else:
    break
```
#### 生成排列，列表中得元素不允许重复出现
```python
from itertools import permutations
ans = list(permutations(list1))
```
#### 生成排列，列表中得元素可以重复出现
```python
from itertools import product
ans = list(product(list1, repeat=len(list1))
```
#### 生成组合，列表中的元素不允许重复出现
```python
from itertools import combinations
ans = list(combinations(list1, i)
```
#### 生成组合，列表中的元素可以重复出现
```python 
from itertools import product
ans = list(product(list1, repeat=i)
```
