from kafka import KafkaConsumer
import pprint
from log_parser import LogRow


kafka_topic = 'test'
group_id = 'log_consumer_group'

#create Kafka consumer

consumer = KafkaConsumer(kafka_topic)
lr = LogRow()

#loop through

for msg in consumer:
    msg = msg.value.decode('ascii')
    msg= lr.parseRow(msg)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(msg)



#parse message
# 200.4.91.190 - - [25/May/2015:23:11:15 +0000] "GET / HTTP/1.0" 200 3557 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
