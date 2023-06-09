FROM apache/airflow:2.4.2-python3.9

USER root
RUN apt-get update \
    && apt-get install wget unzip zip -y

RUN wget -P /home/airflow/spark https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz \
    && cd /home/airflow/spark \
    && tar xzfv openjdk-11.0.2_linux-x64_bin.tar.gz \
    && rm openjdk-11.0.2_linux-x64_bin.tar.gz 

ENV JAVA_HOME "/home/airflow/spark/jdk-11.0.2"
RUN export JAVA_HOME
ENV PATH "${JAVA_HOME}/bin:${PATH}"
RUN export PATH

RUN wget -P /home/airflow/spark https://archive.apache.org/dist/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz \
    && cd /home/airflow/spark \
    && tar xzfv spark-3.3.2-bin-hadoop3.tgz \
    && rm spark-3.3.2-bin-hadoop3.tgz

ENV SPARK_HOME "/home/airflow/spark/spark-3.3.2-bin-hadoop3"
RUN export SPARK_HOME
ENV PATH "${SPARK_HOME}/bin:${PATH}"
RUN export PATH

ENV PYTHONPATH "${SPARK_HOME}/python/:$PYTHONPATH"
RUN export PYTHONPATH
ENV PYTHONPATH "${SPARK_HOME}/python/lib/py4j-0.10.9.5-src.zip:$PYTHONPATH"
RUN export PYTHONPATH

COPY requirements.txt requirements.txt
USER airflow
RUN pip install --no-cache-dir --user -r requirements.txt