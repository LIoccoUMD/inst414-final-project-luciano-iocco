import pandas as pd

# Load dataset
df = pd.read_csv("data\downloaded\megaGymDataset.csv", index_col=0)
# Fix rename, this just drops column
# df.rename(columns={"Unnamed: 0": 'ID'}, inplace=True)

# Calculate the mean rating for each level where rating is not NaN
mean_ratings_by_level = df.groupby('Level')['Rating'].mean()

# Fills missing Rating values based on mean grouped by level (beginner, intermediate, advanced)
def fill_missing_rating(row):
    if pd.isna(row['Rating']):
        return mean_ratings_by_level[row['Level']]
    else:
        return row['Rating']

# Apply the function to fill missing values
df['Rating'] = df.apply(fill_missing_rating, axis=1)

# View specific rows with NaN for equipment
missing_equipment_rows = df[df['Equipment'].isna()]

updates = {
    637: "Bench",
    638: "Bench",
    639: "Rod",
    699: "None",
    912: "Roller",
    914: "Wall",
    1207: "None",
    1402: "None",
    1403: "Band",
    1404: "None",
    1405: "Seat",
    1406: "None",
    1407: "None",
    1531: "None",
    1532: "Seat",
    1533: "None",
    1624: "None",
    1625: "None",
    1626: "None",
    1627: "None",
    1780: "Rod",
    2418: "None",
    2419: "Seat",
    2420: "None",
    2421: "Dumbbell",
    2422: "Smith machine",
    2423: "None",
    2763: "None",
    2764: "None",
    2765: "None"
}

# Apply updates to df
for index, equipment in updates.items():
    df.loc[index, 'Equipment'] = equipment

# Verify specific rows
print(df.loc[list(updates.keys())])