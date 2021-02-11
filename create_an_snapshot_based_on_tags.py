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
            
            if tags['Key']=='Name' and tags['Value']=='Kubernetes_Master':
                ec2.create_snapshots(
                    Description='my-snapshotfromInstance',
                    InstanceSpecification={
                        'InstanceId': id
                    },
                    print("snapshot has been created")

                )
            else:
                print("cannot find the specified tags")
            
