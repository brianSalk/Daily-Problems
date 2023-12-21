# how many numbers between 0 and 10000 have 4 but not 5 in them?


# to make this easier we can left pad the numbers with 0s
# so 10 is 0010 and 123 is 0123 etc.
# 1000 numbers have 4 in each of the 4 digits
# that means 1000 numbers begin with 4
# 900 additional numbers have 4 as the second digit
# 810 additional numbers have 4 as the third digit
# 729 additional numbers have 4 as the fourth digit
if __name__ == "__main__":
    count = 0
    for i in range(10000):
        if '4' in str(i) and '5' not in str(i):
            count += 1
    print(count)
