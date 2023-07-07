import pyaudio
import wave

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000

p = pyaudio.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    frames_per_buffer = FRAMES_PER_BUFFER
)

print("START RECORDING...")

seconds = 3
frames = []
for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open("output.wav", "wb")
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close()

print("START PLAYING...")


p = pyaudio.PyAudio()
path = "output.wav"
chunk_size = 1024
wf = wave.open(path, 'rb')
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
print(p.get_default_output_device_info())
data = wf.readframes(chunk_size)
while data:
    stream.write(data)
    data = wf.readframes(chunk_size)

stream.stop_stream()
stream.close()
p.terminate()