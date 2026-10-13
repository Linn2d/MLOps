FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt
WORKDIR /app 

RUN pip install -r requirements.txt

COPY app.py app.py
COPY image_iris.png image_iris.png

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
