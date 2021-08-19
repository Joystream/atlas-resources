import os
import sys
import subprocess

if (len(sys.argv) != 3):
    raise Exception('Wrong number of args')

input_dir = sys.argv[1]
output_dir = sys.argv[2]

files = os.listdir(input_dir)
input_paths = [os.path.join(input_dir, file) for file in files]

files_without_extension = [os.path.splitext(file)[0] for file in files]
output_paths = [os.path.join(output_dir, f'{file}.webp') for file in files_without_extension]

for idx, input_path in enumerate(input_paths):
    output = subprocess.run(['cwebp', '-q', '75', '-o', output_paths[idx], input_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd())
    print(output.stderr)
