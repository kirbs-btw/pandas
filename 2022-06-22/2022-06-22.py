import pandas as pd

"""
df.head(n) n = count

df.head() == first 5 rows
df.tail() == last 5 rows 
.info() == returns info 

"""

def main():
    df = pd.read_csv('data.csv')

    print(df.head(10))
    print(df.tail())
    print(df.info())



if __name__ == '__main__':
    main()
