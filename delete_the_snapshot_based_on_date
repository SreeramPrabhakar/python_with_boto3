import datetime
import sys
import boto3

#print(datetime.datetime.now())

ec2=boto3.client('ec2')

age=1

response= ec2.describe_snapshots(OwnerIds=['376683965783'])

for snapshot in response["Snapshots"]:
    print('-------------------------------------------')
    id = snapshot['SnapshotId']
    print("Snapshot-ID",id)
    
    time = snapshot['StartTime']
    print("time:",time)
    
    snapshot_create_date= time.date()
    print("snapshot_create_date",snapshot_create_date)
    
    current_date= datetime.datetime.now().date()
    print("current_date",current_date)
    
    diff_date= current_date - snapshot_create_date
    print("diff_date",diff_date)

    print("..........................")
    a=diff_date.days
    print("how many days the snapshot is older:",a)
    print("..........................")

    if a>=age:
        print ("deleting the  snapshot:",id)
        ec2.delete_snapshot(SnapshotId=id)
    else:
        print("the above snapshot is not older")
