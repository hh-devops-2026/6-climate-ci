import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def analyze_and_plot(input_csv, output_file):
    df = pd.read_csv(input_csv, parse_dates=["date"])
    df["month"] = df["date"].dt.month
    monthly_avg = df.groupby("month")["temperature"].mean()

    plt.figure(figsize=(10, 6))
    monthly_avg.plot(kind="bar", title="Average Monthly Temperature (°C)")
    plt.xlabel("Month")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_file)
    plt.close()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv")
    parser.add_argument("output_png")
    args = parser.parse_args()
    analyze_and_plot(args.input_csv, args.output_png)
