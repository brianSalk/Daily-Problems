# how many numbers between 0 and 10000 have 4 but not 5
# as at least one of their digits?
if __name__ == "__main__":
    count = 0
    for i in range(10_000):
        count += '4' in str(i) and '5' not in str(i)
    print(count)
