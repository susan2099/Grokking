def smallest_subarray_with_given_sum(s,arr):
    curr_sum = 0
    result_len = len(arr)
    start=0
    end = 0
    curr_sum = arr[0]
    while(end < len(arr)):
        if(curr_sum >= s):
            if result_len > ((end-start)+1):
                result_len = (end-start) + 1
                curr_sum-=arr[start]
                start+=1
            else:
                curr_sum-=arr[start]
                start+=1
        else:
            end+=1
            if(end < len(arr)):
                curr_sum+=arr[end]
    if(result_len == len(arr)):
        return 0
    return result_len
    
def main():
    result = smallest_subarray_with_given_sum(7,[2,1,5,2,3,2])
    print("Smallest subarray with given sum: " + str(result))
    result = smallest_subarray_with_given_sum(7,[2,1,5,2,8])
    print("Smallest subarray with given sum: " + str(result))
    result = smallest_subarray_with_given_sum(8,[3,4,1,1,6])
    print("Smallest subarray with given sum: " + str(result))

main()