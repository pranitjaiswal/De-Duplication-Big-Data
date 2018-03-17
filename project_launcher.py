from argparse import ArgumentParser
from DeDupeUI import DeDupeUI


def main():
	parser = ArgumentParser()
	parser.add_argument("--input-file", type=str, default="./data/sample.txt", help="Path or location of the input file.")
	parser.add_argument("--output-file", type=str, default="./data/sample_output.txt", help="Path or location of the output file in case of local execution (directory in case of hadoop).")
	parser.add_argument("--mapper", type=str, default="mapper.py", help="Path or location of the mapper script.")
	parser.add_argument("--reducer", type=str, default="reducer.py", help="Path or location of the reducer script.")
	parser.add_argument("--hadoop", type=str, default="", help="Path or location of the hadoop streaming api jar (provide only in case of hadoop execution).")
	args = parser.parse_args()
	app = DeDupeUI(args)
	app.mainloop()


if __name__ == "__main__":
	main()
