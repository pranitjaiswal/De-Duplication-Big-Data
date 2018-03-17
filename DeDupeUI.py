import tkinter as tk
from time import time
from subprocess import call
from tkinter import ttk
from function_thread import FunctionThread
from utitity_functions import file_line_counter, get_local_command, get_hadoop_command


class DeDupeUI(tk.Tk):
	def __init__(self, params, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		self.input_file = params.input_file
		self.output_file = params.output_file
		self.mapper = params.mapper
		self.reducer = params.reducer
		self.hadoop = params.hadoop
		self.process_thread = FunctionThread(self.process_function)

		self.title("DeDupeUI")
		self.geometry("1000x750")
		self.configure(bg='white')

		self.start_button = tk.Button(text="Start", command=self.start_execution, height=2, width=10)
		self.start_button.configure(bg="#7fff00", fg="white", relief=tk.RAISED)
		self.start_button.place(x=100, y=100)

		self.stop_button = tk.Button(text="Exit", command=exit, height=2, width=10)
		self.stop_button.configure(bg="#ff0000", fg="white", relief=tk.RAISED)
		self.stop_button.place(x=800, y=100)

		self.label_text = tk.StringVar()
		self.status_label = tk.Label(self, textvariable=self.label_text, relief=tk.FLAT)
		self.status_label.place(x=400, y=150)

		self.progress = ttk.Progressbar(self, orient="horizontal", length=800, mode="determinate")
		self.progress.place(x=100, y=250)

	def start_execution(self):
		self.start_button.config(state="disabled")
		self.process_thread.start()
		self.periodic_call()

	def periodic_call(self):
		if self.process_thread.is_alive():
			self.progress.step(1)
			self.after(100, self.periodic_call)

	def process_function(self):
		start_time = time()
		if self.hadoop:
			command = get_hadoop_command(input_file=self.input_file, output_dir=self.output_file, mapper=self.mapper, reducer=self.reducer, hadoop_streaming_api_path=self.hadoop)
		else:
			command = get_local_command(input_file=self.input_file, output_file=self.output_file, mapper=self.mapper, reducer=self.reducer)
		self.label_text.set("Executing de-duplication...")
		call("chmod 777 " + self.mapper, shell=True)
		call("chmod 777 " + self.reducer, shell=True)
		call(command, shell=True)
		in_size, out_size = file_line_counter(self.input_file), file_line_counter(self.output_file)
		final_stats = "Execution time:" + str(round(time() - start_time, 6)) + " seconds.\n Input size: " + str(in_size) + "\nOutput size: " + str(out_size) + "\nDuplicate Entries: " + str(in_size - out_size)
		self.label_text.set(final_stats)
		self.progress["value"] = self.progress["maximum"]
