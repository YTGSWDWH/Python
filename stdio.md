## 一行输入（字符串）
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
  read_list = list(map(int, input().split()))
  l1.append(read_list)
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
