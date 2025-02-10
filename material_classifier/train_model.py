import pandas as pd
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from joblib import dump
import os

def train_material_classifier(
    data_path="Training_Data.csv",
    model_output="model.joblib",
    encoder_output="label_encoder.joblib"
):
    """Train a material classification model from a CSV file and save locally."""
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Error: Training data file '{data_path}' not found.")
    
    print(f"📥 Loading training data from '{data_path}'...")
    train_df = pd.read_csv(data_path)

    # Validate required columns exist
    required_columns = ["Material Description", "Classification Number"]
    for col in required_columns:
        if col not in train_df.columns:
            raise ValueError(f"Error: '{col}' column is missing from training data.")

    # Encode labels
    print("🔢 Encoding classification labels...")
    label_encoder = LabelEncoder()
    train_df["subcategory_encoded"] = label_encoder.fit_transform(train_df["Classification Number"])

    # Define model pipeline
    pipeline = Pipeline([
        ('vectorizer', HashingVectorizer(n_features=2**20)),
        ('clf', LinearSVC())
    ])

    print("🎯 Training the model...")
    X_train = train_df["Material Description"]
    y_train = train_df["subcategory_encoded"]
    pipeline.fit(X_train, y_train)

    # Save the trained model and label encoder
    print(f"💾 Saving trained model to '{model_output}' and encoder to '{encoder_output}'...")
    dump(pipeline, model_output)
    dump(label_encoder, encoder_output)

    print("✅ Training complete! Model and encoder saved successfully.")

# Example usage
if __name__ == "__main__":
    train_material_classifier("Training_Data.csv")
