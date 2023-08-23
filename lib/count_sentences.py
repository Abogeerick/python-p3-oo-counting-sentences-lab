#!/usr/bin/env python3

class MyString:
    def __init__(self, value=None):
        self._value = None

        if value is not None:
            self.set_value(value)

    def set_value(self, input):
        if isinstance(input, str):
            self._value = input
        else:
            print("The value must be a string.")

    def get_value(self):
        return self._value

    def is_sentence(self):
        if self._value is not None and self._value[-1] == ".":
            return True
        else:
            return False
        
    def is_question(self):
        if self._value is not None and self._value[-1] == "?":
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self._value is not None and self._value[-1] == "!":
            return True
        else:
            return False
        
    def count_sentences(self):
        if self._value is not None:
            standardized_value = self._value.replace("?", ".").replace("!", ".")

            sentences = standardized_value.split(".")
            sentences = [s.strip() for s in sentences if s.strip()]

            return len(sentences)
        else:
            return 0
        
    value = property(get_value, set_value)


  
erick = MyString("Hello World.")
print(erick.is_sentence())




