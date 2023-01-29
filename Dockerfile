FROM python:3.8
WORKDIR /app/
COPY requiremnts.txt /app/
RUN pip3 install --upgrade pip
RUN pip3 install -r requiremnts.txt
COPY ./core/ /app/
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]