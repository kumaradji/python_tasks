workers = [
    {
        "first_name": "Красильников Дмитрий Юрьевич",
        "address": "ул. Вавиловых, д.11, к.1, кв.193",
        "phone": "+7(967)5941552",
        "phone_other": "+7(921)7968873",
        "mail": "krasilnikovdy@vniig.ru",
        "post": "заместитель начальника отдела",
    },
    {
        "first_name": "Горшкова Людмила Александровна",
        "phone": "+7(921)7971243",
        "phone_other": "",
        "mail": "gorshkovala@vniig.ru",
        "post": "и.о. начальника УАО",
    },
    {
        "first_name": "Ващенко Андрей Александрович",
        "phone": "+7(952)2480824",
        "mail": "",
        "phone_other": "",
        "post": "рабочий по КО и РЗ",
    },
    {
        "first_name": "Детинин Владимир Иванович",
        "address": "ул. Белы-Куна, д.20 к.3 кв.91",
        "phone": "+7(921)3049965",
        "phone_other": "+7(921)3049965",
        "mail": "detininvi@vniig.ru",
        "post": "рабочий по КО и РЗ",
        "birthday": "03 июня 1972"
    },
]


class Vniig:
    def __init__(self, first_name="", address="", phone="",
                 phone_other="", mail="", post="", birthday=""):
        self.first_name = first_name
        self.address = address
        self.phone = phone
        self.phone_other = phone_other
        self.mail = mail
        self.post = post
        self.birthday = birthday

    def init_from_dict(self, event_dict):
        self.first_name = event_dict.get("first_name")
        self.address = event_dict.get("address")
        self.phone = event_dict.get("phone")
        self.phone_other = event_dict.get("phone_other")
        self.mail = event_dict.get("mail")
        self.post = event_dict.get("post")
        self.birthday = event_dict.get("birthday")


for worker in workers:
    staff = Vniig()
    staff.init_from_dict(worker)
    print(staff.first_name)
    print(staff.post)
    print(staff.address)
    print(staff.birthday)
    print('-       ---       -')