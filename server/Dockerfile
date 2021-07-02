#####################
#		Base		#
#####################
FROM python:3.8-slim-buster as base

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# Installing dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# With docker-compose, this copy will be overrindden by volume.
COPY . .

# With docker-compose, this entry point will be overridden.
CMD ["python", "src/main.py"]

#####################
#		Dev			#
#####################
FROM base as dev

# Installing dev-dependencies
COPY requirements.dev.txt ./
RUN pip install --no-cache-dir -r requirements.dev.txt

# With docker-compose, this port will be overridden.
EXPOSE 5678

# With docker-compose, this entry point will be overridden.
CMD ["sh", "-c", "python -m debugpy --wait-for-client --listen 0.0.0.0:5678 src/main.py"]

#####################
#	Production		#
#####################
FROM base as production

# With docker-compose, this entry point will be overridden.
CMD ["python", "src/main.py"]