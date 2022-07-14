import boto3
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId="ami-08d4ac5b634553e16",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="s3_project"
    )