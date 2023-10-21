<<<<<<< Updated upstream
# This is a test for using github
=======
>>>>>>> Stashed changes
from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self.__initialize_photos()
        self.current_page_index = 0

    def __initialize_photos(self):
        matrix = []
        for _ in range(self.pages):
            matrix.append([])
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        number_of_pages = ceil(photos_count / 4)
        return cls(number_of_pages)

    def add_photo(self, label: str): # add 4 photos on every page
        if len(self.photos[self.current_page_index]) == 4:
            self.current_page_index += 1
        try:
            self.photos[self.current_page_index].append(label)
            return f"{label} photo added successfully on " \
                   f"page {self.current_page_index + 1}" \
                   f" slot {len(self.photos[self.current_page_index])}"
        except IndexError:
            return "No more free slots"

    def display(self):
        res = ''
        for page in self.photos:
            res += "-" * 11 + "\n"
            res += " ".join(["[]" for p in page]) + "\n"
        res += "-" * 11 + "\n"

        return res


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
