FROM python:3.11.6-slim
WORKDIR /TorneoFutbol
COPY . /TorneoFutbol
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
