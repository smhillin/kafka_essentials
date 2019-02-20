In this lab you will deploy a single instance of Kafka and Zookeeper.  This lab requires at least 4gb of RAM.

## Download and Install Java


    sudo apt update

    sudo apt-get install default-jre

  
## Download and Install zookeeper

    sudo apt-get install zookeeperd

see if zookeeper is running and stop if so

    sudo service zookeeper status

    sudo service zookeeper stop

### update zookeeper configurations

The zoo.cfg file keeps configuration for ZooKeeper, i.e. on which port the ZooKeeper instance will listen, data directory, etc.

    mv zoo_sample.cfg zoo.cfg

    nano zoo.cfg

What is the client port?  The default listen port is 2181. You can change this port by changing clientPort.

What is the default data directory? You will want to change this from temp because you do not want zookeeper to delete data at some point

exit from nano 

### create a new data directory in zookeeper folder

  mkdir data

### change the data directory

  cd conf

  sudo nano zoo.cfg

  replace with "dataDir=/zookeeper-3.4.12/data"

  save and exit nano

### Start zookeeper

  cd ../bin

  sudo ./zkServer.sh start


## Download and Install Kafka

  cd
  
  mkdir -p ~/Downloads

  wget http://apache.mirrors.ionfish.org/kafka/2.1.0/kafka_2.11-2.1.0.tgz -O ~/Downloads/kafka.tgz

  Create a directory called kafka and change to this directory. This will be the base directory of the Kafka installation.

  mkdir -p ~/kafka && cd ~/kafka
  
  sudo tar -xzf ~/Downloads/kafka.tgz --strip 1


### Update configurations

  cd ~/kafka/config 

  sudo nano server.properties

### By default, Kafka doesn't allow you to delete topics. To be able to delete topics

add the following line at the end of the file:

"delete.topic.enable = true"

### Tell kafka to listen on default port 9092 

remove the commment from "listeners=PLAINTEXT://:9092"

### Update log directory from temp

Change log.dirs from "/tmp/kafka-logs" to "/kafka/logs"


### Check zoopkeeper port and url.  

In this case it will be on local host and default zookeeper port

zookeeper.connect=localhost:2181

  

### Start Zookeeper(if stopped) and Kafka from any folder

  sudo service zookeeper status
  
  sudo service zookeeper status

  sudo ~/zookeeper-3.4.12/bin/zkServer.sh start
  
  sudo ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties


### Run Kafka in Background

  "ctrl-z" 
  
  bg 
  
  verify kafka is still running
  
  jobs
  
## Test Kafka Instalation by Producing and Consuming Data


### Create topic

~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 13 --topic KafkaEssentials

kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181

### Create a console producer that publishes to topic KafkaEssentials

kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic KafkaEssentials

Publish some text to the topic

Hello, World
My name is Shaun
Kafka, I loved your book the Metamorphosis

### Create console consumer

open a new terminal window and ssh into your instance

create a consumer that reads from the begining

~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic KafkaEssentials --from-beginning

what is the result?

your new consumer should print the previous messages you sent to the broker

### Publish some more text to the topic called KafkaEssential

hello, Kafka
thanks for being so available

### now check your consumer and see if the message was recieved by consumer

Congrate you have successfully set up a messaging Queue and Topic

## Trouble Shooting

"If you get an error that kafka is running currently you can kill the process."

  ps -fA | grep ./bin/kafka-server-start.sh
  
  sudo kill -9 <process-id>
  
"Failed to acquire lock on file .lock in /kafka/logs. A Kafka instance in another process or thread is using this directory"

  sudo rm /kafka/logs/.lock
  
  
  
  

