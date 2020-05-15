import pandas as pd


def tsv_to_df():
    """Reads tsv file and returns pandas DataFrame object."""
    file = pd.read_csv("wind_Ukraine.tsv", sep="\t")
    df = pd.DataFrame(file)
    return df


def df_to_dict():
    """Converts pandas DataFrame object to dictionary."""
    df = tsv_to_df()
    regions_dict = dict()

    for ix in range(1, len(df)):
        month_dict = dict()

        for index in range(1, 13):
            month_dict[int(df.iloc[0][index])] = df.iloc[ix][index]

        month_dict[df.iloc[0][13]] = float(df.iloc[ix][13])
        regions_dict[df.iloc[ix][0]] = month_dict

    return regions_dict


def represent():
    """Represents the dictionary of regions got by df_to_dict() method."""
    regions_dict = df_to_dict()
    df = tsv_to_df()

    for ix in range(1, len(df)):
        region = df.iloc[ix][0]
        print(region, ": ", regions_dict[region], sep="")


if __name__ == "__main__":
    represent()





