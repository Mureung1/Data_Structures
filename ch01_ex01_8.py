def algorithm(n) :
    sum = 0
    for i in range (n):
        for j in range (i+1, n+1):
            sum = sum + j