import dvc.api

# Open the file using DVC
with dvc.api.open(
    'get-started/data.xml',
    repo='https://github.com/iterative/dataset-registry'
) as f:
    # Read the first 10 lines
    lines = [next(f) for _ in range(10)]

# Write the first 10 lines to a new file
with open('first_10_rows.txt', 'w') as output_file:
    output_file.writelines(lines)

print("First 10 rows written to 'first_10_rows.txt'")
