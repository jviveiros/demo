FROM alpine:3.18 as python_build

WORKDIR /demo
ADD . /demo

RUN apk add py3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


from python_build as demo_run

CMD [ "sh","-c", "python3 $CMD $ARG"]
