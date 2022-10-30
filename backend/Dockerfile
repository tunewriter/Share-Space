#
FROM python:3.10

#
WORKDIR /code

#
RUN pip install --upgrade pip
RUN pip3 install uvicorn fastapi supabase pytest python-dotenv

#
COPY ./app /code/app

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]