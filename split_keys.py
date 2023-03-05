import openpyxl
import pandas
import pandas as pd

if __name__ == '__main__':

    # list_cols = ["E_phi", "E_psi", "N_0", "N_n", "P", "Q"]
    # dict to store columns needs splitting and the number of splits
    dict_cols = {
        "f": 2,
        "h": 2,
        "E_phi": 2,
        "E_psi": 2,
        "N_0": 4,
        "N_n": 4,
        "P": 8,
        "Q": 8
    }

    # Read the original Excel file
    df = pandas.read_excel("key_list_40000_227.xlsx")

    # Stores output data
    out = pandas.DataFrame()

    for i in dict_cols:
        # Replace the []; with spaces
        df[i] = df[i].str.replace("[", " ", regex=False)
        df[i] = df[i].str.replace("]", " ", regex=False)
        df[i] = df[i].str.replace(";", " ", regex=False)

        # Split based on one or more \s
        x = df[i].str.split(" +", expand=True)

        for j in range(dict_cols[i]):
            # Drop the first column (since in split the first column and last is "")
            out[f"{i}_{j}"] = x[j+1]

    # Reinsert R0 and Rn value into the correct position
    out.insert(loc=4, column="R_0", value=df["R_0"])
    out.insert(loc=4, column="R_n", value=df["R_n"])

    # Covert all to numeric
    out = out.apply(pd.to_numeric)

    out.to_excel("split_key_list_40000_227.xlsx", index=False)
    # out.to_csv("split_key_list_for_matlab_227.csv", index=False)

    print()
