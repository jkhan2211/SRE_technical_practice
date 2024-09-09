import pandas as pd

data = {
    "Month": pd.Series(
        [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
    ),
    "Rainfall": pd.Series(
        [1.65, 2.45, 3.12, 0.98, 1.76, 2.89, 4.56, 3.78, 2.34, 1.23, 1.89, 2.56]
    ),
}

# Task 1: Create a Pandas DataFrame
# Task 2: Read Data from Files
dfc = pd.read_csv(r"./rain.csv")

# Display the DataFrame
print("Our dataframe")
print(dfc, "\n")

# fill missing values with 0
dfclean = dfc.dropna(0)
