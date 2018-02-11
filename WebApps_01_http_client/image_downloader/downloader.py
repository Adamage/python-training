from bs4 import BeautifulSoup
import sys
import requests
import os


def run_application():
    page_in_html = download_page()
    images_links = find_images(page_in_html)
    download_images('images', images_links)


def download_page():
    address = r"http://www.filmweb.pl/ranking/film"
    response = requests.get(address)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


def find_images(page_in_html):
    all_img_tags = page_in_html.findAll('img')
    url_links = []
    for img_tag in all_img_tags:
        attributes = img_tag.attrs
        if 'src' in attributes:
            url = img_tag.attrs['src']
            url_links.append(url)
            continue

        if 'data-src' in attributes:
            url = img_tag.attrs['data-src']
            url_links.append(url)
            continue

    return url_links


def download_images(output_folder, images_links, limit=50):
    count = 0

    while count < limit:
        path_to_file = os.path.join(output_folder, str(count) + '.jpg')
        a = requests.get(images_links[count])
        with open(path_to_file, 'wb') as file:
            file.write(a.content)
        count += 1
        sys.stdout.write("#")
        sys.stdout.flush()
    print(" Done.")

if __name__ == "__main__":
    print(sys.argv)
    run_application()

