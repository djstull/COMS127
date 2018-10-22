def times_tables(n):
    l = len(str(n*n))
    for i in range(1, 1 + n):
        s = ""
        for j in range (1, 1 + n):
            s += "%*d" % (l, i * j)
        print(s)

times_tables(10)