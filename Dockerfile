FROM ruby:3.0.1-buster
LABEL Description="AB Tech Website"

# Install node
RUN NODE_VERSION=node_14.x && \
    NODE_DISTRO=buster && \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -  && \
    echo "deb https://deb.nodesource.com/$NODE_VERSION $NODE_DISTRO main" | tee /etc/apt/sources.list.d/nodesource.list && \
    echo "deb-src https://deb.nodesource.com/$NODE_VERSION $NODE_DISTRO main" | tee -a /etc/apt/sources.list.d/nodesource.list && \
    apt-get update -y && apt-get install -y nodejs=14.17.0-1nodesource1

# throw errors if Gemfile has been modified since Gemfile.lock
#RUN bundle config --global frozen 1

WORKDIR /usr/src/app
VOLUME /usr/src/app

# COPY Gemfile Gemfile.lock ./
# RUN bundle install

# COPY . .

# CMD ["jekyll", "--help"]
EXPOSE 35729
EXPOSE 4000
