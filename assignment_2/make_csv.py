import pandas as pd

i = 'projectdata_FW2022.xlsx'
o = 'projectdata_FW2002.csv'

def main():
    df = pd.read_excel(i)
    df.to_csv(o)
    print(df)

if __name__ == "__main__":
    main()