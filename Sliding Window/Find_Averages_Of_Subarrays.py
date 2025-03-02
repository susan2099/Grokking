def avg_of_subarrays(K, arr):
    sum = 0.0
    start = 0
    result = []
    for end in range(len(arr)):
        sum+=arr[end]
        if((end-start) >= (K-1)):
            result.append(sum/K)
            sum-=arr[start]
            start+=1
    return result
    
def main():
    result = avg_of_subarrays(5,[1,3,2,6,-1,4,1,8,2])
    print("Averages of subarrays of size K: " + str(result))
    
main()   
    
