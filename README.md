
# 📄 Bank Note Authentication API

This is a simple **Flask-based REST API** that authenticates whether a banknote is genuine or fake using a **Machine Learning classifier** trained on statistical features extracted from banknote images. The project is packaged with **Docker** for seamless deployment.

---

## 🚀 Features

- 🔍 Predict if a banknote is real or fake
- 📦 RESTful API using Flask
- 🧠 Pre-trained ML model (e.g., Logistic Regression or Random Forest)
- 🐳 Dockerized for easy deployment
- ✅ Simple and clean codebase for learning

---

## 🧠 Tech Stack

- Python 3.x
- Flask
- scikit-learn
- pandas, numpy
- Docker
- (Optional) Jupyter for model training

---

## 📁 Project Structure

```
.
├── Dockerfile
├── flask_api.py            # Main Flask app
├── requirements.txt        # Python dependencies
├── classifier.pkl          # Trained ML model
├── ModelTraining.ipynb     # Jupyter Notebook for training
└── TestFile.xlsx           # Sample data (if any)
```

---

## ⚙️ Installation (Without Docker)

```bash
# Step 1: Clone the repository
git clone https://github.com/your-username/banknote-auth-api.git
cd banknote-auth-api

# Step 2: Create a virtual environment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the Flask server
python flask_api.py
```

> The API will be running at `http://127.0.0.1:5000/`

---

## 🐳 Docker Setup (Recommended)

```bash
# Step 1: Build the Docker image
docker build -t money_api .

# Step 2: Run the container
docker run -p 5000:5000 money_api
```

> Access the API at `http://localhost:5000/`

---

## 🧪 API Usage

### 🔹 Endpoint: `/predict`

**Method:** `POST`  
**Content-Type:** `application/json`

### ✅ Sample Request:

```json
POST /predict
{
  "variance": 2.3,
  "skewness": 3.4,
  "curtosis": 1.5,
  "entropy": -2.2
}
```

### 🔄 Sample Curl:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"variance": 2.3, "skewness": 3.4, "curtosis": 1.5, "entropy": -2.2}'
```

### 🔙 Response:

```json
{
  "prediction": "Fake Note"
}
```

---

## 📈 Model Info

- Dataset: UCI ML Banknote Authentication Data Set
- Features:
  - Variance of Wavelet Transformed image
  - Skewness
  - Curtosis
  - Entropy
- Model: (e.g., Logistic Regression or Random Forest)
- Accuracy: ~99% on test set

---

## 📚 Sources & References

- [UCI Banknote Dataset](https://archive.ics.uci.edu/ml/datasets/banknote+authentication)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Docs](https://docs.docker.com/)

---

## 🙌 Credits

Made with ❤️ by [Your Name](https://github.com/your-username)
