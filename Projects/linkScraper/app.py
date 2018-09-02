import requests
from bs4 import BeautifulSoup
import validators  # You need to install this module, use: pip install validators

def get_valid_url():
    """
    Prompt the user for a URL and validate it. If the URL is not valid, keep prompting the user.
    """
    while True:
        url = input("Enter a valid URL (including http:// or https://): ")
        if validators.url(url):  # Proper URL validation
            return url
        else:
            print("Invalid URL, please enter a valid URL.")

def fetch_data(url):
    """
    Fetch data from the URL and handle exceptions during the request.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    else:
        return response.text

def extract_links(html):
    """
    Extract and return links from the HTML content.
    """
    soup = BeautifulSoup(html, "html.parser")
    return [link.get("href") for link in soup.find_all("a") if link.get("href") is not None]

def save_links_to_file(links, file_name="myLinks.txt", num_links=10):
    """
    Save the specified number of links to a file.
    """
    if links:
        with open(file_name, 'w') as file:
            for link in links[:num_links]:
                file.write(f"{link}\n")
        print(f"{num_links} links have been saved to {file_name}.")
    else:
        print("No links found to write to a file.")

def main():
    """
    Main function to execute the script functionality.
    """
    url = get_valid_url()
    html_data = fetch_data(url)

    if html_data:
        links = extract_links(html_data)

        # Ask the user for the number of links they want to save
        while True:
            try:
                num_links = int(input("Enter the number of links to save: "))
                if num_links <= 0:
                    raise ValueError("Please provide a number greater than zero.")
                break
            except ValueError as e:
                print(e)

        save_links_to_file(links, num_links=num_links)
    else:
        print("Failed to retrieve data from the URL.")

# Run the script
if __name__ == "__main__":
    main()
