class Language2:
    default_language = "English"

    def __init__(self):
        self.show = '나의 언어는' + self.default_language

    @classmethod
    def class_my_language(cls):
        return cls()
    
    @staticmethod
    def static_my_language():
        return Language2()
    
    def print_language(self):
        print(self.show)

class KoreanLanguage2(Language2):
    default_language = "한국어"

a = KoreanLanguage2.class_my_language()
b = KoreanLanguage2.static_my_language()
a.print_language()
b.print_language()