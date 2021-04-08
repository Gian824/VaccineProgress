FROM python:3

WORKDIR VaccineProgress_test/
COPY . /VaccineProgress_test

EXPOSE 8080

RUN pip install -r requirements.txt
RUN pip install pandas
RUN pip install -U matplotlib
RUN pip install -U scikit-learn
RUN pip install ipython
RUN pip install simplejson

CMD ["make", "start"]
