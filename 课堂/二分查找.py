def two_found(nums,list):
    lower=0
    high=len(list)-1
    while True:
        mid=int((lower+high)/2)
        guess=(list[mid])
        if guess==nums:
            return mid
        elif guess<nums:
            lower=mid+1
        else:
            high=mid-1


print(two_found(8,[1,2,5,8,9,4]))