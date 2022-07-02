import os
from azure.storage.blob import BlockBlobService

root_path = 'T:/'
dir_name = 'myExpressApp'
path = f"{root_path}/{dir_name}"
file_names = os.listdir(path)

account_name = 'collectimage'
account_key = 'DefaultEndpointsProtocol=https;AccountName=5gbware;AccountKey=Rs7mhjoAr1NPBL37y6LLgDaUJuKkxfSXMQd4WYSdj7vjOZtnVhSCHnD2uKxw80jvp40o6O4dUqMQARg2bpWfNA==;EndpointSuffix=core.windows.net'
container_name = 'collectimage'

block_blob_service = BlockBlobService(
    account_name=account_name,
    account_key=account_key
)

for file_name in file_names:
    blob_name = f"{dir_name}/{file_name}"
    file_path = f"{path}/{file_name}"
    print(file_path)
    block_blob_service.create_blob_from_path(container_name, blob_name, file_path)