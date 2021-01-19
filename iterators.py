import json

def hashes():
    file = open("countries.json")
    for lines in file.readline():
        yield hash(lines)
    file.close()

class Iterators:

    def __init__(self, list_of_countries):
        self.cursor = -1
        with open("countries.json") as file:
            self.countries = json.load(file)
        self.end = len(self.countries)

    def __iter__(self):
        return self

    def __next__(self):
        self.cursor = self.cursor + 1
        if self.cursor == self.end:
            raise StopIteration
        name = self.countries[self.cursor]["name"]["common"]
        return f"https://ru.wikipedia.org/wiki/{name}\n".replace(" ", "_")


if __name__ == '__main__':
    with open("link.txt", "w", encoding="utf-8") as f2:
        for c in Iterators("countries.json"):
            f2.write(c)