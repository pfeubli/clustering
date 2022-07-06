FROM python:3.8

ADD clustering_algorithm.py .
ADD helper_functions.py .
ADD requirements.txt .
ADD Data .

RUN pip install pandas

CMD [ "python", "./clustering_algorithm.py"]
