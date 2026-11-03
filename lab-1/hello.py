## 1.3.1 Numbers

print(2 / 2)      # 1.0
print(2 / 3)      # 0.6666666666666666
print(2 // 3)     # 0
print(2 ** -1)    # 0.5


## 1.3.2 Strings

print(15 * "spam ")

str1 = """
This is a multi-line string.
It can span multiple lines.
"""

str2 = 'Han sa "Hej"'
str3 = "Han sa \"Hej\""

str4 = "Hello, world!"

print(str4[0:5])
print(str4[:5])
print(str4[-1])
print(len(str4))


## Strings är immutable
# str4[0] = "J"


## 1.3.3 Lists

a = [100, 1, 2, 3, 4, 5, 6, 7]

r = a
s = a[0:3]
t = a[:]

a[0] = 99

print(a) ## [99, 1, 2, 3, 4, 5, 6, 7]
print(r) ## [99, 1, 2, 3, 4, 5, 6, 7]
print(s) ## [100, 1, 2]
print(t) ## [100, 1, 2, 3, 4, 5, 6, 7]

print(len(a)) ## 8

m = [[1, 2], [3, 4]]
print(m[1][0]) ## 3


### 1.3.4 First steps
a = 5
b = 10
print(a, b) ## 5 10
a, b = b, a
print(a, b) ## 10 5

i = 1
while i <= 9:
    print(i)
    i += 1


## 1.4.1 If statements