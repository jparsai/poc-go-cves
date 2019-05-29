from utils import aws_utils as aws
from utils import cloud_constants as cc


s3_obj = aws.S3_OBJ
bucket_name = cc.S3_BUCKET_NAME
s3_bucket = s3_obj.Bucket(bucket_name)


if __name__ == '__main__':
    print('Downloading Saved Model Assets from S3 Bucket')
    aws.s3_download_folder(s3_bucket_obj=s3_bucket,
                           bucket_dir_prefix='model_assets', download_path='./models')
