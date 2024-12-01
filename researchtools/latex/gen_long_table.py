import pandas as pd


def generate_longtable_latex(data, headers, total_width=15,
                             caption="Your table caption here.",
                             label="your-table-label",
                             latex_file_path="table.tex"):
    # Determine if the input is a DataFrame or a dictionary
    if isinstance(data, list):
        pass
    elif isinstance(data, pd.DataFrame):
        # Convert DataFrame to a list of dictionaries
        data = data.to_dict(orient='records')
    else:
        raise TypeError("Input data must be a dictionary or a pandas DataFrame")

    width_per_column = total_width // len(headers)

    # Start LaTeX table code with reduced font size and left-aligned cells
    latex_code = r"""\begin{longtable}{""" + '|'.join([r'>{\raggedright\arraybackslash}p{' + str(width_per_column) + r'cm}' for _ in headers]) + r"""}
\caption{""" + caption + r"""}\label{""" + label + r"""} \\
\hline
""" + ' & '.join(headers) + r""" \\
\hline
\endfirsthead
\hline
""" + ' & '.join(headers) + r""" \\
\hline
\endhead
"""

    # Iterate over each data entry and create table rows
    for entry in data:
        row = ' & '.join(str(entry.get(header, '')) for header in headers)
        latex_code += row + r""" \\
\hline
"""

    # Close the longtable environment
    latex_code += r"\end{longtable}"

    # Write the LaTeX code to a file
    with open(latex_file_path, 'w') as file:
        file.write(latex_code)
    print(f"Table saved to {latex_file_path}")

    return latex_code
