import pandas as pd

def load_data(file_path):
    """
    Loads a dataset from the given file path.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: Loaded dataset.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        raise
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        raise

def preprocess_data(data, target_column):
    """
    Splits data into features and target.

    Args:
        data (pandas.DataFrame): The dataset to process.
        target_column (str): The name of the target column.

    Returns:
        tuple: (features, target)
    """
    X = data.drop(columns=[target_column])
    y = data[target_column]
    print("Data preprocessing completed.")
    return X, y
