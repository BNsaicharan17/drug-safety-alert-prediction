import pandas as pd

def load_data():
    data = pd.read_csv("drug_data.dataset.csv")   # file name here
    print(data.head())   # show first 5 rows
    return data

if __name__ == "__main__":
    load_data()
