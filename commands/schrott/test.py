import pandas as pd
# Sample DataFrame for demonstration
df_eda = pd.DataFrame({
    'variable_name': [10, 20, 15, 30, 25, 30, 45, 50]
})

# Summary statistics for the 'variable_name' column
summary = df_eda['variable_name'].describe()

# Additional statistics
mean_value = df_eda['variable_name'].mean()
median_value = df_eda['variable_name'].median()
std_dev = df_eda['variable_name'].std()
min_value = df_eda['variable_name'].min()
max_value = df_eda['variable_name'].max()
variance = df_eda['variable_name'].var()
quantiles = df_eda['variable_name'].quantile([0.25, 0.5, 0.75])

# Display the summary statistics
print("Summary Statistics:\n", summary)
print("\nAdditional Statistics:")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_dev}")
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
print(f"Variance: {variance}")
print(f"Quantiles:\n{quantiles}")