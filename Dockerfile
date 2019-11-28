FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /amika-backend
COPY requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 8000