import pandas as pd

"""
df.loc()
change loc()


"""


def main():

    df = pd.read_csv("data.csv")

    df.lov[7, 'Duration'] = 45

    for x in df.index:
        if df.loc[x, "Duration"] > 120:
            df.loc[x, "Duration"] = 120

    for x in df.index:
        if df.loc[x, "Duration"] > 120:
            df.drop(x, inplace=True)


if __name__ == '__main__':
    main()