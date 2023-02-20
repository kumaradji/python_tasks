from string import ascii_letters


class Vniig:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio="", phone="", phone_other="",
                 mail="", post="", birthday=""):
        # self.verify_fio(fio)

        self.__fio = fio  # .split()  # проверить нужно ли?
        self.__phone = phone
        self.__phone_other = phone_other
        self.__mail = mail
        self.__post = post
        self.__birthday = birthday

    @classmethod  # метод для проверки корректности ФИО
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО должны быть буквы и дефис")

    #
    @property
    def get_worker(self):

        def init_from_dict(self, event_dict):
            self.fio = event_dict.get("fio")
            self.phone = event_dict.get("phone")
            self.phone_other = event_dict.get("phone_other")
            self.mail = event_dict.get("mail")
            self.post = event_dict.get("post")
            self.birthday = event_dict.get("birthday")


for worker in workers:
    staff = Vniig()
    staff.init_from_dict(worker)
    print(staff.fio)
    print(staff.post)
    print(staff.birthday)
    print('-       ---       -')

# p = Vniig("Кольцов Сергей Викторович")
