import boto3

client = boto3.client('ec2')

def create_instance():

    output = client.run_instances(
            ImageId="ami-007ec828a062d87a5",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="LondonKeypair_pem"
            )
    print(output)

def list_Instances():
    resp = client.describe_instances()
    for reservation in resp['Reservations']:
      for instance in reservation['Instances']:
        print("Running Instance Image ID: {} Running instance Instance Type: {} Running Instance Keyname {}"
              .format(instance['InstanceId'],instance['InstanceType'],instance['KeyName']))


def terminate_instance():
    instance_id = input("Enter ID of the instance to be deleted : ")
    response = client.terminate_instances(
                InstanceIds=[
            instance_id,
        ],
    )

    print(response)

while True:
    print("1. List of Instances")
    print("3. Create EC2")
    print("4. Create group")
    print("5. Add user into aroup")
    print("0. Exit")

create_instance()
list_Instances()
terminate_instance()
