# 🤖 ML CI Pipeline

This project demonstrates a **Machine Learning Continuous Integration (CI) pipeline** using GitHub Actions.  
It trains a Logistic Regression model on the Iris dataset, evaluates accuracy, and runs automated tests via CI.

---

## 📖 Overview
- Train a Logistic Regression model on the Iris dataset.  
- Automatically test the training pipeline with GitHub Actions.  
- Save the trained model (`model.joblib`).  

---

## 🛠️ Features
- ✅ Logistic Regression model training on Iris dataset  
- ✅ Accuracy evaluation with sklearn metrics  
- ✅ Automated testing using `pytest`  
- ✅ CI/CD pipeline using GitHub Actions (`ci.yaml`)  
- ✅ Model persistence using `joblib`  

---

## 📂 Project Structure
```
ml-ci-pipeline/
│-- src/
│   └── train.py          # Model training script
│-- test_train.py         # Test file for pytest
│-- requirements.txt      # Dependencies
│-- .github/
│   └── workflows/
│       └── ci.yaml       # CI workflow configuration
│-- README.md             # Documentation
```

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
# 1. Clone repository

https://github.com/Shayan03447/ML-CI-PIPELINE.git
cd ML-CI-PIPELINE

# 2. Create virtual environment 
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
conda activate venv        # Conda 

# 3. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

Train the model locally:

```bash
python src/train.py
```

This will output the accuracy and save the trained model as `model.joblib`.

---

## 🧪 Running Tests

Run unit tests using **pytest**:

```bash
pytest test_train.py
```

The test ensures model accuracy is above `0.7`.

---

## ⚡ CI Workflow

The project uses **GitHub Actions** to automate testing on every push or pull request to the `main` branch.  

`.github/workflows/ci.yaml`:

```yaml
name: CI Workflow

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: pytest test_train.py
```

---

## 💻 Tech Stack
- Python 3.9  
- Scikit-learn  
- Joblib  
- Pytest  
- GitHub Actions  

---

## 👤 Author
- **Your Name**  
- GitHub: [@Shayan03447](https://github.com/Shayan03447)  

---

## 📜 License
This project is licensed under the MIT License.  

