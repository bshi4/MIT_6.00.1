s = input('input s:')
str1 = ''
for i in range(len(s)):
    str2 = s[i]
    m = 0
    while i+m+1 < len(s) and s[i+m] <= s[i+m+1]:
        str2 += s[i+m+1]
        m += 1
    if len(str1) < len(str2):
        str1 = str2
print(str1)