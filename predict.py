import joblib
import pandas as pd

model = joblib.load("housing_model.pkl")

def predict(**kwargs):
    """
    Ev fiyatı tahmini yapan fonksiyon.
    
    Args:
        kwargs: Ev özellikleri (CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT)
    
    Returns:
        float: Tahmin edilen ev fiyatı
    """
    # DataFrame’e dönüştür
    X_new = pd.DataFrame([kwargs])
    
    # Tahmin
    price = model.predict(X_new)[0]
    return price