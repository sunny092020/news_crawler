# We're using the python image as a base
FROM python:3.8-slim-buster

# Updating apt-get and installing required packages to install Google Chrome and Chromedriver
RUN apt-get update \
  && apt-get install -y curl unzip gnupg

# Chrome browser to get the proper user agent when making requests
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o google-chrome-stable_current_amd64.deb \
  && dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# Chromedriver to simulate a user in the selenium browser
RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` \
  && echo "Installing chromium webdriver version ${LATEST}" \
  && curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip \
  && unzip chromedriver_linux64.zip \
  && mv chromedriver /usr/bin/chromedriver \
  && chown root:root /usr/bin/chromedriver \
  && chmod +x /usr/bin/chromedriver \
  && rm chromedriver_linux64.zip

# Setting the Python Buffering: This sets Python’s stdin, stdout and stderr to be totally unbuffered.
ENV PYTHONUNBUFFERED 1

# Setting the working directory in the container
WORKDIR /app

# Copying the requirements file to the Docker container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying the rest of the application to the Docker container
COPY . .

EXPOSE 8000
