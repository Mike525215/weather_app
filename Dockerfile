FROM python:3.8
WORKDIR weatherApp/
COPY . .
RUN pip install -r req.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]