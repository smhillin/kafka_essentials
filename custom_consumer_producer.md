# Create a custom Kafka Producer and Consumer

You must have zookeeper and kafka installed on your machine.  If not use

https://github.com/smhillin/kafka_essentials/blob/master/single_kafka_install.md

## Install Python 3.6 on VM (20 Minutes)
    
    cd /opt

    sudo wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
    
    sudo tar -xvf Python-3.6.3.tgz
    
    cd Python-3.6.3
    
    sudo ./configure
    
    sudo apt-get install build-essential libssl-dev libffi-dev python-dev
    
    sudo make
    
    sudo make install
    
install kafka modulepip for Python

    sudo pip3 install kafka-python
    
Check your version of Python
    
    python3.6 -V


## Download Source Code

    cd

    git clone https://github.com/smhillin/kafka_essentials
    
    cd kafka_essentials

## Take a look at your text file

   cat logs/logs.txt
   
Here we have an apache log file with 1000's of log entry's.


##  Create a Producer

We are going to write a producer that reads log data from the log file and writes that data to a kafka broker.  This will simulate
real time logging.  


Luckily this has already been done for you!  Check it out

    nano code/log_consumer.py
   
 

## Create a consumer


We are going to write a producer that polls a kafka topic for log data.  When that topic has data we will take the unstructured log
data and process it into a structure that we can later perform some analysis on. 


    cd code
    
    
    nano code/log_producer.py
    
    
    nano code/log_parser.py
    
    
## Run consumer and producer

Open another terminal window and ssh into your vm.  Go to kafka_essentials directory.
Run both of these consumers.

    sudo python3 code/log_consumer.py
    
    sudo python3 code/log_producer.py

Watch your consumer process the data as it is written to the topic!




    
# Troubleshooting

Problems with Python installation.  Run this and then rebuild.

sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev 
libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev