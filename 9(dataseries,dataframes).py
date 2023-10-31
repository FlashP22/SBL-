import pandas as pd

# Creating a Series
data_series = pd.Series([10, 20, 30, 40, 50])
print("Data Series:")
print(data_series)

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']}
data_frame = pd.DataFrame(data)
print("\nData Frame:")
print(data_frame)

# Accessing elements in a Series
print("\nAccessing elements in the Data Series:")
print("First element:", data_series[0])
print("Last element:", data_series[len(data_series) - 1])
print("Slicing:", data_series[1:4])

# Accessing elements in a DataFrame
print("\nAccessing elements in the Data Frame:")
print("Name column:")
print(data_frame['Name'])
print("\nAge column:")
print(data_frame['Age'])
print("\nRow 2:")
print(data_frame.loc[2])  # Accessing by label
print("\nRow 3:")
print(data_frame.iloc[3])  # Accessing by integer position
