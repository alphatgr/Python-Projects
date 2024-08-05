import pyttsx3
engine=pyttsx3.init()
print("Program for binary search")
engine.say("Program for binary search")
engine.runAndWait()
def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[low] < target:
            low = mid+1
        else :
            high = mid-1
    return -1
engine.say("Enter the number of elements")
engine.runAndWait()
no_of_elements=int(input("Enter the number of elements : "))
arr=[]
engine.say("Enter the elements")
engine.runAndWait()
print("Enter the elements : ")
for i in range (no_of_elements):
    elements=int(input())
    arr.append(elements)
engine.say("Enter the target element to be searched")
engine.runAndWait()
target=int(input("Enter the target element to be searched : "))
result=binary_search(arr,target)
if result!=-1:
    engine.say(f"The target element is found at the index : {result}")
    engine.runAndWait()
    print ("The target element is found at the index : " , result)
else :
    engine.say("The target element is not found.")
    engine.runAndWait()
    print ("The target element is not found.")