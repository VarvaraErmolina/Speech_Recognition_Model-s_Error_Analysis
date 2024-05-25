import csv

with open(r'C:\Users\Варя\PycharmProjects\kursovaya\names_red.txt', 'r') as f:
    files = f.read().split('\n')
with open("comparison_large_red.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
    for name in files:
        line = [name]
        with open(f"result_red/whisper_{name}.txt", 'r', encoding='utf-8') as f3:
            line.append(f3.read())
        file_writer.writerow(line)
