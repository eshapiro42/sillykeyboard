import mido, mido.backends.rtmidi
import time
import threading

class SillyKeyboard:
    def __init__(self, function):
        self.stop_threads = threading.Event()
        self.stop_threads.clear()
        self.buffer = []
        def callback():
            while not self.stop_threads.is_set():
                function(buffer)
        self.t = threading.Thread(target=callback)
        self.t.start()

    def stop(self):
        self.stop_threads.set()

    def interval_offset(buffer, args):
        delay = args[0]
        interval = args[1]
        # Look for ripe MIDI messages
        for msg, added_time in buffer:
            if added_time + (delay / float(1000)) < time.time():
                if msg.type in ["note_on", "note_off"]:
                    msg.note += interval
                outport.send(msg)
                self.buffer.remove((msg, added_time))
        # Look for new MIDI messages
        for msg in inport.iter_pending():
            self.buffer.append((msg, time.time()))
