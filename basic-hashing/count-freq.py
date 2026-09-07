from collections import defaultdict

def countFreq(arr, n):
    freq_map = defaultdict(int)
    
    for i in range(n):
        freq_map[arr[i]] += 1
    
    for key, val in freq_map.items():
        print(key, val)
        
        
countFreq([1,2,3,3], 4)