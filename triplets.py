def compareTriplets(a, b):
   Alice = 0
   Bob = 0

   for i in range(3):
    if a[i] > b[i]:
        Alice+=1
    elif a[i] < b[i]:
        Bob+=1
    return Alice, Bob



 