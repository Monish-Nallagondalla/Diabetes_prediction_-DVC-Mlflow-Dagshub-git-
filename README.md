# Diabetes Prediction with DVC, MLflow, DagsHub, and Git

This repository contains a machine learning pipeline for predicting diabetes outcomes using a dataset of patient features. The project integrates [DVC](https://dvc.org/) for data version control, [MLflow](https://mlflow.org/) for experiment tracking, and [DagsHub](https://dagshub.com/) for hosting the repository and MLflow experiments. The pipeline is versioned using Git and hosted on both [GitHub](https://github.com/Monish-Nallagondalla/Diabetes_prediction_-DVC-Mlflow-Dagshub-git-) and [DagsHub](https://dagshub.com/Monish-Nallagondalla/Diabetes_prediction_-DVC-Mlflow-Dagshub-git-).

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [MLflow Integration](#mlflow-integration)
- [DVC Integration](#dvc-integration)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
The Diabetes Prediction project builds a machine learning model to predict whether a patient has diabetes based on medical features. The pipeline includes data preprocessing, model training, and evaluation, with versioning of data and models using DVC. MLflow tracks experiments, and DagsHub serves as a central hub for collaboration, data storage, and experiment visualization.

## Features
- **Data Preprocessing**: Cleans and prepares the dataset for model training.
- **Model Training**: Trains a machine learning model using scikit-learn.
- **Model Evaluation**: Evaluates model performance using relevant metrics.
- **DVC for Versioning**: Tracks data and model versions with DVC, integrated with S3 for storage.
- **MLflow for Experiment Tracking**: Logs parameters, metrics, and models to MLflow on DagsHub.
- **Git Integration**: Manages code versioning with Git on GitHub and DagsHub.

## Dataset
The dataset (`data.csv`) contains medical features for predicting diabetes, including:
- `Pregnancies`: Number of pregnancies
- `Glucose`: Plasma glucose concentration
- `BloodPressure`: Diastolic blood pressure (mm Hg)
- `SkinThickness`: Triceps skin fold thickness (mm)
- `Insulin`: 2-Hour serum insulin (mu U/ml)
- `BMI`: Body mass index
- `DiabetesPedigreeFunction`: Diabetes pedigree function
- `Age`: Age (years)
- `Outcome`: Target variable (0 = non-diabetic, 1 = diabetic)

The dataset is stored in the `data/raw/` directory and versioned using DVC.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Monish-Nallagondalla/Diabetes_prediction_-DVC-Mlflow-Dagshub-git-.git
   cd Diabetes_prediction_-DVC-Mlflow-Dagshub-git-
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` includes:
   ```
   dvc
   dagshub
   scikit-learn
   mlflow
   dvc-s3
   ```

4. **Initialize DVC**:
   ```bash
   dvc init
   ```

5. **Set Up DVC Remote Storage** (optional, for S3):
   Configure an S3 bucket as the DVC remote:
   ```bash
   dvc remote add -d s3remote s3://your-bucket-name/path
   dvc remote modify s3remote access_key_id YOUR_AWS_ACCESS_KEY
   dvc remote modify s3remote secret_access_key YOUR_AWS_SECRET_KEY
   ```

6. **Pull Data**:
   Retrieve the versioned dataset:
   ```bash
   dvc pull
   ```

7. **Set Up MLflow**:
   Configure MLflow to track experiments on DagsHub:
   ```bash
   export MLFLOW_TRACKING_URI=https://dagshub.com/Monish-Nallagondalla/Diabetes_prediction_-DVC-Mlflow-Dagshub-git-.mlflow
   export MLFLOW_TRACKING_USERNAME=your-dagshub-username
   export MLFLOW_TRACKING_PASSWORD=your-dagshub-token
   ```

## Project Structure
```
Diabetes_prediction_-DVC-Mlflow-Dagshub-git-/
├── .dvcignore                # DVC ignore patterns
├── .gitignore                # Git ignore patterns
├── dvc.yaml                  # DVC pipeline configuration
├── LICENSE                   # License file
├── params.yaml               # Model and pipeline parameters
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── images/                   # Directory for images
│   ├── pipeline.png          # Pipeline diagram
├── data/                     # Dataset storage
│   ├── processed/            # Processed data
│   │   ├── .gitignore
│   ├── raw/                  # Raw data
│   │   ├── .gitignore
│   ├── data.csv.dvc          # DVC-tracked dataset
├── models/                   # Trained models
│   ├── model.pkl             # Saved model
├── src/                      # Source code
│   ├── __init__.py
│   ├── evaluate.py           # Model evaluation script
│   ├── preprocess.py         # Data preprocessing script
│   ├── train.py              # Model training script
```

## Usage
1. **Run the Pipeline**:
   Execute the DVC pipeline to preprocess data, train the model, and evaluate it:
   ```bash
   dvc repro
   ```

   The pipeline is defined in `dvc.yaml` and includes stages for preprocessing, training, and evaluation. The pipeline flow is illustrated below:

  ![image](https://github.com/user-attachments/assets/fbd0b9c6-82e2-484d-b176-f6fa35b2e66a)


   The diagram shows the following stages:
   - `data/raw/data.csv.dvc`: The raw dataset tracked by DVC.
   - `preprocess`: Runs `preprocess.py` to clean and prepare the data, outputting `data.csv` in the `processed/` directory.
   - `train`: Runs `train.py` to train the model using the processed data, outputting `model.pkl`.
   - `evaluate`: Runs `evaluate.py` to evaluate the model using the processed data and trained model.

2. **Track Experiments with MLflow**:
   The `train.py` and `evaluate.py` scripts log experiments to MLflow. After running the pipeline, view experiments on DagsHub:
   [https://dagshub.com/Monish-Nallagondalla/Diabetes_prediction_-DVC-Mlflow-Dagshub-git-/experiments](https://dagshub.com/Monish-Nallagondalla/Diabetes_prediction_-DVC-Mlflow-Dagshub-git-/experiments)

3. **Update Data or Models**:
   - To update the dataset, modify `data/raw/data.csv` and run:
     ```bash
     dvc add data/raw/data.csv
     git add data/raw/data.csv.dvc
     git commit -m "Update dataset"
     git push
     dvc push
     ```
   - To update the model, modify `src/train.py` or `params.yaml`, then rerun:
     ```bash
     dvc repro
     ```

## MLflow Integration
MLflow tracks experiments, including parameters, metrics, and models. All runs are logged to the DagsHub MLflow server. To view experiments:
1. Visit [https://dagshub.com/Monish-Nallagondalla/Diabetes_prediction_-DVC-Mlflow-Dagshub-git-](https://dagshub.com/Monish-Nallagondalla/Diabetes_prediction_-DVC-Mlflow-Dagshub-git-).
2. Navigate to the Experiments tab to explore logged runs, metrics, and artifacts.

## DVC Integration
DVC manages data and model versioning. The `data.csv` file is tracked with DVC, and processed data and models are stored in the `data/processed/` and `models/` directories, respectively. The pipeline is defined in `dvc.yaml`, with parameters in `params.yaml`. Use `dvc pull` and `dvc push` to sync data with the remote storage (e.g., S3).

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request on GitHub or DagsHub.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
