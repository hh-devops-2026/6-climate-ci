Climate Insights is a startup company that analyzes historical temperature data to visualize monthly trends.
The data team needs an automated CI pipeline to:

- Ensure the analysis script is correct
- Follow code style guidelines
- Automatically generate updated visualizations
- Store these visualizations as CI artifacts

They have a functional Python script that utilizes these technologies:
- pandas: A Python library for data manipulation and analysis, especially useful for working with structured data like tables and spreadsheets.
- matplotlib: A widely-used Python library for creating static, animated, and interactive data visualizations (often used for plotting graphs and charts). (You wrote "matlib" but the correct name is "matplotlib.")
- pytest: A testing framework for Python, making it easy to write simple and scalable test cases for your code.
- flake8: A tool for checking the style and quality of Python code, helping developers follow best practices and identify errors or formatting issue
Your mission is to build and test this automation pipeline using GitHub Actions. 

Implement a GitHub Actions workflow that:

1. Installs dependencies via `pip install -r requirements.txt`
2. Runs tests using `pytest`  
3. Checks code style with flake8 linter 
4. Executes the script `analyze.py` to generate a bar chart  
5. Uploads the plot as a build artifact

The `./github/workflows` directory contains the `ci.yml` file. You should complete the tasks marked as TODOs within this file.

Here are some tips to steps:
