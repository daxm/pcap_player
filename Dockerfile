FROM python:3

ARG workdir=/app

RUN mkdir $workdir

WORKDIR $workdir

ADD pcap_player.py .
ADD requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "pcap_player.py"]
