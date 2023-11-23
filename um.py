import re

def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r'(um|Um)', s)
    result = len(match)
    return result

if __name__ == "__main__":
    main()
