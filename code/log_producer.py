from kafka import KafkaProducer
import time
partition=3


#create topic
topic = 'test'
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=str.encode)

#produce logging to topic
with open("logs/test-logs.txt", mode="r") as log:
    for line in log:
        print(line)
        producer.send(topic, value=line)
        time.sleep(3)



