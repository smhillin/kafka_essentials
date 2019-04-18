# Create a multiple Kafka Brokers

Kafka partitions incoming messages for a topic, 
and assigns those partitions to the available Kafka brokers. 
The number of partitions is configurable and can be set per-topic and per-broker.


## Change setting on 1st node

SSH into your first machine shutdown any running Kafka instances 

    nano ~/kafka/config/server.properties


    broker.id=1
    listeners=PLAINTEXT://:9092
    log.dirs=/home/ubuntu/kafka/logs/events-1
    advertised.listeners=PLAINTEXT://<hostname>:9092
    
    for example(advertised.listeners=PLAINTEXT://54.89.214.237:9092)

### Start kafka broker first node

    sudo ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties
    
    kafkat brokers


## Bootstrap 2nd Node


### SSH into 2nd VM


### Download and Install Java


    sudo apt update

    sudo apt-get install default-jdk

### Download and Install Kafka   

    cd

    sudo mkdir -p ~/Downloads

    sudo wget http://ftp.wayne.edu/apache/kafka/2.2.0/kafka_2.12-2.2.0.tgz -O ~/Downloads/kafka.tgz -O ~/Downloads/kafka.tgz

Create a directory called kafka and change to this directory. 
This will be the base directory of the Kafka installation and make
your life a lot easier!

    sudo mkdir -p ~/kafka && cd ~/kafka

    sudo tar -xzf ~/Downloads/kafka.tgz --strip 1

### Make changes to the config file

    nano ~/kafka/config/server.properties

    broker.id=4
    listeners=PLAINTEXT://:9092
    log.dirs=/home/ubuntu/kafka/logs/events-4
    advertised.listeners=PLAINTEXT://18.207.190.9:9092

        for example(advertised.listeners=PLAINTEXT://18.207.190.9:9092)

You will also need to point the zookeeper connect to node-1 as it is not hosted locally
in this setup.

    zookeeper.connect=<hostname>:2181

        for example (zookeeper.connect=54.89.214.237:2181)

add last  line to your file
    
    delete.topic.enable = true
    
### Start 2nd node

    sudo ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties

     
### Check status of your cluster


    kafkat brokers
    
    
You should see something like this
    
Broker		Socket
2		ip-172-31-95-78.ec2.internal:9092
3		ip-172-31-95-78.ec2.internal:9092



## Create a new topics with 2 partitions and 2 replicas



   ~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 2 --partitions 2 --topic kafka-multi-node


    kafkat partitions kafka-multi-node
    

What replicas are each of the partitions on?
  
    kafkat partitions kafka-multi-node
    
 
 What replicas are each of the partitions on?
 
 
## Sketch out a drawing of your brokers, partitions, and topics



## Use console producer to write to topic


## Create a new producer and consumer that publishes to new topic


    ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092  --topic kafka-multi-node


    ~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic kafka-multi-node --from-beginning

## Perform some writes form your console producer

    Hello
    My name is
    <your name>
    My cluster
    Has two brokers
    on 2 VM's
    now that's availability

## Delete Topics


    sudo    ~/kafka/bin/kafka-topics.sh --delete --zookeeper localhost:2181  --topic kafka-multi-node



    
# Trouble Shooting

"If you get an error that kafka is running currently you can kill the process."

    ps -fA | grep ./bin/kafka-server-start.sh

    sudo kill -9 <process-id>

"Failed to acquire lock on file .lock in /kafka/logs. A Kafka instance in another process or thread is using this directory"

    sudo rm /kafka/logs/.lock
    
Kill process on particular port
    
    sudo fuser -k 9092/tcp