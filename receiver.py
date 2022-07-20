import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))

channel = connection.channel()

# 채널 안에서 큐를 선언
# 센더 쪽에서 큐를 선언했지만, 확실히 하기 위해 한 번 더 선언
channel.queue_declare(queue = 'test2')

# 큐에서 가져온 메세지를 처리할 콜백 함수 생성
def callback(ch, method, properties, body):
    print("메세지를 받았습니다 : %r" % body)

# 메세지를 보낼 때 어떻게 할 것인지 설정함
# 함수, 큐, 응답 여부 를 지정
# basic_consume은 버전에 따라 구조가 달라서 주의
channel.basic_consume(queue = 'test2', on_message_callback = callback, auto_ack = True)

print("메세지를 기다리고 있습니다. 종료하려면 CTRL + C를 누르세요")

channel.start_consuming()