FROM python:3.9-slim
RUN pip install pika
COPY hello.py .
COPY receive.py .  
CMD ["python", "hello.py"]
