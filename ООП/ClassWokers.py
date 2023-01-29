workers = [
    {
        "first_name": "Красильников Дмитрий Юрьевич",
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
        "phone": "+7(921)3049965",
        "phone_other": "+7(921)3049965",
        "mail": "detininvi@vniig.ru",
        "post": "рабочий по КО и РЗ",
    },
]


class Vniig:
    def __init__(self, first_name="", phone="",
                 phone_other="", mail="", post=""):
        self.first_name = first_name
        self.phone = phone
        self.phone_other = phone_other
        self.mail = mail
        self.post = post

    def init_from_dict(self, event_dict):
        self.first_name = event_dict.get("first_name")
        self.phone = event_dict.get("phone")
        self.phone_other = event_dict.get("phone_other")
        self.mail = event_dict.get("mail")
        self.post = event_dict.get("post")


for worker in workers:
    staff = Vniig()
    staff.init_from_dict(worker)
    print(staff.first_name, staff.phone_other)
