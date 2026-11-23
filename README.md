# 🌱 Crop Recommendation System



## 🌐 Live Demo

[🚀 Visit Live Website](https://crop-recommendation-system-9qsp.onrender.com)

A Machine Learning-based Crop Recommendation System built using Python, Django, and Scikit-learn. The application helps users identify suitable crops based on soil nutrients and environmental conditions.

## 📌 Project Overview

The Crop Recommendation System analyzes important agricultural parameters and recommends the most suitable crop using trained Machine Learning algorithms.

Users can register, log in, submit soil and weather parameters, view crop predictions, and maintain their prediction history.

## ✨ Features

* User Registration and Login
* Interactive Dashboard
* Crop Recommendation based on agricultural parameters
* Five Machine Learning algorithms
* Prediction Results with input parameters
* Prediction History
* Crop Information
* About and Help section
* Database integration using Django

## 🧠 Machine Learning Algorithms

The project implements five classification algorithms:

1. Random Forest
2. Decision Tree
3. Naive Bayes
4. Support Vector Machine (SVM)
5. K-Nearest Neighbors (KNN)

The system compares model performance and uses the best-performing algorithm for crop prediction.

## 📊 Dataset

The project uses the Crop Recommendation Dataset containing 2,200 records.

**Input Features:**

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* Soil pH
* Rainfall

**Output:** Recommended crop.

## 🛠️ Technologies Used

* Python
* Django
* Scikit-learn
* Pandas
* NumPy
* HTML
* CSS
* JavaScript
* SQLite
* Joblib

## 📁 Project Structure

```text
Crop-Recommendation-System/
│
├── app/
│   ├── migrations/
│   ├── templates/
│   ├── ml_model.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── crop_app/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── Crop_recommendation.csv
├── trained_crop_models.joblib
├── manage.py
└── requirements.txt
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/Subham1636/Crop-Recommendation-System.git
cd Crop-Recommendation-System
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate the environment**

Windows:

```bash
venv\Scripts\activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Apply database migrations**

```bash
python manage.py migrate
```

**6. Run the Django development server**

```bash
python manage.py runserver
```

**7. Open the application**

```text
http://127.0.0.1:8000/
```

## 🔮 Future Enhancements

* Weather API integration
* Multilingual support
* More agricultural datasets
* Cloud deployment
* Additional crop insights



---

⭐ If you find this project useful, consider giving the repository a star!
