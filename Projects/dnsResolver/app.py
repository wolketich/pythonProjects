import dns.resolver

def fetch_dns_records(website):
    """
    Fetch and display the 'A' and 'MX' DNS records of the specified website.

    :param website: The domain name of the website to query.
    """
    dns_record = {}

    try:
        # Fetching the 'A' record of the website and storing it in the dictionary
        a_records = dns.resolver.resolve(website, 'A')
        dns_record['A_Records'] = [ipval.to_text() for ipval in a_records]
        
        # Fetching the 'MX' records of the website and storing them in the dictionary
        mx_records = dns.resolver.resolve(website, 'MX')
        dns_record['MX_Records'] = [record.to_text() for record in mx_records]

    except dns.resolver.NoAnswer:
        print("No answer could be returned for the query.")
    except dns.resolver.NoNameservers:
        print("No name servers could be found to complete the query.")
    except dns.resolver.NXDOMAIN:
        print("The domain does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        # Displaying the records on the screen
        for record_type, records in dns_record.items():
            print(f"{record_type}:")
            for record in records:
                print(f" - {record}")

def main():
    # User input for the website domain
    website = input("Enter the name of the website: ")

    # Input validation could be more sophisticated, ensuring proper domain formatting.
    if not website:
        print("Please enter a valid website name.")
    else:
        fetch_dns_records(website)

if __name__ == "__main__":
    main()