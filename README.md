# DeDoop_SIH2017

## Execution command:
`python3 project_launcher.py --input-file <path/to/input/file> --output-file <path/to/output/file> --mapper <path/to/mapper/script> --reducer <path/to/reducer/script> [--hadoop <path/to/hadoop/streaming/api/jar>]`

## Example:
`python3 project_launcher.py`
> This command should work perfectly fine if you have `tkinter` installed and take the whole directory structure of the repository as is (By cloning or downloading the whole repository). It uses all the default values mention within the program and thus works without any options.

## Developer's Note:
- Use`python3 project_launcher.py --help` for a brief help menu regarding all the options.
- Although I've included the `--hadoop` option, I haven't really tested it as I don't have it installed. Please let me know in case you do so.
- In case of using the `--hadoop` option, please start the required services like sshd, start-dfs.sh and start-yarn.sh before executing the script.
- Without mentioning the `--hadoop` option, it'll work on the local file system only.
- Don't worry about cloning or downloading all the content from the reporsitory as I've only put the sample files and not the large ones.
- I haven't done any error handling yet and I'm aware of the same. Please check out the console during execution.
