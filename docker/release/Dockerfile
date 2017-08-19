FROM 4e82p7d6p872/todobackend-base:latest
MAINTAINER Anonymous User

# Copy application artifacts
COPY target /wheelhouse

# Install application
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse todobackend && \
    rm -rf /wheelhouse
