import boto3

ec2=boto3.client('ec2')

response= ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        #print(instance)
        id = instance['InstanceId']
        print(id)
        for tags in instance['Tags']:
            print(tags)
            
            if tags['Key']=='web' and tags['Value']=='env':
                ec2.create_image(
                    InstanceId = id,
                    Name= "my-first-image",
                )
            
