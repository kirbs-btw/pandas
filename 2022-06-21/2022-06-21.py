

import pandas as pd

"""
reading json files 

Json files = a python dictionary

usage is the same ==


"""

def main():
    df = pd.read_json('data.json')
    print(df.to_string())



if __name__ == '__main__':
    main()
