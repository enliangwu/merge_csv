#!/usr/bin/python3
import sys
import os
import csv


def merge_csv_files(file_list: list) -> bool:
    if len(file_list) < 2:
        print('no enough input files', file=sys.stderr)
        return False

    header_list = []
    for file_index, input_file in enumerate(file_list):
        # check existence of the csv file
        if not os.path.exists(input_file):
            print(f'{input_file} not existed', file=sys.stderr)
            return False

        with open(input_file) as f:
            line = f.readline().strip()
            for header in line.split(","):
                if header not in header_list:
                    header_list.append(header)

    # print header
    header_list.append('"filename"')
    print(','.join(header_list))

    for file_index, input_file in enumerate(file_list):
        # check existence of the csv file
        if not os.path.exists(input_file):
            print(f'{input_file} not existed', file=sys.stderr)
            return False

        # get base name of the file
        filename = os.path.basename(input_file)

        # read file line by line to reduce memory
        with open(input_file) as f:
            output_index_list = []
            output_list = [''] * len(header_list)
            for input_index, input_line in enumerate(f):
                # remove \n at end of the line
                input_line = input_line.strip()

                # set up the index
                if input_index == 0:
                    for header in input_line.split(','):
                        output_index_list.append(header_list.index(header))
                    continue

                for col_idx, field in enumerate(input_line.split(',')):
                    output_list[output_index_list[col_idx]] = field

                output_list[-1] = f'"{filename}"'
                print(','.join(output_list))

    return True


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('no enough arguments', file=sys.stderr)
        exit(0)

    merge_csv_files(sys.argv[1:])  # argv[0] is the program name, argv[1] and so on is a list of inputs
