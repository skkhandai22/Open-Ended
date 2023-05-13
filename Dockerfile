FROM python:3.10

WORKDIR /app

COPY . /app

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

ENTRYPOINT ["streamlit", "run"]

CMD ["main.py"]