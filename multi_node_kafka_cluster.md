# Bootstrap Kafka Nodes

These steps should be performed on all the kafka nodes.

## Download and Install Java

    sudo apt update

    sudo apt-get install default-jre


## Download and Install Zookeeper

    sudo apt-get install zookeeperd

    sudo service zookeeper status

    sudo service zookeeper stop


## Install kafkaT

KafkaT is a tool that makes it easier to view details about your cluster.

Install Ruby

    sudo apt-get install ruby ruby-dev build-essential
    
Install KafkaT Gem
    
    sudo gem install kafkat --source https://rubygems.org --no-ri --no-rdoc
    

Tell KT 
    {
      "kafka_path": "~/kafka",
      "log_path": "/tmp//kafka/logs",
      "zk_path": "localhost:2181"
    }