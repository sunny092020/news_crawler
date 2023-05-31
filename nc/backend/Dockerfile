FROM python:3 AS builder
ENV PYTHONUNBUFFERED=1

# create directory for the app user
ENV HOME=/home/app
ENV APP_HOME=$HOME/web

RUN mkdir -p $HOME \
    mkdir $APP_HOME \
    mkdir $APP_HOME/staticfiles \
    mkdir $APP_HOME/mediafiles

WORKDIR $APP_HOME

COPY ./requirements.txt $APP_HOME
RUN pip install -r requirements.txt

FROM python:3-slim

EXPOSE 8000

# create directory for the app user
ENV HOME=/home/app
ENV APP_HOME=$HOME/web

COPY --from=builder $HOME $HOME
COPY --from=builder /usr/local/ /usr/local/

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

RUN ldconfig /usr/local/lib
WORKDIR $APP_HOME

COPY . $APP_HOME
