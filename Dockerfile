FROM node:python:3.10.13-slim

WORKDIR /usr/src/app
RUN pip install Flask && pip install pandas && pip install xlrd

COPY . .

EXPOSE 5000
CMD [ "python", "main.py" ]