FROM joyzoursky/python-chromedriver:latest
COPY requirnments.txt requirnments.txt
RUN pip3 install -r requirnments.txt
COPY . /app
CMD ["uvicorn", "app.main:app", "--reload"]  
