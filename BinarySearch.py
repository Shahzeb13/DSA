def BinarySearch(nums , target):
    print(f"-----------------------Binary Search-------------------------------")
    low = 0;
    high = len(nums) - 1;
    print(f"Target to be found : {target}");
    i = 0;
    while low <= high:
        
        i += 1;
        print(f"Iteration {i}")
        mid = (low + high) // 2;
        print(f"Mid : { mid}")
        if nums[mid] == target:
            return nums[mid];
        elif nums[mid] < target:
            low = mid + 1;
            print(f" New Low : {low}")
        elif nums[mid] > target:
            high = mid - 1;
            print(f" New High : {high}")

res = BinarySearch([1 , 2, 3, 4, 5, 6, 7, 8, 9, 10] , 8);
print(f" Target Found: {res}")
