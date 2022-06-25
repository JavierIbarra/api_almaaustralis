FROM python:3.9.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./almaaustralis/ .
COPY ./requirements.txt .
EXPOSE 5000
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]