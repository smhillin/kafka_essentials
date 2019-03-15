# Create a multiple Kafka Brokers

Kafka partitions incoming messages for a topic, 
and assigns those partitions to the available Kafka brokers. 
The number of partitions is configurable and can be set per-topic and per-broker.
    
## Make a copy of configurations

    sudo cp ~/kafka/config/server.properties ~/kafka/config/server-1.properties
>   sudo cp ~/kafka/config/server.properties ~/kafka/config/server-2.properties
    sudo cp ~/kafka/config/server.properties ~/kafka/config/server-3.properties

## Stop any running instances of Kafka(For Existing Single Broker)

Make sure Kafka is not running

    netstat -nlpt

    sudo ~/kafka/bin/kafka-server-stop.sh

## Update Settings


The broker.id property is the unique and permanent name of each node in the cluster. 
We have to override the port and log directory only because we are 
running these all on the same machine and we want to keep the brokers from all 
trying to register on the same port or overwrite each other's data.

We most also change the port numbers to provide for one to one mapping 
of brokers to ports


##  Edit config files for 1st Kafka Broker

    sudo nano ~/kafka/config/server-1.properties

    broker.id=1
    listeners=PLAINTEXT://:9092
    log.dirs=logs/events-1


##  Edit config files for 2nd Kafka Broker

    sudo nano ~/kafka/config/server-2.properties
    
    broker.id=2
    listeners=PLAINTEXT://:9093
    log.dirs=logs/events-2

##  Edit config files for 3rd Kafka Broker

    sudo nano ~/kafka/config/server-3.properties
    
    broker.id=3
    listeners=PLAINTEXT://:9094
    log.dirs=logs/events-3

## Make sure zookeeper has started

    sudo service zookeeper start
    
    
## Start kafka Brokers

    sudo ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server-1.properties
    
    
    ctrl-z
    
    bg

    
    sudo ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server-2.properties

    ctrl-z
    
    bg

    sudo ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server-3.properties
    
    ctrl-z
    
    bg

Check to see if they are listening on the ports 9093 and 9094

    nestat -nlpt | grep 909


## Create a script to start and stop kafka brokers

    sudo nano ~/kafka/bin/my-kafka.sh
    
Paste these in you file

    #!/bin/bash
    echo "starting broker 1"
    ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server-1.properties
    echo "Starting broker 2"
    ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server-2.properties
    echo "Starting broker 3"
    ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server-3.properties

Save and edit permission
    
    
    sudo chmod +x ~/kafka/bin/my-kafka.sh

     

## Install kafkaT

KafkaT is a tool that makes it easier to view details about your cluster.

Install Ruby

    sudo apt-get install ruby ruby-dev build-essential
    
Install KafkaT Gem
    
    sudo gem install kafkat --source https://rubygems.org --no-ri --no-rdoc
    

Create a .kafkacfg file

sudo nano .kafkatcfg

Tell KT 
    {
      "kafka_path": "~/kafka",
      "log_path": "/kafka/logs",
      "zk_path": "localhost:2181"
    }
    
## Check status of your cluster


    kafkat brokers
    
    
    kafkat topics
    
You should see something like this
    
Broker		Socket
2		ip-172-31-95-78.ec2.internal:9093
3		ip-172-31-95-78.ec2.internal:9094
1		ip-172-31-95-78.ec2.internal:9092


## Create a new topics with 2 partitions and 2 replicas

Remember: The message is partitioned on the brokers into a set of distinct partitions.  
The meaning of these partitions is left up to the producer.  The producer specifies
which partition a message belongs to.  A partition stores 
messages in the order in which they arrive at the broker, and will be given out
to consumers in that order.

Those partitions can be replicated in case they go down.

   ~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 2 --partitions 2 --topic kafka-multi-broker-1

   ~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 2 --partitions 3 --topic kafka-multi-broker-2


    kafkat partitions kafka-multi-broker-1
    

What replicas are each of the partitions on?
  
    kafkat partitions kafka-multi-broker-2
    
 
 What replicas are each of the partitions on?
 
## Sketch out a drawing of your brokers, partitions, and topics



## Now go to your events directory and check out the directory structure


    tree events-1
    
    tree events-2
    
    tree events-3
 
 
 Does this follow your results from Kafkat command above?
 You should see a structure that reflects the number of partitions and 
 replicas for both of your topics


## Use console producer to write to topic


## Create a new producer and consumer that publishes to new topic


    ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9093  --topic kafka-multi-broker-2


    ~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9093 --topic kafka-multi-broker-2 --from-beginning

## Perform some writes form your console producer

    Hello
    My name is
    <your name>
    todays date 
    is <todays date>

## Now go to your events directory and see what it looks like


    tree events-1
    
    tree events-2
    
    tree events-3
 
## Open one of the paritions on one of the brokers and perform a dump of the logs

 


## Delete Topics


    sudo    ~/kafka/bin/kafka-topics.sh --delete --zookeeper localhost:2181  --topic kafka-multi-broker-1

    sudo    ~/kafka/bin/kafka-topics.sh --delete --zookeeper localhost:2181  --topic kafka-multi-broker-2


    
# Trouble Shooting

"If you get an error that kafka is running currently you can kill the process."

    ps -fA | grep ./bin/kafka-server-start.sh

    sudo kill -9 <process-id>

"Failed to acquire lock on file .lock in /kafka/logs. A Kafka instance in another process or thread is using this directory"

    sudo rm /kafka/logs/.lock
    
Kill process on particulat port
    
    sudo fuser -k 9094/tcp