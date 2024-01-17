FROM node:python:3.7.0

WORKDIR /usr/src/app
RUN pip install Flask && pip install pandas && pip install xlrd

COPY . .

EXPOSE 5000
CMD [ "python", "main.py" ]