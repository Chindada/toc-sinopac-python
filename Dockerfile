FROM python:3.10.6-alpine

USER root

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /toc-sinopac-python
ENV PYTHONPATH=/toc-sinopac-python/pb

COPY src /toc-sinopac-python/src
COPY pb /toc-sinopac-python/pb
COPY scripts /toc-sinopac-python/scripts

# RUN apt update -y && \
#     apt install -y tzdata && \
#     apt autoremove -y && \
#     apt clean && \
#     rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/toc-sinopac-python/scripts/docker-entrypoint.sh"]
