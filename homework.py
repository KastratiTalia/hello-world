# Prva klasa: PublishingHouse
# Vtora klasa: Publication (Book or Magazine)
# Treta klasa: Book
# Cetvrta klasa: Magazine

# 1. Princip na Nasleduvanje: Klasite Book i Magazine nasleduvaat od klasata Publication
# 2. Princip na Polimorfizam: display_info() funkcijata vo Publication, Book, Magazine
# 3. Princip na Abstrakcija:manage_publication() funkcijata vo PublishingHouse
# 4. Princip na Enkapsulacija: privatni/pseudo-privatni atributi i metodi vo PublishingHouse

class Publication:
    """
    Class for the Publications of a Publishing House
    """

    def __init__(self, title: str, publishing_year: int, publication_type: str):
        """
        :param title: Ime na instancata od klasata
        :param publishing_year: godina na izdavanje
        :param publication_type: tip "book" ili "magazine"
        """
        self.title = title
        self.publishing_year = publishing_year
        self.publication_type = publication_type

    def display_info(self):
        """
        Prikaz na site informacii za instanca od Publication klasata
        """
        print(f"Title: {self.title}")
        print(f"Publishing Year: {self.publishing_year}")
        print(f"Publication Type: {self.publication_type}")


class PublishingHouse:
    """
    Klasa za Izdavacka Kukja
    """

    def __init__(self, name: str, creation_year: int):
        """
        :param name: ime na Izdavacka Kukja
        :param creation_year: godina na osnovanje
        """
        self._name = name  # Pseudo-private attribute
        self.creation_year = creation_year
        self.__publications = []  # Private attribute

    def __add_publication(self, publication: Publication):  # Private method
        """Funkcija koja dodava nova instanca od Publication
        klasata vo nizata
        :param publication: Publication koja sakame da ja dodademe
        """
        self.__publications.append(publication)

    def _delete_publication(self, publication_title: str):  # Pseudo-prvate method
        """
        Funkcija koja brisi instanca od Publication
        klasata od nizata 
        :param publication_title: Ime od Publication koja sakame da ja izbriseme od nizata
        """
        for publication in self.__publications:
            if publication.title == publication_title:
                self.__publications.remove(publication)
                break
        else:
            print(f"Publication with title '{publication_title}' not found.")

    def manage_publication(self, publication: Publication, action: str):
        """
        Princip na Abstrakcija
        So ovaa funkcija moze da gi dodademe ili izbriseme Publication,
        i ima nivo na abstrakcija bidejki koristnikot/administrator od eden Publishing House "ne znae" kako se imlementirani 
        metodide za dodavanje i brisenje od listata na Publications

        :param publication: Publication koja sakame da ja dodademe/izbriseme
        :param action: 'add' ili 'delete'
        """
        if action == 'add':
            self.__add_publication(publication)
        elif action == 'delete':
            self._delete_publication(publication.title)
        else:
            print(f"Invalid action: {action}")

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name


class Book(Publication):
    """
    Klasa za knigi
    """

    def __init__(self, title: str, author: str, year: int):
        """
        :param title: Ime na kniga
        :param author: Pisatel na kniga
        :param year: godina na izdavanje
        """
        super().__init__(title, year, 'Book')
        self.author = author

    def display_info(self):
        """
        Dopolnitelno dodavame print statement za Author na knigata
        """
        super().display_info()
        print(f"Author:{self.author}")


class Magazine(Publication):
    """
    Klasa za spisanie
    """

    def __init__(self, title: str, year: int, month: str):
        """
        :param title: ime na spisanie
        :param year: godina na izdavanje
        :param month: mesec na izdavanje
        """
        super().__init__(title, year, 'Magazine')
        self.month = month

    def display_info(self):
        """
        Dopolnitelno dodavame print statement za mesec na izdavanje na knigata
        """
        super().display_info()
        print(f"Month: {self.month}")


# --------------------------------------TESTIRANJE----------------------------------------------
# Instanca od Publication klasata
publication_instance = Publication(
    title="Generic Publication", publishing_year=2023, publication_type="Generic Type")

# Instanca od PublishingHouse klasata
publishing_house = PublishingHouse(
    name="Example Publishing House", creation_year=2000)

# Instanca od Book klasata
book_instance = Book(title="The Great Book", author="John Author", year=2023)

# Instanca od Magazine klasata
magazine_instance = Magazine(title="Tech Monthly", year=2023, month="January")


print("Publication:")
publication_instance.display_info()
print("\n")

print("Book:")
book_instance.display_info()
print("\n")

print("Magazine:")
magazine_instance.display_info()
print("\n")


print("Publishing House:")
print(f"Name: {publishing_house.get_name()}")
publishing_house.manage_publication(publication_instance, action='add')
publishing_house.manage_publication(magazine_instance, action='add')
publishing_house.manage_publication(book_instance, action='add')
print("List of Publications in the Publishing House:")
for publication in publishing_house._PublishingHouse__publications:
    print(f"- {publication.title}")
print("\n")

publishing_house.manage_publication(publication_instance, action='delete')
print("List of Publications in the Publishing House (after deletion):")
for publication in publishing_house._PublishingHouse__publications:
    print(f"- {publication.title}")
