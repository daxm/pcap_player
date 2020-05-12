FROM python:3

ENV WORK_DIR /
WORKDIR $WORK_DIR

ENV PCAP_DIR $WORK_DIR/pcap
ENV PCAP_FILE test.pcap

RUN mkdir -p $WORK_DIR
COPY bootstrap.py $WORK_DIR

RUN mkdir -p $PCAP_DIR
COPY $PCAP_FILE $PCAP_DIR

RUN pip install scapy

CMD [ "sh", "-c", "python bootstrap.py ${PCAP_DIR}/${PCAP_FILE}" ]
