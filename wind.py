import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


file = pd.read_csv('your_path/static/wind_Ukraine.tsv', sep="\t")
df = pd.DataFrame(file)


def df_to_dict():
    """Converts pandas DataFrame object to dictionary."""
    regions_dict = dict()

    for ix in range(1, len(df)):
        month_dict = dict()

        for index in range(1, 13):
            month_dict[int(df.iloc[0][index])] = df.iloc[ix][index]

        month_dict[df.iloc[0][13]] = float(df.iloc[ix][13])
        regions_dict[df.iloc[ix][0]] = month_dict

    return regions_dict


def plot(month="Річний"):
    """Draws a plot of chosen month from the lowest value to rhe highest."""
    region_dict = df_to_dict()
    new_df = pd.DataFrame(columns=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "Річний"], index=list(region_dict.keys()))

    for ix in range(len(region_dict)):
        new_df.loc[list(region_dict.keys())[ix]] = pd.Series(region_dict[list(region_dict.keys())[ix]])
    new_df = new_df.sort_values(month)

    sns.barplot(x=new_df[month], y=new_df.index).set_title("Середньомісячна швидкість вітру в регіонах України")
    plt.xlabel("Середня швидкість вітру, м/с")
    plt.ylabel("Регіони")
    plt.savefig('your_path/static/images/wind.png')
    plt.show()


def represent():
    """Represents the dictionary of regions got by df_to_dict() method."""
    regions_dict = df_to_dict()
    for ix in range(1, len(df)):
        region = df.iloc[ix][0]
        print(region, ": ", regions_dict[region], sep="")


if __name__ == "__main__":
    represent()
    plot()
