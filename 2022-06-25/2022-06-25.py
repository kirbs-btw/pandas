import pandas as pd

"""
Wrong format data 

pd.to_datetime(df['Date'])
converts 
20220412
to 2022/04/12

nan to nat 


df.dropna(subset=['Date'], inplace = True)
drops the whole row

"""


def main():

    df = pd.read_csv('data.csv')

    df['Date'] = pd.to_datetime(df['Date'])

    df.dropna(subset=['Date'], inplace = True)


if __name__ == '__main__':
    main()
