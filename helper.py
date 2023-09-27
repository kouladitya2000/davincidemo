import os
from azure.storage.blob import BlobServiceClient

def upload_file_to_blob(file, STORAGEACCOUNTURL, STORAGEACCOUNTKEY, CONTAINERNAME):
    """
    Uploads a file to Azure Blob Storage.
    
    Parameters:
        file: Uploaded file object from Streamlit.
        STORAGEACCOUNTURL: Azure Storage Account URL.
        STORAGEACCOUNTKEY: Azure Storage Account Key.
        CONTAINERNAME: Azure Blob Storage container name.

    Returns:
        str: The name of the uploaded file.
    """
    if file:
        file_name = file.name

        blob_service_client_instance = BlobServiceClient(account_url=STORAGEACCOUNTURL, credential=STORAGEACCOUNTKEY)

        blob_client_instance = blob_service_client_instance.get_blob_client(container=CONTAINERNAME, blob=file_name)

        with file as data:
            blob_client_instance.upload_blob(data, overwrite=True)

        return file_name

def read_blob_data(STORAGEACCOUNTURL, STORAGEACCOUNTKEY, CONTAINERNAME, file_name):
    """
    Reads and returns data from Azure Blob Storage.

    Parameters:
        STORAGEACCOUNTURL: Azure Storage Account URL.
        STORAGEACCOUNTKEY: Azure Storage Account Key.
        CONTAINERNAME: Azure Blob Storage container name.
        file_name: Name of the blob to read.

    Returns:
        str: The contents of the blob as a string.
    """
    blob_service_client_instance = BlobServiceClient(account_url=STORAGEACCOUNTURL, credential=STORAGEACCOUNTKEY)
    blob_client_instance = blob_service_client_instance.get_blob_client(container=CONTAINERNAME, blob=file_name)
    blob_data = blob_client_instance.download_blob()
    data = blob_data.readall().decode('utf-8')
    return data


def list_blob_files(storage_account_url, storage_account_key, container_name):

    """
Lists and returns the names of blob files within an Azure Blob Storage container.

Parameters:
    storage_account_url (str): The URL of the Azure Blob Storage account.
    storage_account_key (str): The access key for the Azure Blob Storage account.
    container_name (str): The name of the Azure Blob Storage container to list files from.

Returns:
    list of str: A list of file names (blob names) within the specified container.
    An empty list is returned if there are no files or an error occurs.


"""
    try:
        blob_service_client = BlobServiceClient(account_url=storage_account_url, credential=storage_account_key)
        container_client = blob_service_client.get_container_client(container_name)

        blob_files = []

        for blob in container_client.list_blobs():
            blob_files.append(blob.name)

        return blob_files
    except Exception as e:
        print(f"Error listing blob files: {str(e)}")
        return []
