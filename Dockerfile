FROM ghcr.io/hyperledger/aries-cloudagent-python:py3.9-0.8.1

USER root

RUN pip install git+https://github.com/usingtechnology/aries-cloudagent-python-plugins@main#subdirectory=basicmessage_storage

USER $user
COPY ./configs configs

CMD ["aca-py"]