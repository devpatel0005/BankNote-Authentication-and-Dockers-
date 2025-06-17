
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
├── streamlit_app.py        # streamlit deployment
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
## Flask Output
![image](https://github.com/user-attachments/assets/2a64b2e9-6b06-4aeb-a096-294c374d2805)
![image](https://github.com/user-attachments/assets/8fd36693-757d-46ab-8fd0-36d1c3669e1f)
![image](https://github.com/user-attachments/assets/4017c689-67da-4524-a3ac-6bbad4800ed5)
![image](https://github.com/user-attachments/assets/b7476eb8-2a8f-40ca-8128-e3dbf488e72d)

## Streamlit Output
![image](https://github.com/user-attachments/assets/988be4c1-f9f1-44f3-a5d5-5c4b86c8d65e)
![image](https://github.com/user-attachments/assets/e235b552-05d7-45da-88f2-b59a8b612d56)


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

Made with ❤️ by [DEV PATEL](https://github.com/devpatel0005)
