import re

def main():
    ip_address = input("IPv4 Address: ")
    result = validate(ip_address)

    if result:
        print("True")
    else: 
        print("False")

def validate(ip):
    pattern = re.search(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip)
    return pattern is not None

if __name__ == "__main__":
    main()

