def bsearch(data,target) :
    low = 0
    high = len(data)-1
    while (low <= high) :
        mid = (low + high)//2
        if(data[mid]==target) :
            return mid
        elif (data[mid] > target) :
            high = mid -1
        elif(data[mid<target]):
            low = mid + 1
    else:
        return None
data=[1,2,3,4,5]
print(bsearch(data,4))
