from queue import Queue
import time

# Створити чергу заявок
queue = Queue()

# Лічильник заявок
request_id = 0

def generate_request():
    global request_id
    request_id += 1
    request = f"Заявка №{request_id}"
    queue.put(request)
    print(f"Створено: {request}")

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Обробляється: {request}")
    else:
        print("Черга порожня — немає що обробляти.")

# Головний цикл програми:

i = input("Ведіть число клієнтів:")
for i in range(10):
    generate_request()
    process_request()
    time.sleep(1)
