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

### Steps

Your goal is to complete the GitHub Actions workflow file (`.github/workflows/ci.yml`) by implementing the following steps.

1.) **Define Workflow Triggers**
- Make the workflow run when code is pushed or a pull request is made to the main branch.

💡 Hint: Use on: with common GitHub events like push and pull_request.

2.) **Set the Runner Environment**
- Specify that the workflow should use a Linux-based virtual environment.

💡 Hint: Use the latest Ubuntu runner.

3.) **Checkout the Code**
- Include a step to make the code from your repository available in the workflow.

💡 Hint: Use an official GitHub-provided action for this.

4.) **Set Up Python**
- Configure the Python version used in the workflow.

💡 Hint: Use an action that lets you choose the Python version (e.g., 3.11).

5.) **Install Dependencies** 
- Install all Python libraries listed in `requirements.txt` file.

💡 Hint: Use pip with the provided `requirements.txt` file. The command is `pip install -r <file_name>`

6.) **Lint the Code**
- Add a step to check code style for both `source` and `test` directories. Fix linter errors if there are any.

💡 Hint: Use flake8 to check src/ and tests/ folders. The command is `flake8 <folder_1> <folder_2>`

7.) **Generate the Plot**
- Run the analysis script that reads a CSV file and outputs a plot.

💡 Hint: The script accepts input and output paths as arguments. The command is `python src/analyze.py <input_csv> <output_file>`. The csv file that contains data can be found from the `data` directory. The output file name should be `plot.png` and located in the `output` directory.

8.) **Upload the Plot**
- Make the generated plot available as a downloadable artifact in GitHub Actions.

💡 Hint: Use the official upload-artifact action.

💡 Name: climate-plot

💡 Path: The output/plot.png file

9.) **Run Tests**
- Run automated tests to verify your script works correctly.

💡 Hint: Use a Python test framework. The command to run tests is `pytest tests/ -v`
💡 Hint: Set an environment variable `PYTHONPATH` and set its value `${{ github.workspace }}` so the test runner can find the src/ folder.

### Result

After the succesfull workflow run open the workflow log in Github and open `Upload Plot Artifact` step. You can find link to download plot from the log. Download the plot file and it should look the following:


### Bonus

