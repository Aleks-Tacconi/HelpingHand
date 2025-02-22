import json
import requests
import copy
from bs4 import BeautifulSoup


def print_table(table):
    for row in table.split("</tr>"):
        print(row)
        print()


def write_dict_to_json(dictionary):
    with open("tmp.json", "w") as json_file:
        json.dump(dictionary, json_file, indent=4)


def scrape1(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html.parser")

    table = soup.find_all("table")[-1]

    links = []
    for a_tag in table.find_all("a", href=True):
        links.append("https://minecraftitemids.com" + a_tag["href"])

    return links


def scrape2(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html.parser")

    paragraphs = soup.find_all("p")
    paragraphs = paragraphs[1 : len(paragraphs) - 1]

    lst = []
    for p in paragraphs:
        if "numerical ID" in p.text:
            continue
        if "if you're playing on a Minecraft version below" in p.text:
            continue
        if "legacy item ID" in p.text:
            continue
        if "spawned in Minecraft with the below command" in p.text:
            continue
        if "The data value is" in p.text:
            continue
        if (
            "Find thousands more items on our complete list of 1,325 Minecraft IDs."
            in p.text
        ):
            continue

        lst.append(p.text)

    tables = soup.find_all("table")
    for table in tables:
        table_data = []

        head = table.find("thead")

        for row in table.find("tbody").find_all("tr"):
            key = row.find("th")
            value = row.find("td")
            try:
                if key.string is not None and value.string is not None:
                    table_data.append({key.string: value.string})
                elif key.string is not None and value.string is None:
                    items = []
                    for i in value.find_all("a"):
                        items.append(i.string)

                    table_data.append({key.string: items})
            except:
                items = {}

                for k, v in zip(head.find("tr").find_all("th"), row.find_all("td")):
                    items[k.string] = v.string

                table_data.append(items)

        lst.append(table_data)

    return lst


def main():
    url = "https://minecraftitemids.com/"
    urls = [url]
    items = {}

    for i in range(2, 28):
        urls.append(url + str(i))

    try:
        for i, url in enumerate(urls):
            print(f"{i}/{len(urls)}")

            links = scrape1(url)

            for link in links:
                key = link.split("/")[-1]
                items[key] = scrape2(link)
    except KeyboardInterrupt:
        pass
    finally:
        write_dict_to_json(items)


if __name__ == "__main__":
    main()
