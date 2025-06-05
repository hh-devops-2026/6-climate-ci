import pandas as pd
from src.analyze import analyze_and_plot


def test_analyze_and_plot_creates_output_file(tmp_path):
    # Create a simple test DataFrame
    data = {
        'date': pd.date_range(start='2023-01-01', periods=3, freq='ME'),
        'temperature': [10, 15, 20]
    }
    df = pd.DataFrame(data)

    # Save test data to a temporary CSV file
    input_csv = tmp_path / "test_data.csv"
    df.to_csv(input_csv, index=False)

    # Define output file path
    output_file = tmp_path / "test_output.png"

    # Run the function
    analyze_and_plot(input_csv, output_file)

    # Verify that the output file was created
    assert output_file.exists()