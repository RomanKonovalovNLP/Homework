# our base image
FROM python:3-onbuild

# specify the port number the container should expose
EXPOSE 5000

RUN pip install -Ur requirements.txt 
# run the application
CMD ["python3", "./app.py"]
