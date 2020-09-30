FROM python
WORKDIR /usr/app/
COPY /app /usr/app/
RUN pip install flask
EXPOSE 80
CMD python counter-service.py 
