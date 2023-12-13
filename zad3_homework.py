# class Employee:
#     """
#     Klasa za vraboteni.
#     """

#     def __init__(self, first_name: str, last_name: str, email: str, position: str, company: str, salary=None):
#         """
#             Inicijalizirame objekt od klasata Employee.

#             :param first_name: str, ime
#             :param last_name: str, prezime
#             :param email: str, email
#             :param position: str, pozicija vo kompanijata
#             :param company: str, kompanija
#             :param salary: int, plata
#         """
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.position = position
#         self.company = company
#         self.salary = salary

#     def respond(self, job_offer: str):
#         """
#         Vo ovaa funkcija vraboteniot moze da ja prifati ili
#         odbie ponudata od Company
#         """
#         print(job_offer)
#         response = input('Do you accept the job offer? (yes/no): ').lower()
#         if response == "yes":
#             return True
#         else:
#             return False

#     def leave_company(self):
#         response = input(
#             'Are you sure you wish to leave the company? (yes/no): ').lower()
#         if response == "yes":
#             return True
#         else:
#             return False


# class Company:

#     Company_Employees = [Employee("John", "Smith", "johnsmith@email.com", "developer", "semos_mk", 200000),
#                          Employee("Mary", "Mary", "mary@email.com",
#                                   "developer", "semos_mk", 20000),
#                          Employee("Tom", "Brown", "tom.brown@email.com",
#                                   "senior developer", 300000),
#                          Employee("Tom", "Brady", "tom.brady@email.com",
#                                   "junior developer", 30000)
#                          ]

#     """
#     Klasa za kompanija.
#     """

#     def __init__(self, name: str, company_id: int, address=None):
#         """
#         Inicijalizirame objekt od klasata Company.

#         :param name: str, ime na kompanijata
#         :parm company_id: int, unikaten broj na kompanija 
#         :param address: str, adresa
#         """
#         self.name = name
#         self.company_id = company_id
#         self.address = address

#     def hire(self, employee: Employee, position: str, salary: int):
#         """
#         Vo ovaa funkcija, Company prakja ponuda do vraboteniot
#         """
#         response = f"{self.name} is making a job offer to {employee.first_name} {employee1.last_name} for the position of {position} with a salary of {salary}."
#         return response

#     def final_response(self, employee1_response: bool, employee: Employee):
#         """
#         Vo ovaa funkcija samo printuvame soodvetna poraka ako 
#         vraboteniot ja prifakja ponudata ili ne
#         """
#         if (employee1_response == True):
#             Company.Company_Employees.append(employee)
#             print(f"Welcome to the company!")
#         else:
#             print(f"Maybe next time!")
    
#     def average_salary(self):
#         sum_salary = 0
#         total_employees = len(Company.Company_Employees)

#         for employee in Company.Company_Employees:
#             if employee.salary is not None:
#                 sum_salary += employee.salary

#         if total_employees != 0:
#             avg_salary = sum_salary / total_employees
#             return avg_salary
#         else:
#             return 0


        
#     def add_employ(self, employee:Employee):
#         Company.Company_Employees.append(employee)

#     def print_employees(self):
#         """
#         Ovaa funkcija gi printuva site vraboteni
#         """
#         print("Employees:")
#         for employee in Company.Company_Employees:
#             print(f"{employee.first_name} {employee.last_name} - {employee.position}")

#     def employee_quits(self, decision: bool, employee: Employee):
#         """
#         Ako ovoj vraboten ja napusta firmata,
#         treba da go izbrisime od listata
#         """
#         if (decision == True):
#             Company.Company_Employees.remove(employee)
#         else:
#             pass

#     def promotion(self, employee:Employee):
#         employee.salary+=3000


# # zadaca 1
# # Da se napravat 2 instanci od klasata Company i 3 instanci od klasata Employee.
# semos_mk = Company("Semos Makedonija", 1234)
# tesla=Company("Tesla", 1222)


# # employee1 = Employee("John", "Doe", "johndoe@email.com",
# #                      "developer", "semos_mk")
# # employee2=Employee("Mary", "Mary", "mary@email.com","developer", "semos_mk", 20000),
# # employee3=Employee("Tom", "Brown", "tom.brown@email.com","senior developer", 300000)

# # zadaca 2
# # Da se napravi sporedba za prosecnite salary costs za sekoja kompanija.

# avg_salary=semos_mk.average_salary()
# print(avg_salary)

# # zadaca 3
# # Da se napise metod days_off so koj employee ke ima pravo da bara denovi odmor.
# # Pritoa imame annual leave, special circumstances leave, maternity leave, sick days leave.

# # zadaca 4
# # Da se napise metod promotion so koj employee ke moze da bide unapreden.

# promotion_employee=semos_mk.Company_Employees[0]
# semos_mk.promotion(promotion_employee)

# zadaca 5
# Da se napravi klasa Produkt.
# Da se dodadat zadolzitelni atriibuti pri kreiranje na instanca od Produkt: naziv, seriski_broj, cena, tip
# i opcionalen atribut kolicina.

class Product:
    """
    Klasa za Produkti
    """

    def __init__(self, name: str, serial_number: str, price: float, product_type: str, quantity=None):
        """
        Inicijalizirame instanca od klasata Product

        :param name: str, ime na produkt
        :param serial_number: str, seriski broj na produkt
        :param price: float, cena na produkt
        :param product_type: str, tip na produkt
        :param quantity: int, opcionalen atribut za kolicina na produkt
        """
        self.name = name
        self.serial_number = serial_number
        self.price = price
        self.product_type = product_type
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.name} ({self.product_type}) - ${self.price:.2f}"

# zadaca 6
# Da se napravi klasa Prodavnica.
# Instancata od prodavnicata, mora da ima: ime, seriski_broj.
# Da se kreira metod dodaj_produkt, koj kje dodava produkti vo prodavnicata,
# so toa sto mora da se proveri dali e od tip Produkt.

class Prodavnica:
    """
    Klasa za Prodavnica
    """
    def __init__(self, name: str, serial_number: str):
        """
        Inicijalizacija na instanca od klasata Prodavnica

        :param name: str, ime na prodavnica
        :param serial_number: str, seriski broj na prodavnicata
        """
        self.name = name
        self.serial_number = serial_number
        self.products = []  # Lista za produktite vo prodavnicata

    def dodaj_produkt(self, product:Product):
        """
        Dodava produkt vo prodavnicata

        :param product: Product, produktot za proverka
        """
        if isinstance(product, Product):
            self.products.append(product)
            print(f"Produktot: {product.name} dodadeno vo {self.name}.")
        else:
            print("Ne e tip Produkt")
    
    def pecati_produkti(self):
        print(f"Produkti vo {self.name}:")
        for product in self.products:
            print(product)

    def __str__(self):
        return f"{self.name} (Seriski Broj: {self.serial_number})"
    
    def __brisi_produkt(self, product):
       
        if product in self.products:
            self.products.remove(product)
            print(f"{product.name} izbrisano od {self.name}.")
        else:
            print(f"{product.name} ne e najdeno vo {self.name}.")

    def buy_product(self, client, product):
     
        if product in self.products and client.current_balance >= product.price:
            client.current_balance -= product.price
            print(f"{client.name} kupi {product.name} od {self.name} za ${product.price:.2f}.")
            self.__brisi_produkt(product)
        elif product not in self.products:
            print(f"{product.name} ne e najdeno vo {self.name}.")
        else:
            print(f"{client.name} nema dovolni sredstva za {product.name}.")


# zadaca 7
# Da se kreira klasa Kupuvac.
# Sekoj Kupuvac mora da ima: ime, prezime, dostapni_paricni_sredstva.
# zadaca 8
# Da se kreiraat __str__ metodi za klasite.
# Da se kreira metod pecati_produkti na klasata Prodavnica koj sto kje gi printa site dostapni produkti.

# zadaca 9
#  Da se kreiraat 5 produkti.
# Da se kreiraat 2 prodavnici.
# Da se dodadat produkti vo prodavnicite.
# Da se kreiraat kupuvaci.
# Da se napravi scenario, kupuvacot da kupi produkt od prodavnica. Vo slucaj ako go nema produktot,
# da proba da go kupi produktot od drugata prodavnica.
# Pri kupuvanje na produkt od prodavnica, treba da se izbrise istoit od listata na produkti. Za ova da se koristi
# privaten metod __brisi_produkt.
# Da se vnimava na dostapnite sredstva na kupuvacot.

class Kupuvac:
    """
    Klasa za kupuvaci
    """

    def __init__(self, name: str, surname: str, current_balance: float):
        """
        Inicijalizacija na objekt od klasata Kupuvac.

        :param name: str, ime na kupuvac
        :param surname: str, prezime na kupuvac
        :param current_balance: float, dostapni paricni sredstva na kupuvac
        """
        self.name = name
        self.surname = surname
        self.current_balance = current_balance

    def __str__(self):
        return f"{self.name} {self.surname} - Paricni sredstva: ${self.current_balance:.2f}"


product1 = Product(name="Laptop", serial_number="L123", price=1200.0, product_type="Electronics", quantity=5)
product2 = Product(name="Smartphone", serial_number="S456", price=800.0, product_type="Electronics")
product3 = Product(name="Headphones", serial_number="H789", price=100.0, product_type="Electronics", quantity=10)
product4 = Product(name="Coffee Maker", serial_number="C101", price=50.0, product_type="Appliances", quantity=3)
product5 = Product(name="Backpack", serial_number="B222", price=30.0, product_type="Fashion")

prodavnica1=Prodavnica(name="Electronics Store", serial_number="123ABC")
prodavnica2=Prodavnica(name="Phone Store", serial_number="456DEF")




prodavnica1.dodaj_produkt(product1) 
prodavnica1.dodaj_produkt(product2)
prodavnica1.dodaj_produkt(product3) 
prodavnica1.dodaj_produkt(product4)

prodavnica2.dodaj_produkt(product2)
prodavnica2.dodaj_produkt(product4)
prodavnica2.dodaj_produkt(product5)

client1 = Kupuvac(name="John", surname="Doe", current_balance=1000.0)
client2 = Kupuvac(name="Mary", surname="Smith", current_balance=2000.0)
client3 = Kupuvac(name="Sarah", surname="John", current_balance=3000.0)

prodavnica1.buy_product(client1,product1)

prodavnica2.buy_product(client2,product3)

client2.current_balance=0.0
prodavnica2.buy_product(client1,product4)
