import pika
from time import sleep

## 메세지 센더

#서버와 연결
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

#채널을 만듭니다
channel = connection.channel()

#채널 안에서 큐를 선언 (새 큐를 만듦)
channel.queue_declare(queue = 'test2')

#메세지를 보냄
#channel.basic_publish(exchange = '', routing_key = 'hello', body = 'Hello World!!!')

for i in range(5):
    channel.basic_publish(exchange = '', routing_key = 'test2', body = str(i))
    print("메세지를 보냈습니다.")
    sleep(3)

connection.close()