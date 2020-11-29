from credentials import Credentials as cr
import csv

import os

def split_datas(filename, columnwanted):

    '''
    Break raw data into many files
    '''
    os.makedirs(os.getcwd() + os.sep + "data" + os.sep + "CURATED" + os.sep + columnwanted + os.sep, exist_ok=True)

    RAW_LOCAL_PATH = os.getcwd() + os.sep
    CURATED_LOCAL_PATH = os.getcwd() + os.sep + "data" + os.sep + "CURATED" + os.sep + columnwanted + os.sep
    COUNTRY_FILES_PATH = os.getcwd() + os.sep + "data" + os.sep + "CURATED" + os.sep + columnwanted + os.sep + columnsousdossier + os.sep
    print(CURATED_LOCAL_PATH)
    csv.field_size_limit(10000000)

    with open(RAW_LOCAL_PATH + filename, encoding='utf-8') as file_stream:
        file_stream_reader = csv.DictReader(file_stream, delimiter=',')
        open_files_references = {}

        for row in file_stream_reader:
            nameoffile = row[columnwanted]
            # Open a new file and write the header
            if nameoffile not in open_files_references:
                print (CURATED_LOCAL_PATH + '{}.csv'.format(nameoffile))
                output_file = open(CURATED_LOCAL_PATH + '{}.csv'.format(nameoffile), 'w', encoding='utf-8', newline='')
                dictionary_writer = csv.DictWriter(output_file, fieldnames=file_stream_reader.fieldnames)
                dictionary_writer.writeheader()
                open_files_references[nameoffile] = output_file, dictionary_writer

            # Always write the row
            open_files_references[nameoffile][1].writerow(row)
        # Close all the files
        for output_file, _ in open_files_references.values():
            output_file.close()