FROM python:alpine3.19
RUN apk update
RUN apk add git
RUN pip install flask
RUN git clone https://github.com/Nathekip/API_microservice.git
EXPOSE 5000
CMD python /root/API_microservice/api_medal.py
