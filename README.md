# 🌸 Iris Flower Classification with FastAPI & Streamlit

This project is a demonstration of an MLOps pipeline for predicting the class of an Iris flower. It consists of two main parts: a FastAPI server that hosts the machine learning model, and a Streamlit client that allows users to interact with the model via a web interface. Both parts are containerized using **Docker** for seamless deployment and local orchestration via **Docker Compose**.


---

## 📦 Project Structure

```
.
├── client/
│   ├── app.py              # Streamlit frontend
│   ├── image_iris.jpg      # Image of Iris flower species
│   ├── requirements.txt    # Client dependencies
│   └── Dockerfile
│
├── server/
│   ├── app.py              # FastAPI backend
│   ├── train.py            # Model training script
│   ├── model.pkl           # Trained model (pickle)
│   ├── requirements.txt    # Server dependencies
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

## 🚀 How to Run

To run this project, you will first need to have Docker Desktop installed on your machine (https://www.docker.com/products/docker-desktop/).


### 1. Clone the repo

```bash
git clone https://github.com/Linn2d/MLOps
cd MLOps
```
### 2. Build and run the full application

From the project root:

```bash
docker compose up --build
```

This will:
- Build the server and client Docker images
- Start the FastAPI server at `http://localhost:8000`
- Launch the Streamlit app at `http://localhost:8501`

---

## 🖼️ Interface Overview

- The Streamlit interface allows users to input 4 Iris flower features.
- An image shows the 3 Iris species (Setosa, Versicolor, Virginica).
- When clicking "Predict", it sends a request to the API and displays the predicted class.
  
![app](https://github.com/user-attachments/assets/e100a0b6-ff1e-45fe-ad3a-f4e26af5aaf5)

---

## 👤 Author

Built by [Linn2d](https://github.com/Linn2d) as a mini MLOps practice project.

---

## 📬 Contact

Feel free to open an issue or a pull request on the [GitHub repo](https://github.com/Linn2d/MLOps) if you have suggestions or improvements.
