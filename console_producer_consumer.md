# Test Kafka Instalation by Producing and Consuming Data


### Start Zookeeper and Kafka

    sudo service zookeeper status

    sudo service zookeeper start

    sudo ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties

### Create topic

    ~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 5 --topic KafkaEssentials

    ~/kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181

### Create a console producer that publishes to topic KafkaEssentials

    ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic KafkaEssentials

Publish some text to the topic

    Hello, World
    My name is Shaun
    Kafka, I loved your book the Metamorphosis

### Create console consumer

Open a new terminal window and ssh into your instance

Create a consumer that reads from the beginning

    ~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic KafkaEssentials --from-beginning

What is the result? 

Your new consumer should print the previous messages you sent to the broker

### Publish some more text to the topic called KafkaEssential

    hello, Kafka
    thanks for being so available

Now check your consumer and see if the message was recieved by consumer

Congrats! you have successfully set up a messaging Queue and Topic


### Create another consumer

    ctrl-z your consumer 

    ~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic KafkaEssentials

What is the result?
    
Your consumer should be blank as we did not pass --from-beginning flag to consumer
    
Type some text in your consumer.

    close your consumer
    
### Create another topic

Open a new terminal window

    ~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 5 --topic KafkaEssentials-2


    ~/kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181

### Crate a new producer that publishes to new topic


    ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic KafkaEssentials-2

### Create a new consumer that consumers from both topics

    ~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --whitelist "KafkaEssentials| KafkaEssentials-2"
    
Now publish to both producers.

Check your new consumer to see what happens

# Trouble Shooting

    "If you get an error that kafka is running currently you can kill the process."

    ps -fA | grep ./bin/kafka-server-start.sh

    sudo kill -9 <process-id>

    "Failed to acquire lock on file .lock in /kafka/logs. A Kafka instance in another process or thread is using this directory"

    sudo rm /kafka/logs/.lock