#!/usr/bin/python3
# script that fetches data from given url

import urllib.request


def fetch_info(url):
    try:
        with urllib.request.urlopen(url) as response:
            status_code = response.getcode()
            if status_code == 200:
                body = response.read()
                return {
                    "type": type(body),
                    "content": body,
                    "utf8_content": body.decode('utf-8')
                }
            else:
                return {
                    "error": f"Failed to fetch. Status code: {status_code}"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    status = fetch_info(url)
    if "error" in status:
        print(status["error"])
    else:
        print("Body response:")
        for key, value in status.items():
            print(f"\t- {key}: {value}")
