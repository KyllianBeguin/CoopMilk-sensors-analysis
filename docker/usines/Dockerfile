FROM python

COPY automates_type ./automates_type

COPY generate_data.py ./generate_data.py

COPY rules_coopmilk.csv ./rules_coopmilk.csv

RUN pip install pandas

CMD [ "python3", "./generate_data.py" ]