import pandas as pd
from joblib import load

def classify_materials(
    input_csv, 
    classification_matrix_csv, 
    output_csv="Material_Predictions.csv", 
    model_path="model.joblib", 
    encoder_path="label_encoder.joblib"
):
    """Classify materials from a CSV file and merge with a classification matrix."""
    
    # Load trained model and label encoder
    print("Loading the trained model and label encoder...")
    pipeline = load(model_path)
    label_encoder = load(encoder_path)

    # Read the input CSV file (unclassified materials)
    print(f"Reading unclassified data from {input_csv}...")
    test_df = pd.read_csv(input_csv)

    if "Material Description" not in test_df.columns:
        raise ValueError("CSV file must contain a 'Material Description' column.")

    # Predict classifications
    X_test = test_df["Material Description"]
    y_pred_encoded = pipeline.predict(X_test)
    y_pred = label_encoder.inverse_transform(y_pred_encoded)

    # Add predictions to DataFrame
    test_df["Predicted Classification"] = y_pred

    # Load classification matrix (if provided)
    try:
        print(f"Loading classification matrix from {classification_matrix_csv}...")
        classification_info_df = pd.read_csv(classification_matrix_csv)

        if "Classification Code" not in classification_info_df.columns:
            raise ValueError("Classification Matrix CSV must contain a 'Classification Code' column.")

        # Merge classification matrix with predictions
        combined_df = classification_info_df.merge(
            test_df, how="inner", left_on="Classification Code", right_on="Predicted Classification"
        )

        # Define column order
        columns_order = ["Material Code", "Material Description", "Classification Code", "Family", "Category", "Sub-Category"]
        combined_df = combined_df[columns_order]

        # Save the results to a CSV file
        print(f"Saving classified data to {output_csv}...")
        combined_df.to_csv(output_csv, index=False)
    
    except FileNotFoundError:
        print(f"Warning: Classification matrix file '{classification_matrix_csv}' not found. Saving predictions without merging.")
        test_df.to_csv(output_csv, index=False)

    print("Classification complete. Output saved.")

# Example usage
if __name__ == "__main__":
    classify_materials("Unclassified_Data.csv", "Classification_Matrix.csv")
