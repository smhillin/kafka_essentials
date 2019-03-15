# Creating a Streaming Data Pipeline


### Start Zookeeper and your Kafka Cluster

    sudo ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server-1.properties
    
    sudo ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server-2.properties
    
    sudo ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server-3.properties

### Create the input topic
  ~/kafka/bin/kafka-topics.sh --create \
          --zookeeper localhost:2181 \
          --replication-factor 1 \
          --partitions 1 \
          --topic streams-plaintext-input
   
### Create the output topic
  ~/kafka/bin/kafka-topics.sh --create \
          --zookeeper localhost:2181 \
          --replication-factor 1 \
          --partitions 1 \
          --topic streams-wordcount-output

### generate some input data and store it in a local file at /tmp/file-input.tx  

    echo -e "Hello Kafka Essentials Class\nHave a nive day.\nStream on!" > /tmp/file-input.txt
          
###  The result file will have the follwoing

    Hello Kafka Essentials Class
    Have a nive day.
    Stream on!

### Lastly, we send this input data to the input topic:


    cat /tmp/file-input.txt | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic streams-plaintext-input

The Kafka console producer reads the data from STDIN line-by-line, 
and publishes each line as a separate Kafka message to the topic 
streams-plaintext-input, where the message key is null and the 
message value is the respective line such as all streams lead to kafka, 
encoded as a string.


## Process tht input with Kafka streams

We will run the WordCount demo application, which is included in Apache Kafka. 
It implements the WordCount algorithm, which computes a word occurrence histogram 
from an input text. However, unlike other WordCount examples you might have seen 
before that operate on finite, bounded data, the WordCount demo application 
behaves slightly differently because it is designed to operate on an infinite, 
unbounded stream of input data.

Similar to the bounded variant, it is a stateful algorithm that tracks and updates the 
counts of words. However, since it must assume potentially unbounded input data, 
it will periodically output its current state and results while continuing to 
process more data because it cannot know when it has processed "all" the input data. 
This is a typical difference between the class of algorithms that operate on unbounded 
streams of data and, say, batch processing algorithms such as Hadoop MapReduce. 
It will be easier to understand this difference once we inspect the actual output data 
later on.

## Run the WordCount demo application.

The application writes its results to a Kafka output topic -- 
there won't be any STDOUT output in your console.

You can safely ignore any WARN log messages.

    ~/kafka/bin/kafka-run-class.sh org.apache.kafka.streams.examples.wordcount.WordCountDemo

No deployment magic here: The WordCount demo is a normal Java application 
that can be started and deployed just like any other Java application. 
The script kafka-run-class is nothing but a simple wrapper for java -cp ....


## Word Count Application

The WordCount demo application will read from the input topic streams-
plaintext-input, perform the computations of the WordCount algorithm 
on the input data, and continuously write its current results to the 
output topic streams-wordcount-output (the names of its input and 
output topics are hardcoded). To terminate the demo enter control-c 
from the keyboard.

    

## Use CLI tools to manually reading output from topic



## Troubleshooting



    "If you get an error that kafka is running currently you can kill the process."

    ps -fA | grep ./bin/kafka-server-start.sh

    sudo kill -9 <process-id>

    "Failed to acquire lock on file .lock in /kafka/logs. A Kafka instance in another process or thread is using this directory"

    sudo rm /kafka/logs/.lock


Get this error.

There is insufficient memory for the Java Runtime Environment to continue.
Native memory allocation (mmap) failed to map 3221225472 bytes for committing reserved memory.
An error report file with more information is saved as:

increase heap size for Kafka


    export KAFKA_HEAP_OPTS="$KAFKA_HEAP_OPTS -Xms3g -Xmx3g"
    
    
restart kafka brokers


