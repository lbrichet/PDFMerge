# curl -H 'Authorization: Token 5b6ef986ffe805aa0a2174ed644b12d20ff0e148' https://paperless.brichet.be/api/documents/?tags__name__iexact=Q3%20-%202023

import requests
import os

# Define the API endpoint, your specific tag, and your authentication token
api_url = "https://paperless.brichet.be/api/documents/"
tag_to_query = "Q3 - 2023"
auth_token = "5b6ef986ffe805aa0a2174ed644b12d20ff0e148"  # Replace with your actual token

# Set up the headers with the authentication token
headers = {
    'Authorization': f'Token {auth_token}',
}

# Make a GET request to the API to retrieve documents with the specific tag
response = requests.get(api_url, params={'tags__name__iexact': tag_to_query}, headers=headers)

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

