import requests

def paperless(tag_to_query):
    # PAPERLESS CONSTANTS
    API_URL = "https://paperless.brichet.be/api/documents/"
    AUTH_TOKEN = "08d29963baa1a3ed9a8a0a0f59103b86b0079a3a"  

    # Set up the headers with the authentication token
    headers = {
        'Authorization': f'Token {AUTH_TOKEN}',
    }

    # Make a GET request to the API to retrieve documents with the specific tag
    response = requests.get(API_URL, params={'page_size': 5000, 'tags__name__iexact': tag_to_query}, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        documents = response.json()

        # Iterate through the documents and download them
        for document in documents['results']:
            # Download the document
            document_id = document['id']
            
            # Sometimes, archived_file_name is 'None'
            if document['archived_file_name'] is not None:
                document_filename = str(document['archived_file_name'])
            else:
                document_filename = str(document['original_file_name'])

            document_url = API_URL+str(document_id)+"/download/"
            document_file = requests.get(document_url, headers=headers)
            
            if document_file.status_code == 200:
                open(document_filename, 'wb').write(document_file.content)
                print(f"Downloaded: {document['id']} : {document_filename}")
            else:
                print(f"Failed to download: {document['id']} : {document_filename}")
    else:
        print(f"Failed to retrieve documents. Status code: {response.status_code}")