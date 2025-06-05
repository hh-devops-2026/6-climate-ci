import sys
import os
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from src.analyze import analyze_and_plot


def test_analyze_and_plot_creates_plot():
    input_csv = "data/demodata.csv"
    with tempfile.TemporaryDirectory() as tmpdir:
        output_file = os.path.join(tmpdir, "plot.png")
        analyze_and_plot(input_csv, output_file)
        assert os.path.exists(output_file), "Plot file was not created."
        # Optionally, check that the file is not empty
        assert os.path.getsize(output_file) > 0, "Plot file is empty."
