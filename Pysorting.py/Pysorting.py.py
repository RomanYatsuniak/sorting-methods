import random
random.seed()
arr=[]
def sel_sort(arr1):
    for i in range(len(arr1)):
        min=arr1[i]
        for j in range (i,len(arr1)):
            if min>arr1[j]:
                min=arr1[j]
                k=j
        tmp=arr1[i]
        arr1[i]=min
        arr1[k]=tmp
    return(arr1)

def ins_sort(arr2):
    for i in range (1,len(arr2)):
        j=i
        while j>0:
            if arr2[j]<arr2[j-1]:
                tmp=arr2[j-1]
                arr2[j-1]=arr2[j]
                arr2[j]=tmp
            j-=1
    return(arr2)

def bubble_sort(arr3):
    length=len(arr3)
    for i in range (len(arr3)):
        for j in range (1,length):
            if arr[j-1]>arr[j]:
                tmp=arr[j]   
                arr[j]=arr[j-1]
                arr[j-1]=tmp
        length-=1
    return(arr3)
def quick_sort(arr4, st, end):
    pivot=arr4[round((st+end)/2)]
    i=st
    j=end
    while i<=j:
        while arr[i]<pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        if i<=j:
            tmp=arr4[i]
            arr4[i]=arr4[j]
            arr4[j]=tmp
            i+=1
            j-=1
            if st<j:
                quick_sort(arr4, st, j)
            if i<end:
                quick_sort(arr4, i, end)
    return (arr4)

def merge_sort(arr5):
    if len(arr5)<2:
        return arr5
    mid=round(len(arr5)/2)
    left=merge_sort(arr5[:mid])
    right=merge_sort(arr5[mid:])
    return merge(left, right)

def merge(left, right):
    res=[]
    i=0
    j=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res+=left[i:]
    res+=right[j:]
    return res

def heap_sort(arr6):
    def heap(arr6,m,n):
        nel=arr6[m]
        while 2*m+1<n:
            child=2*m+1
            if child+1 < n and arr6[child] < arr6[child+1]:
                child+=1
            if nel>=arr6[child]:
                break
            arr6[m]=arr6[child]
            m=child
            arr[m]=nel
    l1=len(arr6)
    for i in range(l1//2-1,-1,-1):
        heap(arr6, i, l1)
    for i in range(l1-1,0,-1):
        tmp=arr6[i]
        arr6[i]=arr6[0]
        arr6[0]=tmp
        heap(arr6,0,i)
    return (arr6)

def bucket_sort(arr7):
    MAX=max(arr7)
    length=len(arr7)
    size=MAX/length
    bucket = [[] for _ in range(length)]
    for i in range(length):
        div=int(arr7[i]/size)
        if div != length:
            bucket[div].append(arr7[i])
        else:
            bucket[length -1].append(arr7[i])
    for i in range (length):
        bubble_sort(bucket[i])
    res=[]
    for i in range(length):
        res=res+bucket[i]
    return(res)

def radix_sort(arr8):
    m=1
    r=10
    beginning=True
    while beginning:
        beginning = False
        bucket=[[], [], [], [], [], [], [], [], [], []]
        for i in arr8:
            pos=i%r//m
            bucket[pos].append(i)
            if not beginning and pos >0:
                beginning=True
        arr8=[]
        for i in bucket:
            for j in i:
                arr8.append(j)
        r*=10
        m*=10
    return(arr8)

for i in range (50):
    losowana = random.randrange(1,51)
    arr.append(losowana)
print(arr)

print("\nSelection sort\n",sel_sort(arr))
print("\nInsertion sort\n",ins_sort(arr))
print("\nBubble sort\n",bubble_sort(arr))
print("\nQuick sort\n",quick_sort(arr,0,len(arr)-1))
print("\nMerge sort\n",merge_sort(arr))
print("\nHeap sort\n",heap_sort(arr))
print("\nBucket sort\n",bucket_sort(arr))
print("\nRadix sort\n", radix_sort(arr))