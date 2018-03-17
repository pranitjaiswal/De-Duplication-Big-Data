def file_line_counter(file_name=""):
	with open(file_name) as file:
		file_line_count = len(file.read().split("\n"))
	return file_line_count


def get_local_command(input_file="", output_file="", mapper="", reducer=""):
	return "cat " + repr(input_file) + " | python3 " + mapper + " | sort | python3 " + reducer + " > " + output_file


def get_hadoop_command(input_file="", output_dir="", mapper="", reducer="", hadoop_streaming_api_path=""):
	return "hadoop fs " + hadoop_streaming_api_path + " -file " + mapper + " -file " + reducer + " -mapper " + mapper + " -reducer " + reducer + " -input " + input_file + " -output " + output_dir
