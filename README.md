# README.md
# Material Classifier

The **Material Classifier** is a Python library that uses machine learning to classify materials based on their descriptions. It allows users to train a model on their data and classify unclassified materials, merging predictions with existing classification information.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
  - [Installing Dependencies](#installing-dependencies)
  - [Project Structure](#project-structure)
- [Usage](#usage)
  - [Training the Model](#training-the-model)
  - [Classifying Materials](#classifying-materials)
- [Customization Options](#customization-options)
- [Expected Outputs](#expected-outputs)
- [Troubleshooting](#troubleshooting)
- [Tests](#tests)
- [License](#license)

---

## Features

- Train a machine learning model using custom training data.
- Classify unclassified materials based on descriptions.
- Merge predictions with a classification matrix.
- Output results as a CSV file for further use.

---

## Requirements

- Python 3.8 or higher
- Libraries (install via `requirements.txt`):
  - pandas
  - scikit-learn
  - joblib

---

## Setup

### Installing Dependencies

1. Clone the repository:

   ```bash
   git clone https://github.com/Jeffa90/material_classifier.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

### Project Structure

```
material_classifier/
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
├── material_classifier/
│   ├── __init__.py
│   ├── classify_materials.py
│   ├── train_model.py
├── tests/
│   ├── __init__.py
│   ├── test_train_model.py
│   └── test_classify_materials.py
└── data/ (optional)
    ├── Training Data.csv
    ├── Unclassified Data.csv
    └── Classification Matrix.csv
```

---

## Usage

### Training the Model

Train a machine learning model using your custom training data.

1. Ensure your training data CSV is ready with the following columns:

   | Material Description | Classification Number |
   |----------------------|----------------------|
   | Steel pipe          | 1001                 |
   | Aluminum sheet      | 1002                 |
   | Copper wire        | 1003                 |

2. Run the training script:

   ```bash
   python material_classifier/train_model.py
   ```

3. The trained model will be saved as:
   - `model.joblib`
   - `label_encoder.joblib`

---

### Classifying Materials

Use the trained model to classify unclassified materials.

1. Prepare your unclassified data CSV with the following column:

   | Material Description |
   |----------------------|
   | Pipe Steel           |
   | Wire Copper          |

2. Run the classification script:

   ```bash
   python material_classifier/classify_materials.py
   ```

3. The script merges predictions with `Classification_Matrix.csv` and saves:
   - `Material_Predicted_Classifications.csv`

---

## Customization Options

1. **Change Model and Encoder Paths:**
   ```bash
   python train_model.py --model new_model.joblib --encoder new_encoder.joblib
   ```

2. **Change Output File Name:**
   ```bash
   python classify_materials.py --output my_classifications.csv
   ```

---

## Expected Outputs

### Classification Output

| Material Code | Material Description | Classification Code | Family  | Category | Sub-Category |
|-------------- |----------------------|---------------------|---------|----------|--------------|
| 001           | Pipe Steel           | 1001                | Metal   | Pipes    | Structural   |
| 002           | Wire Copper          | 1003                | Metal   | Wires    | Electrical   |

---

## Troubleshooting

### 1️⃣ `FileNotFoundError: Training Data.csv not found`
- Ensure the CSV file is in the correct directory (`data/` by default).
- Use `python train_model.py --data path/to/your/file.csv`.

### 2️⃣ `ValueError: CSV file must contain 'Material Description'`
- Ensure the input file has the required column headers.

### 3️⃣ `ModuleNotFoundError: No module named 'material_classifier'`
- Run `pip install .` inside the project directory.

---

## Tests

Run unit tests to verify functionality:

```bash
pytest tests/
```

---

## License

This project is not licensed. See the [LICENSE](LICENSE) file for details.
