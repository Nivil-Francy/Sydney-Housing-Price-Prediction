# Sydney Housing Price Prediction and Decision Support System

## Project Overview

This project develops a machine learning system for predicting residential property sale prices in selected Sydney suburbs.

The project uses property data from:

* Beverly Hills
* Concord
* Castle Hill

The dataset contains 105 sold properties with information about suburb, property type, bedrooms, bathrooms, sale date and sale price.

The project covers the complete machine learning workflow, including data cleaning, exploratory data analysis, feature engineering, model development, evaluation, prediction-error analysis and deployment using Streamlit.

## Machine Learning Models

Three regression models were evaluated:

1. Linear Regression
2. Random Forest Regression
3. Gradient Boosting Regression

Five-fold cross-validation was used to compare the models using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² score

### Model Results

| Model             |         MAE |        RMSE |    R² |
| ----------------- | ----------: | ----------: | ----: |
| Linear Regression | $436,180.57 | $559,891.19 | 0.742 |
| Random Forest     | $340,531.14 | $456,809.88 | 0.823 |
| Gradient Boosting | $328,845.40 | $456,524.43 | 0.824 |

Gradient Boosting was selected as the final model because it achieved the lowest MAE and RMSE and the highest R² during cross-validation.

## Features

The final model uses:

* Suburb
* Property type
* Bedrooms
* Bathrooms
* Total rooms

total_rooms is an feature calculated by adding the number of bedrooms and bathrooms.

## Streamlit Application

The project includes a Streamlit web application that allows users to enter property characteristics and receive an estimated sale price.

The application allows the user to:

1. Select a suburb.
2. Select a property type.
3. Enter the number of bedrooms.
4. Enter the number of bathrooms.
5. Click Predict Sale Price.
6. View the estimated sale price.

## How to Run the Application

### 1. Download or clone the repository

```bash
git clone https://github.com/Nivil-Francy/Sydney-Housing-Price-Prediction.git
```

### 2. Open the project directory

```bash
cd Sydney-Housing-Price-Prediction
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in a web browser using the local Streamlit address provided in the terminal.

## Project Files

| File                           | Description                                                              |
| ------------------------------ | ------------------------------------------------------------------------ |
| 8.1D.ipynb                     | Main project notebook containing data analysis and machine learning work |
| app.ipynb                      | Application/model development notebook                                   |
| app.py                         | Streamlit web application                                                |
| sydney_housing.csv             | Housing dataset containing 105 property records                          |
| housing_price_model.pkl        | Trained Gradient Boosting model                                          |
| model_comparison_results.csv   | Cross-validation results for the three models                            |
| requirements.txt               | Python packages required to run the application                          |
| README.md                      | Project documentation                                                    |

## Dataset

The dataset contains 105 property sales:

* 35 properties from Beverly Hills
* 35 properties from Concord
* 35 properties from Castle Hill

The dataset includes property characteristics such as property type, bedrooms, bathrooms, sale date and sale price.

## Limitations

The dataset is relatively small and covers only three suburbs. Important property characteristics such as land size, floor area, parking, renovation quality, property condition and exact location are not included.

Therefore, the model predictions should be treated as estimates and decision-support information rather than formal property valuations.

## Future Improvements

Future improvements could include:

* Collecting a larger dataset.
* Including more Sydney suburbs.
* Adding land size and floor area.
* Including parking information.
* Adding geographic coordinates.
* Including distance to schools, transport and amenities.
* Using a longer historical period.
* Performing additional hyperparameter tuning.
* Testing additional machine learning algorithms.

## Author

**Nivil Francy**
