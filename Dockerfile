FROM python:3

RUN pip install req.txt

CMD [ "python3", "./main.py" ]