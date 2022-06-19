
import pandas as pd

def main():
    data = {
        "items": [4, 231, 20],
        "water": [0, 231, 1312],

    }

    df = pd.DataFrame(data)
    print(df)
    print(df.loc[0])

    ndf = pd.DataFrame(data, index=["Ger", "Aus", "It"])
    print(ndf)

    print(ndf.loc["Ger"])

if __name__ == '__main__':
    main()
