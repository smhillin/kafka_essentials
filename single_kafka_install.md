In this lab you will deploy a single instance of Kafka and Zookeeper.  
This lab requires at least 4gb of RAM on an Ubuntu machine.

# Install Zookeeper and Kafka



## Download and Install Java


    sudo apt update

    sudo apt-get install default-jdk


## Install jvmtop

this is a handy tool to monitor memory usage on your jvm

    wget https://github.com/patric-r/jvmtop/releases/download/0.8.0/jvmtop-0.8.0.tar.gz
    
    tar -xvzf jvmtop-0.8.0.tar.gz
    
    sudo chmod +x jvmtop.sh

    export JAVA_HOME='/usr/lib/jvm/java-8-openjdk-amd64/'

check to see if jvmtop works

    ./jvmtop.sh
    
    
## Download and Install Zookeeper

    sudo apt-get install zookeeperd

See if zookeeper is running 

    sudo service zookeeper status

Check to if zookeeper is listing on port 2181

    sudo netstat -nlpt | grep ':2181'
    
    
Now, ZooKeeper is installed, and it will be started as a daemon automatically
    
CD into Zookeeper directory and checkout the directory structure

     cd /var/lib/zookeeper/data
     
     sudo apt install tree
     
     tree
     

### Update zookeeper configurations

The zoo.cfg file keeps configuration for ZooKeeper, i.e. on which port the ZooKeeper instance will listen, data directory, etc.

    cd /etc/zookeeper    

    sudo nano conf/zoo.cfg

What is the client port?  The default listen port is 2181. You can change this port by changing clientPort.

What is the default data directory? You will want to change this from temp because you do not want zookeeper to delete data at some point

    exit from nano

### Create a new data directory in zookeeper folder


    sudo mkdir config/data

### Change the data directory

    sudo nano conf/zoo.cfg

    replace with "dataDir=/var/lib/zookeeper/data"

    save and exit nano


## Download and Install Kafka

    cd

    sudo mkdir -p ~/Downloads

    sudo wget http://ftp.wayne.edu/apache/kafka/2.2.0/kafka_2.12-2.2.0.tgz -O ~/Downloads/kafka.tgz

Create a directory called kafka and change to this directory. 
This will be the base directory of the Kafka installation and make
your life a lot easier!

    sudo mkdir -p ~/kafka && cd ~/kafka

    sudo tar -xzf ~/Downloads/kafka.tgz --strip 1


### Update configurations

    cd ~/kafka/config

    sudo nano server.properties

### By default, Kafka doesn't allow you to delete topics. To be able to delete topics

Add the following line at the end of the file:

    delete.topic.enable = true

### Tell kafka to listen on default port 9092 

Remove the comment from "listeners=PLAINTEXT://:9092"

### Update log directory from temp


Change log.dirs from "/tmp/kafka-logs" to "logs/events"


### Check zoopkeeper port and url.  

In this case it will be on local host and default zookeeper port

    zookeeper.connect=localhost:2181


### Increase Kafka JVM

Kafka relies heavily on the filesystem for storing and caching messages. 
All data is immediately written to a persistent log on the 
filesystem without necessarily flushing to disk.  Kafka uses page 
cache memory as a buffer for active writers and readers, so after you specify 
JVM size (using -Xmx and -Xms Java options), 
leave the remaining RAM available to the operating system for page caching.

    # Set KAFKA specific environment variables here.
    export KAFKA_HEAP_OPTS="$KAFKA_HEAP_OPTS -Xms1g -Xmx1g"
  

### Start Zookeeper(if stopped) and Kafka from any folder

    sudo service zookeeper status

    sudo service zookeeper start

    sudo ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties


### Run Kafka in Background

    "ctrl-z"

    bg

### Check to See if Kafka is Running on port 9092

    netstat -nlpt

## Install kafkaT

KafkaT is a tool that makes it easier to view details about your cluster.

Install Ruby

    sudo apt-get install ruby ruby-dev build-essential
    
Install KafkaT Gem
    
    sudo gem install kafkat --source https://rubygems.org --no-ri --no-rdoc
    
    cd 
    
Create a .kafkacfg file

    sudo nano .kafkatcfg

Add the following lines:

    {
      "kafka_path": "~/kafka",
      "log_path": "/kafka/logs",
      "zk_path": "localhost:2181"
    }

Check to See if Kafkat works and shows your broker


# Trouble Shooting

    "If you get an error that kafka is running currently you can kill the process."

    ps -fA | grep ./bin/kafka-server-start.sh

    sudo kill -9 <process-id>

    "Failed to acquire lock on file .lock in /kafka/logs. A Kafka instance in another process or thread is using this directory"

    sudo rm /kafka/logs/.lock
  
  
  
  

