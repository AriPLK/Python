import time
import threading


def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(1, word_count + 1):
        time.sleep(0.1)
        file.write(f'Какое-то слово № {i}\n')
    file.flush()
    print(f'Завершилась запись в файл {file_name}')


time_start = time.time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
time_end = time.time()
print(f"Работа потоков - {round(time_end - time_start, 2)} секунд")

thread1 = threading.Thread(target=write_words, args=(10, "example5.txt"))
thread2 = threading.Thread(target=write_words, args=(30, "example6.txt"))
thread3 = threading.Thread(target=write_words, args=(200, "example7.txt"))
thread4 = threading.Thread(target=write_words, args=(100, "example8.txt"))

time_start2 = time.time()

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

time_end2 = time.time()
print(f"Работа потоков - {round(time_end2 - time_start2, 2)} секунд")
