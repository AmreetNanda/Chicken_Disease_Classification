# Chicken Disease Classification App (Deep Learning + Flask + Docker)

The Chicken Disease Classification Web App is an interactive, user-friendly tool that detects chicken diseases from uploaded images using a deep learning model. This project demonstrates how a machine learning model can be integrated with a web interface to provide an intuitive experience for poultry farmers and enthusiasts who want to identify diseases quickly and accurately.

It includes:
- A complete deep learning prediction pipeline
- A Flask web interface for uploading images and getting predictions
- A fully modular ML codebase
- Optional Docker container for deployment
---

## Features

- **Image Upload Form:** Users can upload a chicken image for classification.
- **Deep Learning Classification:** The application predicts the disease type based on the uploaded image.
- **User-Friendly Interface:** Provides prediction results in big, readable format.
- **Disease Information:** Displays detailed info about common chicken diseases including symptoms and treatments.

## Diseases Detected:
- **Coccidiosis:** Diarrhea, weight loss, weakness. Treatment: Anticoccidial medication, good hygiene.
- **New Castle Disease:** Respiratory distress, nervous signs, reduced egg production. Treatment: Vaccination, supportive care.
- **Salmonella:** Diarrhea, reduced growth, lethargy. Treatment: Antibiotics, proper sanitation.
- **Healthy:** Normal behavior and appearance. Treatment: Maintain good care.

## Technologies Used:
- **Front-End:** HTML, CSS, Bootstrap
- **Back-End:** Python (Flask framework)
- **Deep Learning for image classification:** 
  - VGG16
  - Optimizers: Adam
  - Trained models for detecting chicken diseases

## Project Structure

```bash
Chicken-Disease-Classification/
│
├── app.py # Flask app
├── chicken_disease_classifier/ # Modular ML package
│ ├── config
│ │   └──config.yaml
│ ├── Research
│ ├── models
│ │   ├── H5_model/
│ │   │   └── trained_model.h5
│ │   ├── Reports/
│ │   │   └── evaluation_reports.csv
│ ├── src
│ │   ├── __init__.py
│ │   ├── components
│ │   │   ├── __init__.py
│ │   │   ├── data_ingestion.py
│ │   │   ├── prepare_base_model.py
│ │   │   ├── prepare_callbacks.py
│ │   │   ├── training.py
│ │   │   └── evaluation.py
│ │   │   ├── config
│ │   │   │   ├── __init__.py
│ │   │   │   ├── configuration.py
│ │   │   ├── constants
│ │   │   │   ├── __init__.py
│ │   │   ├── entity
│ │   │   │   ├── __init__.py
│ │   │   │   ├── config_entity.py
│ │   │   ├── pipeline
│ │   │   │   ├── __init__.py
│ │   │   │   ├── predict.py
│ │   │   │   ├── stage_01_data_ingestion.py
│ │   │   │   ├── stage_02_prepare_base_model.py
│ │   │   │   ├── stage_03_training.py
│ │   │   │   └── stage_04_evaluation.py
│ │   │   ├── utils
│ │   │   │   ├── __init__.py
│ │   │   │   └── common.py
├── templates
│   └── result.html
├── template.py
├── params.yaml
├── requirements.txt # Python dependencies
├── Dockerfile # Docker container
├── run.sh # Optional to run the script
└── setup.py # Optional

## Installation

## 🛠 Installation (without Docker)

### 1. Clone the repo
```bash
git clone https://github.com/AmreetNanda/Chicken_Disease_Classification.git
cd Chicken_Disease_Classification
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Flask app
```bash
run app.py
```
Open in your browser:
👉 http://127.0.0.1:8080/
👉 Click on "Upload image"
👉 Select the image to load
👉 Click the "Predict" button.
👉 Receive the predicted skin disease

## 🐳 Running with Docker (optional)
### Build the image
```bash
docker build -t Chicken_Disease_Classification .

```

### Run the container
```bash
docker run -p 8501:8501 Chicken_Disease_Classification

```
Open: 👉 http://localhost:8501

## Screenshots

##### Home page
![App Screenshot](https://github.com/AmreetNanda/Chicken_Disease_Classification/blob/main/Chicken_disease_classification.png)

## Demo video


## License

[MIT](https://choosealicense.com/licenses/mit/)