import pandas as pd

# Define the input data as a list of tuples
data = [
    [1, 'Soumita M', 'Winning Culture Lab', 280],
    [2, 'Subhangi 0', 'Winning Culture Lab', 75],
    [3, 'Nitin Shane', 'Winning Culture Lab', 1124],
    [4, 'Merwin', 'Mentor', 295],
    [5, 'fardinkamal62', 'Human Capital Lab', 263],
    [6, '__riddhi_213_', 'Human Capital Lab', 504],
    [7, 'Rohit Dutta', 'Mentor', 266],
    [8, 'imshawan', 'Tech Lab', 71],
    [9, 'Anuraj_Saini', 'BrandTech Lab', 342],
    [10, 'sharath', 'Student Unicorn Lab', 3367],
    [11, 'Ronak 0', 'Tech Lab', 302],
    [12, 'Amrit Malviya', 'BrandTech Lab', 336],
    [13, 'Saurabh', 'Mentor', 271],
    [14, 'darshimalde', 'Student Unicorn Lab', 3169],
    [15, 'Shagun', 'Tech Lab', 100],
    [16, 'Ayisha', 'Student Unicorn Lab', 3406],
    [17, 'Palash', 'Growpital', 69],
    [18, 'raman', 'Growpital', 539],
    [19, 'Nishant', 'Growpital', 299],
    [20, 'Vatsal', 'Kringle', 3408],
    [21, 'devmenkr', 'Kringle', 360]
]

# Define the column names
columns = ['S.NO', 'Name', 'Team Name', 'User ID']

# Create a DataFrame from the input data
inp1 = pd.DataFrame(data, columns=columns)

# Display the DataFrame
# print(inp1)

import pandas as pd

data = [[1, 'Soumita M', 280, 13, 21],
        [2, 'Subhangi 0', 75, 13, 16],
        [3, 'Nitin Shane', 1124, 12, 11],
        [4, 'Merwin', 295, 13, 12],
        [5, 'fardinkamal62', 263, 2, 2],
        [6, '__riddhi_213_', 504, 2, 7],
        [7, 'Rohit Dutta', 266, 3, 3],
        [8, 'imshawan', 71, 9, 9],
        [9, 'Anuraj_Saini', 342, 7, 7],
        [10, 'sharath', 3367, 8, 8],
        [11, 'Ronak 0', 302, 16, 19],
        [12, 'Amrit Malviya', 336, 2, 4],
        [13, 'Saurabh', 271, 6, 8],
        [14, 'darshimalde', 3169, 3, 3],
        [15, 'Shagun', 100, 2, 2],
        [16, 'Ayisha', 3406, 11, 8],
        [17, 'Palash', 69, 6, 7],
        [18, 'raman', 539, 5, 5],
        [19, 'Nishant', 299, 4, 5],
        [20, 'Vatsal', 3408, 2, 2],
        [21, 'devmenkr', 360, 7, 7]]

columns = ['S No', 'Name', 'User ID', 'total_statements', 'total_reasons']

inp2 = pd.DataFrame(data=data, columns=columns)

# print(inp2)

merged_df = pd.merge(inp1, inp2, on='User ID')
# print(merged_df)
# print(merged_df.iloc[0])

merged_df = merged_df.drop('Name_y', axis=1)
merged_df = merged_df.drop('S No', axis=1)

# print(merged_df.iloc[0])

# merged_df.to_excel('output.xlsx', index=False)

# merged_df['sum_col'] = merged_df['total_statements'] + merged_df['total_reasons']
# merged_df = merged_df.sort_values(['sum_col','Name_x'], ascending=[False,True])
# print(merged_df)


merged_df = merged_df.assign(sum_col=merged_df['total_statements'] + merged_df['total_reasons']).sort_values(['sum_col', 'Name_x'], ascending=[False, True], kind='mergesort').drop('sum_col', axis=1)

merged_df = merged_df.drop(['Team Name','S.NO'], axis=1)

merged_df = merged_df.reset_index()
print(merged_df)
merged_df.to_excel('output2.xlsx', index=False)