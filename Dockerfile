FROM python:3-slim

# Update
# RUN apk add --update python py-pip

# Bundle app source
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_APP=skel.py

EXPOSE  5000

ENTRYPOINT ["flask"]
CMD ["run", "--host", "0.0.0.0"]
