s = [int(x) for x in open('17.txt')]
ans = []
for i in range(len(s)):
    if s[i] % 3 == 0 and s[i] % 7 != 0 and s[i] % 17 != 0 and s[i] % 19 != 0 and s[i] % 27 != 0:
        ans.append(s[i])
print(len(ans), max(ans))

s = [int(x) for x in open('17 (1).txt')]
ans = []
for i in range(len(s)):
    if (s[i] % 10 == 2 or s[i] % 10 == 7) and s[i] % 3 == 0 and s[i] % 11 == 0:
        ans.append(s[i])
print(len(ans), min(ans))

s = [int(x) for x in open('17 (3).txt')]
ans = []
for i in range(len(s)):
    if (s[i] % 10 == 5 or s[i] % 10 == 7) and s[i] % 9 != 0 and s[i] % 11 != 0:
        ans.append(s[i])
print(len(ans), min(ans) + max(ans))

s = [int(x) for x in open('17 (4).txt')]
ans = []
for i in range(len(s)):
    if s[i] % 13 == 7 and s[i] % 7 != 0 and s[i] % 11 != 0:
        ans.append(s[i])
print(max(ans) - min(ans), len(ans))

s = [int(x) for x in open('17 (5).txt')]
ans = []
for i in range(len(s)):
    if s[i] % 16 == 11 and s[i] % 7 == 0 and s[i] % 6 != 0 and s[i] % 13 != 0 and s[i] % 19 != 0:
        ans.append(s[i])
print(sum(ans), len(ans))
s = [int(x) for x in open('17 (6).txt')]
ans = []
for i in range(len(s) - 1):
    if abs((s[i] + s[i + 1])) % 3 == 0 and abs((s[i] + s[i + 1])) % 6 != 0 and abs(s[i] * s[i + 1]) % 10 == 8:
        ans.append(s[i] + s[i + 1])
print(len(ans), max(ans))

s = [int(x) for x in open('17 (7).txt')]
ans = []
for i in range(len(s) - 1):
    if abs((s[i] + s[i + 1])) % 7 == 0 and (s[i] * s[i + 1]) > 0:
        ans.append(s[i] * s[i + 1])
print(len(ans), min(ans))
s = [int(x) for x in open('17 (8).txt')]
ans = []
for i in range(len(s) - 2):
    if abs(s[i] * s[i + 1] * s[i + 2]) % 7 == 0 and abs(s[i] + s[i + 1] + s[i + 2]) % 10 == 5:
        ans.append(s[i] + s[i + 1] + s[i + 2])
print(len(ans), max(ans))

s = [int(x) for x in open('17 (9).txt')]
ans = []
for i in range(len(s) - 2):
    if (s[i] % 12 == 0 or s[i + 1] % 12 == 0 or s[i + 2] % 12 == 0):
        if (s[i] % 3 == 0 and s[i + 1] % 3 == 0 and s[i + 2] % 3 == 0):
            ans.append((s[i] + s[i + 1] + s[i + 2]) // 3)
print(len(ans), min(ans))

s = [int(x) for x in open('17 (10).txt')]
ans = []
for i in range(len(s) - 2):
    if (s[i] % 3 == 2 or s[i + 1] % 3 == 2 or s[i + 2] % 3 == 2):
       ans.append(min(s[i], s[i+1], s[i+2]))
print(len(ans), sum(ans))

s = [int(x) for x in open('17 (12).txt')]
ans = []
for i in range(len(s) - 4):
    if s[i] >= s[i + 1] >= s[i + 2] >= s[i + 3] and ((s[3] - s[1])) > 1000:
        ans.append(s[i] + s[i + 1] + s[i + 2] + s[i + 3])
print(len(ans), min(ans))

s = [int(x) for x in open('17 (13).txt')]
ans = []
for i in range(len(s) - 1):
    if s[i] + s[i + 1] >= 100 and (s[i] < 0 or s[i + 1] < 0):
        ans.append(s[i] * s[i + 1])
print(len(ans), max(ans))

s = [int(x) for x in open('17 (14).txt')]
# ans = []
for i in range(len(s) - 1):
    if 50 <= (abs(s[i]) + abs(s[i + 1])) <= 200:
        ans.append(min([s[i], s[i + 1]]))
print(len(ans), min(ans))

s = [int(x) for x in open('17 (15).txt')]
ans = []
ar = sum(s) // len(s)
for i in range(len(s) - 2):
    if (s[i] > ar) + (s[i + 1] > ar) + (s[i + 2] > ar) >= 2:
        ans.append(s[i] + s[i + 1] + s[i + 2])
print(len(ans), max(ans))

s = [int(x) for x in open('17 (16).txt')]
M = max(x for x in s if x % 19 == 0)
ans = []
for i in range(len(s) - 1):
    if s[i] > M or s[i + 1] > M:
        ans.append(s[i] + s[i + 1])
print(len(ans), min(ans))

s = [int(x) for x in open('17 (17).txt')]

a11 = [x for x in s if x % 11 == 0]
a17 = [x for x in s if x % 17 == 0]
if len(a11) > len(a17):
    print(len(a11), min(a11))
else:
    print(len(a17), min(a17))

s = [int(x) for x in open('17 (18).txt')]
a = max(x for x in s if x % 10 == 4) + min(x for x in s if x % 10 == 4)
ans = []
for i in range(len(s) - 1):
    if s[i]+s[i+1] < a:
        ans.append(s[i]+s[i+1])
print(len(ans), max(ans))

s = [int(x) for x in open('17 (19).txt')]
ans = []
for i in range(len(s) - 1):
    if (s[i] % 9 == 0 and s[i + 1] % 9 != 0 and abs(s[i + 1]) % 8 == 3) \
            or (s[i + 1] % 9 == 0 and s[i] % 9 != 0 and abs(s[i]) % 8 == 3):
        ans.append(max([s[i], s[i + 1]]))
print(len(ans), max(ans))

s = [int(x) for x in open('17 (20).txt')]
ans = []
def f(x):
    return x > 0 and x % 10 == 9
for i in range(len(s)-2):
    if (not f(s[i])) and f(s[i+1]) and (not(f(s[i+2]))):
        ans.append(s[i] + s[i+1]+s[i+2])
print(len(ans), max(ans))

s = [int(x) for x in open('17 (21).txt')]
S = sum(int(i) for x in s if x % 35 == 0 for i in str(x))
ans = []
for i in range(len(s) - 1):
    if (s[i] > S and s[i + 1] <= S and s[i + 1] % 16 == 15 and s[i + 1] // 16 % 16 == 14) \
            or (s[i + 1] > S and s[i] <= S and s[i] % 16 == 15 and s[i] // 16 % 16 == 14):
        ans.append(s[i] + s[i + 1])
print(len(ans), min(ans))
