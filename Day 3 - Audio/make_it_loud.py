import wave, struct


file = wave.open("task1.wav") # открываем файл
n = file.getnframes() # узнаем число число фреймов (значений амплитуды в файле)

data = file.readframes(n) # считываем все фреймы
print(data[:100]) # это байт строка

frames = struct.unpack("@{0}h".format(n), data) # преобразуем строку в кортеж из чисел
# @ - порядок бит в байте - нативный
# посередине - количестве
# h - двухбайтовые числа (short)
print(frames[:100])

# увеличиваем громкость, складывая в новый список
loud_frames = []
for frame in frames:
    loud_frames.append(frame*10)
#да, они стали громче
print(loud_frames[:100])

# запаковываем список в байт-строку
loud_data = struct.pack("@{0}h".format(n), *loud_frames)
print(loud_data[:100])

# сохраняем в новый файл
output_file = wave.open("result.wav", 'w')
output_file.setparams(file.getparams())
output_file.writeframes(loud_data)


