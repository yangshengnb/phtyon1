for i in range(1, 10):
    for j in range(1, i+1):
      formula=f'{i:1}x{j:1}={i*j:<2}}'
      print (formula,end=' ')
    print()
