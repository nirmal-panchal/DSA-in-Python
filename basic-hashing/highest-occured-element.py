from collections import defaultdict

def countFreq(arr, n):
    freq_map = defaultdict(int)
    
    for i in range(n):
        freq_map[arr[i]] += 1
    
    mx = 0
    item = 0
    
    for key, val in freq_map.items():
        if mx < val : 
            mx = val
            item = key
            
    print("highest occured one is :", item)
        
        
countFreq([1,2,2,2,3,3], 4)