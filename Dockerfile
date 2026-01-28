FROM python:3.10-slim
WORKDIR /app-flask
RUN pip install flask
COPY . .
EXPOSE 5000
CMD ["Python", "app.py"]
