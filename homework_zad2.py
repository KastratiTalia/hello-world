class Employee:
    """
    Klasa za vraboteni.
    """

    def __init__(self, first_name: str, last_name: str, email: str, position: str, company: str, salary=None):
        """
            Inicijalizirame objekt od klasata Employee.

            :param first_name: str, ime
            :param last_name: str, prezime
            :param email: str, email
            :param position: str, pozicija vo kompanijata
            :param company: str, kompanija
            :param salary: int, plata
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.position = position
        self.company = company
        self.salary = salary

    def respond(self, job_offer: str):
        """
        Vo ovaa funkcija vraboteniot moze da ja prifati ili
        odbie ponudata od Company
        """
        print(job_offer)
        response = input('Do you accept the job offer? (yes/no): ').lower()
        if response == "yes":
            return True
        else:
            return False

    def leave_company(self):
        response = input(
            'Are you sure you wish to leave the company? (yes/no): ').lower()
        if response == "yes":
            return True
        else:
            return False


class Company:

    Company_Employees = [Employee("John", "Smith", "johnsmith@email.com", "developer", "semos_mk", 200000),
                         Employee("Mary", "Mary", "mary@email.com",
                                  "developer", "semos_mk", 20000),
                         Employee("Tom", "Brown", "tom.brown@email.com",
                                  "senior developer", 300000),
                         Employee("Tom", "Brady", "tom.brady@email.com",
                                  "junior developer", 30000)
                         ]

    """
    Klasa za kompanija.
    """

    def __init__(self, name: str, company_id: int, address=None):
        """
        Inicijalizirame objekt od klasata Company.

        :param name: str, ime na kompanijata
        :parm company_id: int, unikaten broj na kompanija 
        :param address: str, adresa
        """
        self.name = name
        self.company_id = company_id
        self.address = address

    def hire(self, employee: Employee, position: str, salary: int):
        """
        Vo ovaa funkcija, Company prakja ponuda do vraboteniot
        """
        response = f"{self.name} is making a job offer to {employee.first_name} {employee1.last_name} for the position of {position} with a salary of {salary}."
        return response

    def final_response(self, employee1_response: bool, employee: Employee):
        """
        Vo ovaa funkcija samo printuvame soodvetna poraka ako 
        vraboteniot ja prifakja ponudata ili ne
        """
        if (employee1_response == True):
            Company.Company_Employees.append(employee)
            print(f"Welcome to the company!")
        else:
            print(f"Maybe next time!")

    def print_employees(self):
        """
        Ovaa funkcija gi printuva site vraboteni
        """
        print("Employees:")
        for employee in Company.Company_Employees:
            print(f"{employee.first_name} {employee.last_name} - {employee.position}")

    def employee_quits(self, decision: bool, employee: Employee):
        """
        Ako ovoj vraboten ja napusta firmata,
        treba da go izbrisime od listata
        """
        if (decision == True):
            Company.Company_Employees.remove(employee)
        else:
            pass


semos_mk = Company("Semos Makedonija", 1234)

employee1 = Employee("John", "Doe", "johndoe@email.com",
                     "developer", "semos_mk")


# Baranje 1
company_offer = semos_mk.hire(employee1, "developer", 20000000)

employee1_response = employee1.respond(company_offer)

company_response = semos_mk.final_response(employee1_response, employee1)

semos_mk.print_employees()

# Baranje 2
employee_decision = employee1.leave_company()
print(employee_decision)

semos_mk.employee_quits(employee_decision, employee1)
semos_mk.print_employees()
