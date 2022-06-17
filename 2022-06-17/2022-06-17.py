import pandas as pd

"""
cleaning data duplicates get dropped of you can replace them with a loop 


"""

def main():
    df = pd.read_csv("data.csv")

    print(df.duplicated())
    df.drop_duplicates(inplace = True)


if __name__ == '__main__':
    main()
