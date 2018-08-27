import requests  # Using requests for improved performance and simplicity
import emoji

def get_http_status(url):
    """
    Fetch the HTTP status code for the given URL/API and print the corresponding message and emoji.

    :param url: The URL to be checked.
    """
    try:
        # Send a request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.ok:
            print(f'Status code: {response.status_code} {emoji.emojize(":thumbs_up:")}')
            print(f'Message: Request succeeded. Request returned message - {response.reason}')
        else:
            # The request returned an unsuccessful status code
            print(f'Status: {response.status_code} {emoji.emojize(":thumbs_down:")}')
            print(f'Message: Request failed. Server returned reason - {response.reason}')

    except requests.ConnectionError:
        # Handle connection errors
        print(f'Status: Connection error {emoji.emojize(":thumbs_down:")}')
        print('Message: Failed to establish a connection to the server.')
    except requests.Timeout:
        # Handle timeout errors
        print(f'Status: Timeout {emoji.emojize(":thumbs_down:")}')
        print('Message: The request timed out.')
    except requests.RequestException as e:
        # Handle other types of request errors
        print(f'Status: Error {emoji.emojize(":thumbs_down:")}')
        print(f'Message: {str(e)}')
    except Exception as e:
        # Handle any other exception that wasn't caught above
        print(f'An unexpected error occurred: {str(e)} {emoji.emojize(":thumbs_down:")}')

def main():
    # Request the URL input from the user
    request_url = input("Enter the URL to be invoked: ")

    # Validate URL format
    if not request_url.startswith(('http://', 'https://')):
        print("Invalid URL. Please include http:// or https://")
    else:
        # Invoke the function to get the HTTP status
        get_http_status(request_url)

if __name__ == "__main__":
    main()
