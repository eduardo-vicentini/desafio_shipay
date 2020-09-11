# Start with a base image
FROM python:3-onbuild
# Copy our application code
WORKDIR /var/application
COPY . .
COPY requirements.txt .
# Fetch app specific dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get -y update
RUN apt-get install -y sqlite3 libsqlite3-dev
# Expose port
EXPOSE 5000
# Start the app
CMD ["gunicorn", "application:app", "--bind", "0.0.0.0:5000"]