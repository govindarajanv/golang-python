FROM python:3.7
RUN mkdir /src
ADD . /src
RUN pip install kopf
RUN pip install kubernetes
CMD kopf run /src/ephemeral.py --verbose