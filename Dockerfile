FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install flask requests

EXPOSE 5000

CMD ["python", "-m", "app.main"]
