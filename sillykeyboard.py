from tkinter import *
from tkinter.ttk import *
import mido
import mido.backends.rtmidi
import time
import threading

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.stop_threads = threading.Event()

        # Start button
        self.start_button = Button(frame, text="Start", command=self.start)
        self.start_button.pack(padx=5, pady=5, side=RIGHT)

        # Stop button
        self.stop_button = Button(frame, text="Stop", command=self.stop)
        self.stop_button.pack(padx=5, pady=5, side=RIGHT)

        # Delay selection
        self.delay_label = Label(frame, text="Delay")
        self.delay_label.pack(padx=5, pady=10, side=LEFT)
        self.delay_entry = Entry(frame)
        self.delay_entry.pack(padx=5, pady=10, side=LEFT)

        # Interval selection
        self.interval_label = Label(frame, text="Interval")
        self.interval_label.pack(padx=5, pady=10, side=LEFT)
        self.interval_entry = Entry(frame)
        self.interval_entry.pack(padx=5, pady=10, side=LEFT)

    def start(self):
        self.stop_threads.clear()
        outport = mido.open_output(output_spinbox.get())
        inport = mido.open_input(input_spinbox.get())
        delay = float(self.delay_entry.get())
        interval = 4
        buffer = []
        def callback():
            while not self.stop_threads.is_set():
                # Look for ripe MIDI messages
                for msg, added_time in buffer:
                    if added_time + (delay / float(1000)) < time.time():
                        if msg.type in ["note_on", "note_off"]:
                            msg.note += interval
                        outport.send(msg)
                        buffer.remove((msg, added_time))
                # Look for new MIDI messages
                for msg in inport.iter_pending():
                    buffer.append((msg, time.time()))
        t = threading.Thread(target=callback)
        t.start()

    def stop(self):
        self.stop_threads.set()

def on_closing():
    app.stop_threads.set()
    root.destroy()

root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)

inputs = mido.get_input_names()
outputs = mido.get_output_names()


# MIDI input device selection
input_label = Label(root, text="Input")
input_label.pack(padx=5, pady=5, side=LEFT)
input_spinbox = Combobox(root, values=inputs)
input_spinbox.pack(padx=5, pady=5, side=LEFT)

# MIDI output device selection
output_label = Label(root, text="Output")
output_label.pack(padx=5, pady=5, side=LEFT)
output_spinbox = Combobox(root, values=outputs)
output_spinbox.pack(padx=5, pady=5, side=LEFT)

app = App(root)
root.mainloop()

