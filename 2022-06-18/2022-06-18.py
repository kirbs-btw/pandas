import pandas as pd

"""
Series
    series is just a column 
    you can label your column with new ones (index = [...])
     

"""

def main():
    arr = [0, 4, 12, 1, 8]
    print(pd.Series(arr))

    print(pd.Series(arr)[0])

    newArr = pd.Series(arr, index = ["a", "b", "c", "d", "e"])
    print(newArr["d"])

def keys():
    setArr = {
        "28-01": 1531,
        "29-01": 451,
        "30-01": 2313,
    }

    mySet = pd.Series(setArr, index=["29-01", "28-01"])
    print(mySet)

def dataFrameFunc():
    setArr = {
        "28-01": [1531],
        "29-01": [451],
        "30-01": [2313],
    }

    print(pd.DataFrame(setArr))

if __name__ == '__main__':
    dataFrameFunc()
