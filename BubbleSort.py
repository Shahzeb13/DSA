def bubbleSort(nums):
    # for i in range(len(nums) - 1):
    #     j = i+1;
    #     for j in :
    #         if(j < nums.length):
    #             if(nums[i] > nums[j]):
    #                 #swap nums[i] with nums[j]
    #                 i +=1
    #                 j +=1
    #                 break;
    #         i=0;
    #         j=0;
    #         break;
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i -1):
            if nums[j] > nums[j + 1]:
                nums[j] , nums[j+1] = nums[j+1] , nums[j]
    return nums

res = bubbleSort([9,1,5,3,7])
print(res);
