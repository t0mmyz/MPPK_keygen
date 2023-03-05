import pandas
import pandas as pd
import openpyxl

from keygen import keygen


def gen_key_dataframe(m, n, lam, upper_limits, number_of_keys):
    """
    Use the MPPKDS algorithm to generate a dataframe of pub and pri keys
    :param m: number of noise vars, currently equals to n (might subject to change)
    :param n: the degree of a base polynomial
    :param lam: the degree of two univariate polynomials
    :param upper_limits: the upper limits in base polynomials
    :param number_of_keys number of keys to generate
    :return: pandas df containing keys
    """
    # Use a list of dict to store first
    key_list = []

    for i in range(number_of_keys):
        pri_key, pub_key = keygen(m, n, lam, upper_limits)
        # Concatenate dict into a single dict
        key = {**pri_key, **pub_key}
        key_list.append(key)

    # Convert into dict
    return pd.DataFrame(key_list)


if __name__ == '__main__':
    m = 2
    n = 2
    lam = 1
    upper_limits = [1, 1]

    key_df = gen_key_dataframe(m, n, lam, upper_limits, 40000)



    # Hack for matlab to recognize the shape of the list (replace \n with ";")
    key_df["P"] = key_df["P"].astype(str)
    key_df["Q"] = key_df["Q"].astype(str)
    key_df["P"] = key_df["P"].str.replace("\n", ";")
    key_df["Q"] = key_df["Q"].str.replace("\n", ";")

    key_df.to_excel("key_list_40000_227.xlsx", index=False)
    print()

