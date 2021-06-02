FROM ruby:3.0.1-buster
LABEL Description="AB Tech Website"

ENV BUNDLE_APP_CONFIG=/usr/src/app/.bundle

# Install NodeJS and set Ruby dependency location (with bundler config file)
RUN export NODE_VERSION=node_14.x && \
    export NODE_DISTRO=buster && \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -  && \
    echo "deb https://deb.nodesource.com/$NODE_VERSION $NODE_DISTRO main" | tee /etc/apt/sources.list.d/nodesource.list && \
    echo "deb-src https://deb.nodesource.com/$NODE_VERSION $NODE_DISTRO main" | tee -a /etc/apt/sources.list.d/nodesource.list && \
    apt-get update -y && apt-get install -y nodejs=14.17.0-1nodesource1 && \
    bundle config set --local path vendor/bundle

WORKDIR /usr/src/app
VOLUME /usr/src/app

EXPOSE 35729
EXPOSE 4000
