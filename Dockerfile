# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV DJANGO_SECRET_KEY !1e7xu0j8t9$!l3^wu$qegxkuaelq4)sjvyr17rdctjy4=^g(^
# ENV ENVIRONMENT DEVELOPMENT


# Set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/
