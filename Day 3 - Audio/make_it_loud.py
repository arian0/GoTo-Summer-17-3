import wave, struct
#открываем аудио файл
audio_file = wave.open("task1.wav")
#получаем количество фреймов (значений амплитуды) в нем
n = audio_file.getnframes()
#читаем в память все значения амплитуды в виде байт строки
data = audio_file.readframes(n)
#превращаем байт строку в кортеж
frames = struct.unpack("@{0}h".format(n), data)

#умножаем каждый фрейм на 10 (увеличиваем громкость)
loud_frames = []
for frame in frames:
    loud_frames.append(frame * 10)

#превращаем список обратно в байт-строку
loud_data = struct.pack("@{0}h".format(n), *loud_frames)

#записываем байт строку в новый файл
loud_file = wave.open("result1.wav", "wb")
loud_file.setparams(audio_file.getparams())
loud_file.writeframes(loud_data)

