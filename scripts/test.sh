#!/bin/bash
# Activate virtual environment
. /appenv/bin/activate

# Download requirements to build cache. This tells pip to 
# download all dependencies to the /build folder.
pip download -d /build -r requirements_test.txt --no-input

# Install application test requirements. --no-index tells
# not to attempt to download external dependencies. Instead
# get all dependencies from the /build folder
pip install --no-index -f /build -r requirements_test.txt

# Run test.sh arguments
exec $@
