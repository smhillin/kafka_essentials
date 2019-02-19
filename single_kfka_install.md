## Download and Install Java

  sudo add-apt-repository ppa:webupd8team/java

  sudo apt update

  sudo apt install oracle-java8-set-default

## Download and Install zookeeper

  wget https://www-us.apache.org/dist/zookeeper/stable/zookeeper-3.4.12.tar.gz

  tar -xzf zookeeper-3.4.12.tar.gz

  cd zookeeper-3.4.12/conf

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

### Stop zookeeper

  sudo ./zkServer.sh stop

## Download and Install Kafka

  cd

  wget http://apache.mirrors.ionfish.org/kafka/2.1.0/kafka_2.11-2.1.0.tgz

  tar -xzf kafka_2.11-2.1.0.tgz


### Update configurations

  cd kafka_2.11-2.1.0/config

  sudo nano server.properties

### Tell kafka to listen on default port 9092 

remove the commment from "listeners=PLAINTEXT://:9092"

### Update log directory from temp

Change log.dirs from "/tmp/kafka-logs" to "/kafka_2.11-2.1.0/kafka-logs"

### Check zoopkeeper port and url.  

In this case it will be on local host and default zookeeper port

zookeeper.connect=localhost:2181

### Start Kafka

go to kafka home directory

  sudo ./bin/kafka-server-start.sh config/server.properties



