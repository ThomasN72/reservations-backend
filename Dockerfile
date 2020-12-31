FROM python:3.7-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends

# Python won’t try to write .pyc files on the import of source modules
ENV PYTHONDONTWRITEBYTECODE=1 
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 
# ignore case on imports
ENV PYTHONCASEOK=1

RUN mkdir /app

COPY . /app

# Application directory setup
WORKDIR /app

# Installing Reqs
RUN pip install pipenv
RUN pipenv install --system

# Expose Port
EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]