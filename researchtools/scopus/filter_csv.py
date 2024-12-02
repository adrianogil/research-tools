import pandas as pd

def process_csv(input_csv, output_csv):
    """
    Processes a CSV file to add a 'C0' column based on the 'Title' field.

    Rows with 'Proceedings' or 'Conference' in the 'Title' field get 'C0' as 'No'.
    All other rows get 'C0' as 'Yes'.

    Parameters:
    - input_csv (str): Path to the input CSV file.
    - output_csv (str): Path to save the processed CSV file.
    """
    # Load the CSV file
    data = pd.read_csv(input_csv)

    # Add the 'C0' column
    data['C0'] = data['Title'].apply(
        lambda title: 'No' if isinstance(title, str) and ('Proceedings' in title or 'Conference' in title) else 'Yes'
    )

    # Count the occurrences of 'No' and 'Yes' in the 'C0' column
    counts = data['C0'].value_counts()
    print(counts.to_dict())

    # Save the updated data to a new CSV file
    data.to_csv(output_csv, index=False)
    print(f"Processed file saved to: {output_csv}")


if __name__ == '__main__':
    import argparse

    # Example usage:
    # process_csv('input.csv', 'output.csv')
    parser = argparse.ArgumentParser(description="Process a CSV file to add a 'C0' column based on the 'Title' field.")
    parser.add_argument('input_csv', help='Path to the input CSV file')
    parser.add_argument('output_csv', help='Path to save the processed CSV file')
    args = parser.parse_args()

    process_csv(args.input_csv, args.output_csv)
