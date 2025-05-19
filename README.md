# 🚀 House Price Prediction Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24%2B-orange)  
![License](https://img.shields.io/badge/License-MIT-green)  

**House Price Prediction Project** is a machine-learning pipeline that selects among multiple regressors to forecast real estate values. We compare Linear Regression, Decision Tree and Random Forest models—and deploy the top performer (Random Forest) for inference.

> “Predict home values with precision—and turn data into decisions.”

---

## 🔍 Features

- **Model Selection Pipeline**  
Maps three algorithms:
```python
_map = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "Decision Tree": DecisionTreeRegressor(max_depth=4, random_state=42)
}
```

- **Best Performer:** 
```bash
Random Forest
Used RandomForestRegressor(n_estimators=100, random_state=42) for final predictions.
```

## 🛠️ Installation & Usage

1. Clone The Repo

```bash
git clone https://github.com/fatimesevilgen/house-price-prediction-app.git
cd house-price-prediction-app
```

2. (Optional) Create & activate a virtual environment

```bash
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run app

```bash
streamlit run app.py
```

## 📁 Project Structure

```bash
house-price-prediction-app/
    ├── predict.py                   # Predict method with model
    ├── app.py                       # Streamlit application code
    ├── housing_model.joblib         # Trained MultinomialNB model
    ├── requirements.txt             # Python dependencies
    └── README.md                    # This file
```

## 🤝 Contributing

1. Fork this repository

2. Create a feature branch (git checkout -b feature/awesome-new)

3. Commit your changes (git commit -m "Add awesome new feature")

4. Push to your branch (git push origin feature/awesome-new)

5. Open a Pull Request 🚀

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 📬 Contact
Questions, suggestions, or just want to say hi?

- [Email](fatimesevilen@gmail.com)
- [Linkedin](https://www.linkedin.com/in/fatimesevilgen1/)
- [Github](https://github.com/fatimesevilgen)