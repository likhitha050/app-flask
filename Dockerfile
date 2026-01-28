FROM python:3.10-slim
WORKDIR /app-flask
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt
COPY . .
EXPOSE 5000
CMD ["python","app.py"]
