import boto3

def s3_upload():
# Configure AWS credentials
 print("Uploading on S3 bucket...")
 aws_access_key_id = 'AKIAWUO5P34TQTJWJSHB'
 aws_secret_access_key = '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'
 region_name = 'us-east-1'

# Create an S3 client
 s3_client = boto3.client('s3',
                         aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key,
                         region_name=region_name)
 file_path = 'D:\\cloud\\Huffman-Coding\\encrypted_text_file.enc'
 bucket_name = 'rohan1090'
 object_key = 'file.enc'

 s3_client.upload_file(file_path, bucket_name, object_key)
 print("Succesfully uploaded")
 return True


def downloadfile():
 bucket_name = 'rohan1090'
 file_key = 'file.enc'
 aws_access_key_id = 'AKIAWUO5P34TQTJWJSHB'
 aws_secret_access_key = '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'
 region_name = 'us-east-1'

# Create an S3 client
 s3_client = boto3.client('s3',
                         aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key,
                         region_name=region_name)

# Specify the local file path to save the downloaded file
 local_file_path = 'D:/cloud/downloadedfile.enc'

# Download the file
 s3_client.download_file(bucket_name, file_key, local_file_path)

 print('Successfully downloaded')
#download()




bucket_name = 'rohan1090'
file_key = 'file.enc'

def check_file_exists(bucket_name, file_key):
    aws_access_key_id = 'AKIAWUO5P34TQTJWJSHB'
    aws_secret_access_key = '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'
    region_name = 'us-east-1'

# Create an S3 client
    s3_client = boto3.client('s3',
                         aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key,
                         region_name=region_name)
    try:
        s3_client.head_object(Bucket=bucket_name, Key=file_key)
        return True
    except Exception as e:
        return False
#print(check_file_exists(bucket_name,file_key))





 


