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

## 🚀 How to Run Locally

To run this project on your own machine, you will first need Docker Desktop installed (https://www.docker.com/products/docker-desktop/).


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

## ☁️ Online Deployment

If you don't want to install anything, I also deployed the app online. You can try it [here](https://ebm9uhz3xtkdxtruf5kwri.streamlit.app/).

It is split into two services:

- the **FastAPI server** is hosted on [Render](https://render.com) (built from `server/Dockerfile`)
- the **Streamlit client** is hosted on [Streamlit Community Cloud](https://streamlit.io/cloud)

Both redeploy automatically on every push to `main`. The client finds the API through the `API_URL` setting (environment variable or Streamlit secret).

> ⏳ The API runs on Render's free tier and goes to sleep after about 15 minutes of inactivity. The first prediction may take 30 to 60 seconds while it wakes up.

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
