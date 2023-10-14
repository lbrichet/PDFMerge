import requests
import os

# Define the API endpoint and your specific tag
api_url = "https://paperless.brichet.be/api/documents/"
tag_to_query = "Q3 - 2023"

# Make a GET request to the API to retrieve documents with the specific tag
response = requests.get(api_url, params={'tags__name__iexact': tag_to_query}, timeout=10)

# Check if the request was successful
if response.status_code == 200:
    documents = response.json()

    # Create a directory to store the downloaded documents
    download_dir = "downloaded_documents"
    os.makedirs(download_dir, exist_ok=True)

    # Iterate through the documents and download them
    for document in documents:
        document_url = document['file']
        document_name = os.path.basename(document_url)
        document_path = os.path.join(download_dir, document_name)

        # Download the document
        document_response = requests.get(document_url)
        if document_response.status_code == 200:
            with open(document_path, 'wb') as f:
                f.write(document_response.content)
            print(f"Downloaded: {document_name}")
        else:
            print(f"Failed to download: {document_name}")
else:
    print(f"Failed to retrieve documents. Status code: {response.status_code}")

