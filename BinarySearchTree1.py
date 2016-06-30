from time import time

def bs_contains(ordered, target):
    """ use binary array serach to determine if target is in collection """
    
    low = 0
    high = len(ordered) - 1
    while low <= high:
        mid = (low + high) / 2
        if target == ordered[mid]:
            return mid
        elif target < ordered[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return -(low + 1)

def insertInPlace(ordered, target):
    """ insert target into proper location """
    idx = bs_contains(ordered, target)
    if idx < 0:
        ordered.insert(-(idx + 1), target)
        return
    
    ordered.insert(idx, target)

def performance():
    """" demonstrate execution performance of contains """
    n = 1024
    while n < 50000000:
    	sorted = range(n)
    	now = time()
    
    	#Code whose performance is to be evaluated
    	insertInPlace(sorted, + 1)
    
    	done = time()
    
    	print n, (done - now) * 1000
    
    	n *= 2
    
performance()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    