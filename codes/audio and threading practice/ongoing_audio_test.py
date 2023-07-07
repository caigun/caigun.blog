import pyaudio
import wave
from queue import Queue
import time
import threading

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000

p1 = pyaudio.PyAudio()
p2 = pyaudio.PyAudio()

stream1 = p1.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    frames_per_buffer = FRAMES_PER_BUFFER)

stream2 = p2.open(format=FORMAT,
                channels=1,
                rate=RATE,
                output=True,
                output_device_index=5)

frames = Queue()

print(p2.get_default_output_device_info())


def record_sound(seconds):
    
    global frames

    print("START RECORDING...")
    for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
        data = stream1.read(FRAMES_PER_BUFFER)
        frames.put(data)
    print("STOP RECORDING!!")

def play_sound():

    global frames

    time.sleep(1)
    while not frames.empty():
        data = frames.get()
        stream2.write(data)

class record(threading.Thread):
    def run(self, seconds=2):
        record_sound(seconds)

class play(threading.Thread):
    def run(self):
        play_sound()

# threadLock = threading.Lock()
threads = []

# thread1 = record()
# thread2 = play()

thread1 = threading.Thread(target=record_sound, args=(2,))
thread2 = threading.Thread(target=play_sound)

thread1.start()
thread2.start()


threads.append(thread1)
threads.append(thread2)

print("THE FIRST PIN")

for t in threads:
    t.join()

print("THE SECOND PIN")

stream1.stop_stream()
stream1.close()
p1.terminate()
stream2.stop_stream()
stream2.close()
p2.terminate()