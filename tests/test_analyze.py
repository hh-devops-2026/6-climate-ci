from src.analyze import analyze_and_plot
import os
import tempfile


def test_analyze_and_plot_creates_plot():
    input_csv = "data/demodata.csv"
    with tempfile.TemporaryDirectory() as tmpdir:
        output_file = os.path.join(tmpdir, "plot.png")
        analyze_and_plot(input_csv, output_file)
        assert os.path.exists(output_file), "Plot file was not created."
        assert os.path.getsize(output_file) > 0, "Plot file is empty."
