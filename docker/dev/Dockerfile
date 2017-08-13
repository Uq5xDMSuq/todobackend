FROM pluralsight/todobackend-base:latest
MAINTAINER Anonymous User

# Install dev/build dependencies
RUN apt-get update && \
    apt-get install -qy python-dev

# Activate virtual environment and install wheel support
RUN . /appenv/bin/activate && \
    pip install wheel --upgrade

# PIP environment variables (NOTE: must be set after installing wheel)
ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache

# OUTPUT: Build artefacts (Wheels) are output here
VOLUME /wheelhouse

# OUTPUT: Test reports are output here
VOLUME /reports

# Add test entrypoint script
COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

# Set defaults for entrypoint and command string
ENTRYPOINT ["test.sh"]
# This becomes the default arguments to the ENTRYPOINT shell script
CMD ["python", "manage.py", "test", "--noinput"]

# Add application source. Doing these as the last step because it will help
# with future caching. The previous steps won't change that much, but the
# application code will - so it can reuse the cache of all previous steps
# when building new images.
COPY src /application
WORKDIR /application

