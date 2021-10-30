def twoSum(nums, target):
        
        ind = []

        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    ind = [i,j]
                    
        return ind

if __name__ == '__main__':
    ind_ret = twoSum([3,3],6)
    print(ind_ret)