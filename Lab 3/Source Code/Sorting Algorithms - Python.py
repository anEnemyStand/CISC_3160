#Clinton Caldwell   Lab 3
#Python Sorting Algorithms

def printPreSortList(sortType, a):
    print("Pre-",sortType,"Sort:\n",a,)

def printPostSortList(sortType, a):
    print("Post-",sortType,"Sort:\n",a,)
    print("----------\n")


#Insertion Sort ----------------------------------
def insertionSort(a):
    printPreSortList("Insertion", a)
    
    for i in range(1, len(a)):
        temp = a[i]
        j = i
        while j>0 and a[j-1] >= temp:
            a[j] = a[j-1]
            j-=1
        a[j] = temp

    printPostSortList("Insertion", a)
    

#Bubble Sort ----------------------------------
def bubbleSort(a):
    printPreSortList("Bubble", a)

    for j in range(len(a)-1, 0, -1):
        for i in range(0, j):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp

    printPostSortList("Bubble", a)


#Selection Sort ----------------------------------
def selectionSort(a):
    printPreSortList("Selection", a)
    
    for i in range(0, len(a)):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j
        temp = a[min]
        a[min] = a[i]
        a[i] = temp


    printPostSortList("Selection", a)


#Merge Sort ----------------------------------
def mergeSort2(a):
    if len(a) >1:
        m = len(a)//2
        L = a[:m]
        R = a[m:]
        
        mergeSort2(L)
        mergeSort2(R)

        #Merge L and R into original   
        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                a[k] = L[i]
                i+=1
            else:
                a[k] = R[j]
                j+=1
            k+=1
            
        #Add any remaining elements in L and R
        while i < len(L):
            a[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            a[k] = R[j]
            j+=1
            k+=1

#Merge Sort Gate
def mergeSort(a):
    printPreSortList("Merge", a)
    mergeSort2(a)
    printPostSortList("Merge", a)



#Quick Sort ----------------------------------
def quickSort2(a, start, end):
    if start < end:
        p = partition(a, start, end)
        quickSort2(a, start, p-1)
        quickSort2(a, p+1, end)

def partition(a, start, end):
    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] < pivot:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            i+=1
    temp = a[i]
    a[i] = a[end]
    a[end] = temp
    return i


  
#Quick Sort Gate
def quickSort(a):
    printPreSortList("Quick", a)
    quickSort2(a, 0, len(a)-1)
    printPostSortList("Quick", a)



#Shell Sort ----------------------------------
def shellSort(a):
    printPreSortList("Shell", a)
    
    gap = len(a)//2

    while gap > 0:
        for i in range(gap,len(a)):
            temp = a[i]
            j=i
            while j >= gap and a[j-gap] > temp:
                a[j] = a[j-gap]
                j -= gap
            a[j] = temp
        gap //= 2
        
    printPostSortList("Shell", a)




#Testing Sorting Algorithms ----------------------------------
def getList():
    bList = [8, 10, 15, 2, 3, 70, 100, 45, 0, 12, 0, 10, 1, 6, 21, 93]
    sList = [6, 0, 4, 2, 1]
    tList = [2, 1]
    zList = [5]
    
    return bList


insertionSort(getList())

bubbleSort(getList())

selectionSort(getList())

mergeSort(getList())

quickSort(getList())

shellSort(getList())




