import whisper

with open(r'C:\Users\Варя\PycharmProjects\kursovaya\names.txt', 'r') as f:
    files = f.read().split('\n')
model = whisper.load_model("large")
for name in files:
    result = model.transcribe(fr"C:\Users\Варя\PycharmProjects\kursovaya\vyborka\{name}.wav")
    with open(fr'C:\Users\Варя\PycharmProjects\kursovaya\result\whisper_{name}.txt', 'w', encoding='utf-8') as f2:
        f2.write(result["text"].strip())
