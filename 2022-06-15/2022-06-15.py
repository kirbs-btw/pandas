import pandas as pd

"""
use of pandas: 
    -data analysis 
    -cleaning 
    -exploring 
    -manipulating
    -pandas = python data analysis

dataFrame : frames the data in a readable way

"""

def main():

    data = {
        'mouse': ["Nyth", "Kova", "Koan"],
        'passings': [3, 4, 1],
    }

    print(pd.DataFrame(data))



if __name__ == '__main__':
    main()