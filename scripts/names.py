from os import walk

filenames = next(walk(r"C:\Users\Варя\PycharmProjects\kursovaya\vyborka"), (None, None, []))[2]
filenames = [i[:-4] for i in filenames if i[-3:] == 'wav']
with open('names.txt', 'w') as f:
    f.write('\n'.join(filenames))
