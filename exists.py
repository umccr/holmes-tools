import sys
import boto3
import binascii
import botocore

from settings import SITES_CHECKSUM, FINGERPRINT_BUCKET

if __name__ == '__main__':
    s3 = boto3.resource('s3')

    # expecting BAM URLs as input i.e. gds://production/analysis/MY.bam or s3://prod-data/my.bam
    for line in sys.stdin:
        gds_file = line.strip()

        # the fingerprint bucket stores the file paths using hex (to avoid any strange S3 quoting requreiments)
        gds_as_hex = binascii.hexlify(str.encode(gds_file, 'utf-8'))

        key = f"{SITES_CHECKSUM}/{gds_as_hex.decode('utf-8')}"

        obj = s3.Object(bucket_name=FINGERPRINT_BUCKET, key=key)

        try:
            # test if the fingerprint is present and loadable
            obj.load()

            print(f"{gds_file}\ts3://{FINGERPRINT_BUCKET}/{key}")
        except botocore.exceptions.ClientError:
            print(f"{gds_file}\t-")
