# import os
# import boto3
# import s3fs
# from botocore.exceptions import ClientError

# input_archive_folder = "input_archive"
# to_process_folder = "to_process"
# file_row_limit = 50
# file_delimiter = ','

# # S3 bucket info
# s3 = s3fs.S3FileSystem(anon=False)

# def lambda_handler(event, context):
#     print("Received event: \n" + str(event))
#     for record in event['Records']:
#         # Assign some variables that make it easier to work with the data in the 
#         # event record.
#         bucket = record['s3']['bucket']['name']
#         key = record['s3']['object']['key']
#         input_file = os.path.join(bucket,key)
#         archive_path = os.path.join(bucket,input_archive_folder,os.path.basename(key))
#         folder =  os.path.split(key)[0]
#         s3_url = os.path.join(bucket,folder)
#         output_file_template = os.path.splitext(os.path.basename(key))[0] + "__part"
#         output_path = os.path.join(bucket,to_process_folder)

#         # Set a variable that contains the number of files that this Lambda 
#         # function creates after it runs.
#         num_files = file_count(s3.open(input_file, 'r'), file_delimiter, file_row_limit)

#         # Split the input file into several files, each with 50 rows.
#         split(s3.open(input_file, 'r'), file_delimiter, file_row_limit, output_file_template, output_path, True, num_files)

#         # Send the unchanged input file to an archive folder.
#         archive(input_file,archive_path)

# # Determine the number of files that this Lambda function will create.
# def file_count(file_handler, delimiter, row_limit):
#     import csv 
#     reader = csv.reader(file_handler, delimiter=delimiter)
#     # Figure out the number of files this function will generate.
#     row_count = sum(1 for row in reader) - 1
#     # If there's a remainder, always round up.
#     file_count = int(row_count // row_limit) + (row_count % row_limit > 0)
#     return file_count

# # Split the input into several smaller files.
# def split(filehandler, delimiter, row_limit, output_name_template, output_path, keep_headers, num_files):
#     import csv 
#     reader = csv.reader(filehandler, delimiter=delimiter)

#     current_piece = 1
#     current_out_path = os.path.join(
#          output_path,
#          output_name_template + str(current_piece) + "__of" + str(num_files) + ".csv"
#     )
#     current_out_writer = csv.writer(s3.open(current_out_path, 'w'), delimiter=delimiter)
#     current_limit = row_limit
#     if keep_headers:
#         headers = next(reader)
#         current_out_writer.writerow(headers)
#     for i, row in enumerate(reader):
#         if i + 1 > current_limit:
#             current_piece += 1
#             current_limit = row_limit * current_piece
#             current_out_path = os.path.join(
#               output_path,
#               output_name_template + str(current_piece) + "__of" + str(num_files) + ".csv"
#             )
#             current_out_writer = csv.writer(s3.open(current_out_path, 'w'), delimiter=delimiter)
#             if keep_headers:
#                 current_out_writer.writerow(headers)
#         current_out_writer.writerow(row)

# # Move the original input file into an archive folder.
# def archive(input_file, archive_path):
#     s3.copy_basic(input_file,archive_path)
#     print("Moved " + input_file + " to " + archive_path)
#     s3.rm(input_file)
import sys
import boto3
def lambda_handler(event, context):
    print("Received event: \n" + str(event))
    for record in event['Records']:
        s3 = boto3.resource('s3')
        bucket = record['s3']['bucket']['name']
        keyku = record['s3']['object']['key']
        obj = s3.Object(bucket, keyku)
        body = obj.get()['Body'].read()
        # print(json_cont)
        size=int(sys.getsizeof(body))
        if size > 2000:
            obj.delete()
