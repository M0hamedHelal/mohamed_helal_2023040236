FROM alpine
WORKDIR /app
COPY app.py .
RUN apk add --update python3
RUN apk add --update py3-pip
RUN pip3 install --break-system-packages flask
CMD ["python3", "app.py"]