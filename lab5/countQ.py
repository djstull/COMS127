def countQ(s):
    count = 0
    for q in s:
        if q == "q":
            count += 1
    return count

print(countQ("qqq"))