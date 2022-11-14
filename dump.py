import boto3
import binascii

from settings import FINGERPRINT_BUCKET, SITES_CHECKSUM

if __name__ == '__main__':
    s3 = boto3.resource('s3')

    s3_paginator = boto3.client('s3').get_paginator('list_objects_v2')


    def keys(bucket_name, prefix='/', delimiter='/', start_after=''):
        prefix = prefix[1:] if prefix.startswith(delimiter) else prefix
        start_after = (start_after or prefix) if prefix.endswith(delimiter) else start_after
        for page in s3_paginator.paginate(Bucket=bucket_name, Prefix=prefix, StartAfter=start_after):
            for content in page.get('Contents', ()):
                yield content['LastModified'], content['Key']


    for d, p in keys(FINGERPRINT_BUCKET, prefix=f"{SITES_CHECKSUM}/"):
        encoded = p[len(SITES_CHECKSUM) + 1:]

        print(f"{d}\t{binascii.unhexlify(encoded).decode('utf-8')}")
