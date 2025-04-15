# pylint: skip-file
def merge_sort(arr):
    global count
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                count+=len(left)-i
                arr[k]=right[j]
                j+=1
                k+=1
            else:
                arr[k]=left[i]
                i+=1
                k+=1
        while i<len(left):
            arr[k]=left[i]
            k+=1
            i+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1

n=int(input())
velocity=[]
count=0
for i in range(n):
    velocity.append(int(input()))
velocity.reverse()
merge_sort(velocity)
print(count)

