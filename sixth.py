
import sys
import requests


def download_url_and_get_all_hrefs(url):
    hrefs = []

    response = requests.get(url)

    if response.status_code == 200:
        obsah = response.text

        odkazy = obsah.split('<a href="')

        for odkaz in odkazy[1:]:
            href = odkaz.split('"')[0]
            hrefs.append(href)

    else:
        raise Exception(f"Chyba při stahování stránky: {response.status_code}")

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)

        for href in hrefs:
            print(href)

    except Exception as e:
        print(f"Program skončil chybou: {e}")
