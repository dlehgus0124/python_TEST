class Language1:
    default_language = "English"

    def __init__(self):
        self.show = '나의 언어는 ' + self.default_language

    @classmethod
    def class_my_language(cls):
        return cls()

    @staticmethod
    def static_my_language():
        return Language1()

    def print_language(self):
        print(self.show)


class KoreanLanguage1(Language1):
    default_language = "한국어"


a = KoreanLanguage1.class_my_language()
b = KoreanLanguage1.static_my_language()
a.print_language()
b.print_language()
