In this lab you will deploy a single instance of Kafka and Zookeeper.  This lab requires at least 4gb of RAM.

# Install Zookeeper and Kafka

## Download and Install Java


    sudo apt update

    sudo apt-get install default-jre

  
## Download and Install Zookeeper

    sudo apt-get install zookeeperd

See if zookeeper is running 

    sudo service zookeeper status

Check to if zookeeper is listing on port 2181

    sudo netstat -nlpt | grep ':2181'
    
    
Now, ZooKeeper is installed, and it will be started as a daemon automatically
    
CD into Zookeeper directory and checkout the directory structure

     cd /usr/share/zookeeper
     
     sudo apt install tree
     
     tree
     

### Update zookeeper configurations

The zoo.cfg file keeps configuration for ZooKeeper, i.e. on which port the ZooKeeper instance will listen, data directory, etc.

    cd /etc/zookeeper/conf    

    sudo nano zoo.cfg

What is the client port?  The default listen port is 2181. You can change this port by changing clientPort.

What is the default data directory? You will want to change this from temp because you do not want zookeeper to delete data at some point

    exit from nano

### Create a new data directory in zookeeper folder

    sudo mkdir data

### Change the data directory

    sudo nano zoo.cfg

    replace with "dataDir=/zookeeper/data"

    save and exit nano


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

Add the following line at the end of the file:

    delete.topic.enable = true

### Tell kafka to listen on default port 9092 

Remove the comment from "listeners=PLAINTEXT://:9092"

### Update log directory from temp


Change log.dirs from "/tmp/kafka-logs" to "/kafka/logs"


### Check zoopkeeper port and url.  

In this case it will be on local host and default zookeeper port

    zookeeper.connect=localhost:2181

  

### Start Zookeeper(if stopped) and Kafka from any folder

    sudo service zookeeper status

    sudo service zookeeper start

    sudo ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties


### Run Kafka in Background

    "ctrl-z"

    bg

### Check to See if Kafka is Running

    netstat -nlpt
  


# Trouble Shooting

    "If you get an error that kafka is running currently you can kill the process."

    ps -fA | grep ./bin/kafka-server-start.sh

    sudo kill -9 <process-id>

    "Failed to acquire lock on file .lock in /kafka/logs. A Kafka instance in another process or thread is using this directory"

    sudo rm /kafka/logs/.lock
  
  
  
  

