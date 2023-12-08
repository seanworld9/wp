from urllib.request import urlopen
from xml.etree import ElementTree
import subprocess

url = "http://seanworld.net:10214/original/post-sitemap.xml"

prefixText = "http://seanworld.net:10214/original/\nhttp://seanworld.net:10214/original/category/japan/\nhttp://seanworld.net:10214/original/category/trip/\nhttp://seanworld.net:10214/original/category/money/\nhttp://seanworld.net:10214/original/category/technology/\nhttp://seanworld.net:10214/original/category/gadget/\nhttp://seanworld.net:10214/original/category/diy/\n"

def fetch(url: str) -> str:
    """指定した URL のリソースを文字列で取得します。"""
    with urlopen(url) as res:
        return res.read().decode("utf-8")


def extract_urls(sitemap_xml):
    """sitemap.xml の内容から URL を抽出します。"""
    urls = []
    root = ElementTree.fromstring(sitemap_xml)
    # <loc> タグの中身を取得する
    for loc in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
        urls.append(loc.text)
    return urls


if __name__ == "__main__":
    sitemap_xml = fetch(url)
    urls = extract_urls(sitemap_xml)

    f = open('tempfile.txt', 'w')
    f.write(prefixText)
    for url in urls:
        f.write(url+"\n")
    f.close()

    cmd = "wget --no-parent --page-requisites --convert-links --html-extension -i tempfile.txt -l 1 -x"
    subprocess.call(cmd, shell=True)

