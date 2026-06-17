# ...existing code...
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import numpy as np
# Added ML imports
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score
import joblib
# ...existing code...

def generate_sample_data(n_records=1000):
    """Generate sample car sales data"""
    np.random.seed(42)
    
    dates = [datetime(2022, 1, 1) + timedelta(days=x) for x in range(730)]
    data = {
        'Date': np.random.choice(dates, n_records),
        'CarType': np.random.choice(['Sedan', 'SUV', 'Truck', 'Coupe', 'Hatchback'], n_records),
        'Color': np.random.choice(['White', 'Black', 'Silver', 'Red', 'Blue', 'Gray'], n_records),
        'Region': np.random.choice(['North', 'South', 'East', 'West', 'Central'], n_records),
        'Price': np.random.randint(20000, 80000, n_records),
        'Engine': np.random.choice(['2.0L', '2.5L', '3.0L', '3.5L'], n_records),
        'Transmission': np.random.choice(['Manual', 'Automatic', 'CVT'], n_records),
    }
    
    return pd.DataFrame(data)

# ...existing code...
# (rest of file unchanged)
# ...existing code...

# ===== ML TRAINING =====
def train_price_model(df, save_path=None, random_state=42):
    """
    Train a model to predict Price from categorical and simple numeric features.
    Returns: (pipeline, rmse, r2)
    """
    df_ml = df.copy()
    # convert date to numeric feature
    df_ml['DaysSince'] = (df_ml['Date'] - df_ml['Date'].min()).dt.days

    feature_cols = ['CarType', 'Color', 'Region', 'Engine', 'Transmission', 'DaysSince']
    X = df_ml[feature_cols]
    y = df_ml['Price']

    cat_feats = ['CarType', 'Color', 'Region', 'Engine', 'Transmission']
    num_feats = ['DaysSince']

    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    preprocessor = ColumnTransformer([
        ('num', num_pipeline, num_feats),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse=False), cat_feats)
    ])

    pipeline = Pipeline([
        ('pre', preprocessor),
        ('model', RandomForestRegressor(n_estimators=100, random_state=random_state, n_jobs=-1))
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)

    pipeline.fit(X_train, y_train)
    preds = pipeline.predict(X_test)

    rmse = mean_squared_error(y_test, preds, squared=False)
    r2 = r2_score(y_test, preds)

    print(f"ML Training completed — RMSE: ${rmse:,.2f}, R2: {r2:.3f}")

    if save_path:
        joblib.dump(pipeline, save_path)
        print(f"Model saved to: {save_path}")

    return pipeline, rmse, r2

if __name__ == "__main__":
    # assuming df is defined earlier in the script
    try:
        model, rmse, r2 = train_price_model(df, save_path='price_model.joblib')
    except NameError:
        print("Dataframe 'df' not found. Run data loading section first.")
# ...existing code...
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import numpy as np
# Added ML imports
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score
import joblib
# ...existing code...

def generate_sample_data(n_records=1000):
    """Generate sample car sales data"""
    np.random.seed(42)
    
    dates = [datetime(2022, 1, 1) + timedelta(days=x) for x in range(730)]
    data = {
        'Date': np.random.choice(dates, n_records),
        'CarType': np.random.choice(['Sedan', 'SUV', 'Truck', 'Coupe', 'Hatchback'], n_records),
        'Color': np.random.choice(['White', 'Black', 'Silver', 'Red', 'Blue', 'Gray'], n_records),
        'Region': np.random.choice(['North', 'South', 'East', 'West', 'Central'], n_records),
        'Price': np.random.randint(20000, 80000, n_records),
        'Engine': np.random.choice(['2.0L', '2.5L', '3.0L', '3.5L'], n_records),
        'Transmission': np.random.choice(['Manual', 'Automatic', 'CVT'], n_records),
    }
    
    return pd.DataFrame(data)

# ...existing code...
# (rest of file unchanged)
# ...existing code...

# ===== ML TRAINING =====
def train_price_model(df, save_path=None, random_state=42):
    """
    Train a model to predict Price from categorical and simple numeric features.
    Returns: (pipeline, rmse, r2)
    """
    df_ml = df.copy()
    # convert date to numeric feature
    df_ml['DaysSince'] = (df_ml['Date'] - df_ml['Date'].min()).dt.days

    feature_cols = ['CarType', 'Color', 'Region', 'Engine', 'Transmission', 'DaysSince']
    X = df_ml[feature_cols]
    y = df_ml['Price']

    cat_feats = ['CarType', 'Color', 'Region', 'Engine', 'Transmission']
    num_feats = ['DaysSince']

    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    preprocessor = ColumnTransformer([
        ('num', num_pipeline, num_feats),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse=False), cat_feats)
    ])

    pipeline = Pipeline([
        ('pre', preprocessor),
        ('model', RandomForestRegressor(n_estimators=100, random_state=random_state, n_jobs=-1))
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)

    pipeline.fit(X_train, y_train)
    preds = pipeline.predict(X_test)

    rmse = mean_squared_error(y_test, preds, squared=False)
    r2 = r2_score(y_test, preds)

    print(f"ML Training completed — RMSE: ${rmse:,.2f}, R2: {r2:.3f}")

    if save_path:
        joblib.dump(pipeline, save_path)
        print(f"Model saved to: {save_path}")

    return pipeline, rmse, r2

if __name__ == "__main__":
    # assuming df is defined earlier in the script
    try:
        model, rmse, r2 = train_price_model(df, save_path='price_model.joblib')
    except NameError:
        print("Dataframe 'df' not found. Run data generation first.")