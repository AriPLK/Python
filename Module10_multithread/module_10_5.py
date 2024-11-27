from multiprocessing import Pool
import time

def read_info(name):
    all_data = []
    file = open(name, "r")
    a = file.readline()
    with file:
       for line in file:
           new_line = line.replace("\n", '')
           all_data.append(new_line)
           if a == "":
               break

file_names = [f'./file {number}.txt' for number in range(1, 5)]



if __name__ == "__main__":
    start_time = time.time()
    for file in file_names:
        a = read_info(file)
    end_time = time.time()
    print(f"{round(end_time - start_time, 5)} (линейный)")

    with Pool(5) as p:
        start_time1 = time.time()
        a = p.map(read_info, file_names)
        end_time1 = time.time()
        print(f"{round(end_time1 - start_time1, 5)} (многопроцессный)")




