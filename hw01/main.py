for i in range(1, 10):
    for x in range(1,i):
        print(end='       ')
    for j in range(1, 10):
        formula=f'{i:1}x{j:1}={i*j:<2}'
        if i<=j:print (formula,end=' ')
    print( ) 
