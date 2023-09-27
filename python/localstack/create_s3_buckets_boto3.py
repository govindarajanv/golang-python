import boto3
import random

endpoint_url = "http://0.0.0.0:4566"

def main():
    client = boto3.client("s3", endpoint_url=endpoint_url)
    suffix = random.randint(1,10)
    client.create_bucket(Bucket="mybucket" + str(suffix),
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1'
    }
                         )
    result = client.list_buckets()
    print(result)

if __name__ == "__main__":
    main()
