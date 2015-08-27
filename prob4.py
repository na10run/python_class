def min(x, y):
    out = []
    length = len(x)
    a = 0
    while length != a:
        if x[a] < y[a]:
            out.append(x[a])
        else:
            out.append(y[a])
        a += 1
    print(out)

x= [10,2,30,4]
y= [1,20,3,40]
min(x, y)
