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
    response = requests.get(API_URL, params={'page_size': 5000, 'tags__name__icontain': tag_to_query}, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        documents = response.json()

        # Iterate through the documents and download them
        for document in documents['results']:
            document_filename = str(document['archived_file_name'])
            print(document_filename)


paperless("Q4")