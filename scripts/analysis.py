import csv

with open(r'C:\Users\Варя\PycharmProjects\kursovaya\names.txt', 'r') as f:
    files = f.read().split('\n')
with open("comparison_large.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
    for name in files:
        line = []
        with open(f"vyborka/{name}.txt", 'r', encoding='utf-8') as f2:
            line.append(f2.read())
        with open(f"result/whisper_{name}.txt", 'r', encoding='utf-8') as f3:
            line.append(f3.read())
        line.append(name)
        file_writer.writerow(line)
