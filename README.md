# Diabetes Prediction App

This project is a machine learning-based web application for predicting the likelihood of diabetes in a patient. It consists of a **FastAPI backend** for serving predictions and a **Streamlit frontend** for user interaction.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup Instructions](#setup-instructions)
5. [Running the Application](#running-the-application)
6. [API Endpoints](#api-endpoints)
7. [Validation Rules](#validation-rules)
8. [Contributing](#contributing)
9. [License](#license)

---

## Project Overview
The Diabetes Prediction App uses a **Random Forest Classifier** trained on the Pima Indians Diabetes Dataset to predict whether a patient has diabetes based on input features such as glucose level, blood pressure, BMI, etc. The app consists of:
- A **FastAPI backend** that serves predictions via an API endpoint.
- A **Streamlit frontend** that provides a user-friendly interface for inputting data and viewing predictions.

---

## Features
- **User-friendly interface**: Input patient data and get predictions in real-time.
- **Validation**: Ensures input values are within specified ranges.
- **Scalability**: The backend can handle multiple requests simultaneously.
- **CORS Support**: Allows the frontend to communicate with the backend seamlessly.

---

## Technologies Used
- **Python**: Primary programming language.
- **FastAPI**: Backend framework for serving predictions.
- **Streamlit**: Frontend framework for building the user interface.
- **Scikit-learn**: Machine learning library for training the Random Forest model.
- **Joblib**: For saving and loading the trained model and scaler.
- **NumPy**: For numerical computations.

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/diabetes_assim.git
cd diabetes_assim
