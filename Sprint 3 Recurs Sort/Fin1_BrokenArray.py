"""
id 64528864. 
Basically it's a binary search with some adjusment.
Because array was sorted, but then 'broken' - we can say that one half is always sorted.
One can check that with array[minimum] < array[middle].
On the next step we can check if the query is in that range.
If not - discard that half and split the other half.

Time complexity: in worst case O(log n), on each iteration algo discards one half of array and searches thru other half. So on each recursive call we deal only with half of problem.

Memory complexity: constant O(1), all operations happen on the same array. 
"""

def broken_search(nums, query):
    
    def binary_search(nums, min_ind, max_ind, query):
        mid_ind = (min_ind + max_ind) // 2
        
        if nums[mid_ind] == query: #are we lucky?
            return mid_ind
        
        else: # which half is sorted?
            if nums[min_ind] <= nums[mid_ind-1]:
            
                if nums[min_ind] <= query <= nums[mid_ind-1]: # if the number in it?
                    result = binary_search(nums,min_ind,mid_ind,query)
                else:
                    result = binary_search(nums,mid_ind,max_ind,query)

            elif nums[mid_ind] <= nums[max_ind-1]:
                if nums[mid_ind] <= query <= nums[max_ind-1]:
                    result = binary_search(nums,mid_ind,max_ind,query)
                else:
                    result = binary_search(nums,min_ind,mid_ind,query)
            else:
                result = -1
        return result

    if len(nums) == 1: # is it that simple?
        if nums[0] == query:
            return 0
        else:
            return -1 
    else:  # start binary search
        return binary_search(nums, 0, len(nums), query)