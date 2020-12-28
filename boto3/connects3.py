import boto3 
def list_buckets_and_objects():
    s3 = boto3.resource('s3')

    for bkt in s3.buckets.all():
        print(bkt.name)
        for k1 in bkt.objects.all():
            print(k1.key)

def download_many_objects():
    client = boto3.client('s3')

    response = client.get_object(
    Bucket='bucketname', Key='LOLLL.jpg')

    print(response)
    

download_many_objects()


