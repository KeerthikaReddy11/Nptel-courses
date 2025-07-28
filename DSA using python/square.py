def h(n):
    s = False
    for i in range(1,(n**2)+1):
        if i*i == n:
            s = True
    return(s)
print(h(12))
