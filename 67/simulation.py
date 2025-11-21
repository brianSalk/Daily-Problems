# count five digit numbers that do not contain 67
# count numbers without 6 

two67 = 3*10
one67 = 4*10**3

has67 = one67 - two67
no67 = 10**5 - has67

print(no67)

count = 0
success = 0
for each in range(0, 100_000):
    if '67' in str(each):
        success += 1
    count += 1
    
print(100_000-success)
