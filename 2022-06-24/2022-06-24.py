import pandas as pd

"""

dropna() 

del's the rows with empty data
finna = replace empty slots with certain values

x = df["Calories"].mean()
x = the mean of every value 

x = df["Calories"].median()
.median = median 

x = df["Calories"].mode()[0]
mode = the most frequent value

"""

def main():
    df = pd.read_csv('data.csv')

    new_df = df.dropna()

    print(new_df.to_string())

    df.dropma(inplace = True)
    print(df.to_string())

    df.fillna(130, inplace = True)

    df["Calories"].fillna(130, inplace = True)

def otherWay():

    df = pd.read_csv('data.csv')

    x = df["Calories"].mean()
    x = df["Calories"].median()
    x = df["Calories"].mode()[0]

    df["Calories"].fillna(x, inplace=True)




if __name__ == '__main__':
    main()
