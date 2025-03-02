def max_sub_array_of_size_k(k,arr):
    sum = 0
    start = 0
    result_sum = 0

    for end in range(len(arr)):
        sum+=arr[end]
        if((end-start)>=(k-1)):
            result_sum = max(result_sum,sum)
            sum-=arr[start]
            start+=1
    return result_sum

def main():
    result = max_sub_array_of_size_k(3, [2,1,5,1,3,2])
    print("Max subarray of size K: " + str(result))

main()