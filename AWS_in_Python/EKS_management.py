import boto3

eks_client = boto3.client('eks', region_name='eu-west-2')

def create_eks_cluster():
    response = eks_client.create_cluster(
        name=input("Enter Cluster Name: "),
        roleArn='arn:aws:iam::381771126161:role/eksClusterRole',
        resourcesVpcConfig={
        'subnetIds': ['subnet-001afa82561490e07', 'subnet-0aeaa3296a81af2fd', 'subnet-02bc9e453509e0ec9']
    }
    )
    print(response)

def delete_eks_cluster():
    response = eks_client.delete_cluster(
        name=input("Enter Cluster Name: ")
    )
    print(response)
    
def list_eks_clusters():
    response = eks_client.list_clusters()
    print("Cluster Names:", response['clusters'])
    
while True:
    print("            ")
    print("1. Create EKS Cluster")
    print("2. Delete Cluster")
    print("3. List Clusters")
    print("0. Exit")

    choice = int(input("ENTER CHOICE: "))

    if choice==1:
        create_eks_cluster()
    elif choice==2:
        delete_eks_cluster()
    elif choice==3:
        list_eks_clusters()
    elif choice==0:
        break
    else:
        print("INVALID CHOICE")
        continue