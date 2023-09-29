import sys
from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import dumps,loads
from time import sleep


bootstrap_servers = ['localhost:29092']
topicName = 'myTopic'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers,value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
for e in range(5):
    data = {'number' : e}
    ack = producer.send('numtest', value=data)
    metadata = ack.get()
    print(metadata.topic)
    print(metadata.partition)
    sleep(1)

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['localhost:29092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

try:
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
except KeyboardInterrupt:
    sys.exit()
