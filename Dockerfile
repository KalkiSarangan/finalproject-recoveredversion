# define base image
FROM python:3.8

WORKDIR /app

# copy all the files to the container WORKDIR
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose port for web app
EXPOSE 5000

# write the command for running the application
CMD gunicorn -b 0.0.0.0:5000 app:app --timeout 600
