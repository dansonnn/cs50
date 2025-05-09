import requests
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=86d4e479d3c5cc37e768cca637d94f1ba1e02c4b4cb27038f930c8c11a0f1654")
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        pass

    value = price * amount
    print(f'${value:,.4f}')


if __name__ == "__main__":
    main()
