from functools import wraps
import datetime

def intime(f):
    @wraps(f)
    def inner_wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        res = f(*args,**kwargs)
        end = datetime.datetime.now()
        print(f"runtime = {(end-start).total_seconds()}")
        return res
    return inner_wrapper

@intime
def linear_search(arr,target):
    pos = arr.index(target)
    return pos

@intime
def binary_search(arr,target):
    def _bs(arr,target,first,last):
        mid = int((first + last)/2)
        if first > last:
            return None
        else:
            if arr[mid] == target:
                print("FOUND")
                return mid
            elif arr[mid] > target:
                # print(f"LEFT - {first} to {mid-1}")
                return _bs(arr,target,first,mid-1)
            else:
                # print(f"RIGHT - {mid+1} to {last}")
                return _bs(arr,target,mid+1,last)
    return _bs(arr,target,0,len(arr)-1)