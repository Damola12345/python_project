import os
files = os.listdir('text')

def ignore_non_txt_file(file):
    if file.endswith(".txt"):
        return True
    return False

filtered_files = filter(ignore_non_txt_file, files)

with open('combined_output.txt', 'w') as fo:
    for input_file in filtered_files:
        with open(f'text/{input_file}', 'r') as fi:
            fo.write(fi.read())
            fo.write('\n')
            













