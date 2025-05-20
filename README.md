# solar-challenge-week1



####### Project Structure

solar-challenge-week1/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/                   # (Git-ignored) Raw and cleaned CSV files
├── notebooks/
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── compare_countries.ipynb
├── scripts/
│   └── README.md
├── src/
│   └── util.py             # Reusable data cleaning functions
├── tests/
│   └── __init__.py
├── .gitignore
├── requirements.txt
├── README.md

⚙️ Setup Instructions
Clone the repository


git clone https://github.com/tsegabogale24/solar-challenge-week1.git
cd solar-challenge-week1
Create a virtual environment

Using venv:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


pip install -r requirements.txt
 CI/CD
A basic GitHub Actions workflow is configured in .github/workflows/ci.yml to:

Ensure dependencies install correctly

Confirm Python version


