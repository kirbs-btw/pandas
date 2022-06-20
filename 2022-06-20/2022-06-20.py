inport pandas as pd 

reading csv files


"""

def main():
    df = pd.read_csv('data.csv')

    print(df.to_string())

def system():
    print(pd.options.display.max_rows)

    """ change max rows"""
    pd.options.display.max_rows = 100


if __name__ == '__main__':
    system()
