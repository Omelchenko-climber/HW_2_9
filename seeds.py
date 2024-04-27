import json

import connect
from models import Tag, Authors, Quotes

files = ["authors.json", "quotes.json"]


def get_quote():
    while True:
        command, *details = input(">>>: ").split(":")
        if command == "exit":
            break

        list_quotes = []

        match command:
            case "name":
                name, = details
                author_id, = [auth.id for auth in Authors.objects() if (auth.fullname == name)
                              or ("".join([word[0].lower() for word in auth.fullname.split()]) == name)
                              or (auth.fullname[:2].lower() == name)]
                list_quotes = [q.quote for q in Quotes.objects() if q.author.id == author_id]
            case "tag":
                tag, = details
                list_quotes = []
                for q in Quotes.objects():
                    if (tag in [tag.name for tag in q.tags]) or (tag in [tag.name[:2] for tag in q.tags]):
                        list_quotes.append(q.quote)
            case "tags":
                tags = set(details[0].split(","))
                list_quotes = [q.quote for q in Quotes.objects() if tags.intersection(set(tag.name for tag in q.tags))]

        print(list_quotes)


def send_data():
    with open("authors.json", "r", encoding="utf-8") as f_a:
        data = json.load(f_a)
        for author in data:
            author_class = Authors(fullname=author["fullname"], born_date=author["born_date"], born_location=author[
                "born_location"], description=author["description"])
            author_class.save()

            with open("quotes.json", "r", encoding="utf-8") as f_q:
                quotes = json.load(f_q)

                for record in quotes:
                    if record["author"] == author_class.fullname:
                        quote = Quotes(tags=[Tag(name=tag) for tag in record["tags"]], author=author_class, quote=record[
                            "quote"])
                        quote.save()


if __name__ == '__main__':
    get_quote()
