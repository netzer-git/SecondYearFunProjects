from openpyxl import Workbook
import re

"""
USAGE:
    1. Change FILE_PATH to your full path to your input text file (including '.txt' suffix)
    2. Change OUT_PATH to your wanted xl file name (and full path if you want it in different directory. don't forget
     '.xlsx' suffix)
    3. Run the program, either with IDE or with 'python WhatsApp-TextParser.py' in local command line.
"""
file_path = 'YourFile.txt'
output_path = "YourOutputFileName.xlsx"


def write_data_to_xl(data):
    """
    :param data: [{url: , ... }, ... { ... }]
    """
    labels = ['date', 'time', 'name', 'content', 'line_num']
    ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']

    wb = Workbook()
    wb['Sheet'].title = "WhatsApp Parser"
    sheet1 = wb.active

    for i in range(len(labels)):
        sheet1[ABC[i] + str(1)].value = labels[i]

    for i in range(len(data)):
        for j in range(len(labels)):
            entry = data[i]
            sheet1[ABC[j] + str(i + 2)].value = str(entry[labels[j]])  # fixme !!!!

    wb.save(output_path)


def parse_text_file():
    line_num = 0
    with open(file_path, 'r', encoding='utf8') as f:
        data = []
        pattern = re.compile('^(?P<date>[^,]+), (?P<time>[^-]+) - (?P<name>[^:]+): (?P<content>.*)')
        for line in f:
            line_num += 1
            match = pattern.search(line)
            if match is not None:
                try:
                    date = match.group('date').split('.')
                    date = date[0] + '/' + date[1] + '/' + date[2]
                    entry = {
                        'line_num': line_num,
                        'date': date,
                        'time': match.group('time'),
                        'name': match.group('name'),
                        'content': match.group('content')
                    }
                    data.append(entry)
                    print(entry)
                except IndexError:
                    data[-1]['content'] += line
            else:
                time_pattern = re.compile('(\d?\d:\d\d)')
                match = time_pattern.search(line)
                try:
                    if not match:
                        data[-1]['content'] += line
                except IndexError:
                    print("IndexError in line " + str(line_num))
    return data


if __name__ == '__main__':
    file_path = input("Enter full path to your input file (including .txt suffix): ")
    output_path = input("Enter full path to your output file (including .xlsx suffix): ")
    data = parse_text_file()
    write_data_to_xl(data)
    input("WhatsApp Parsing Completed!")
