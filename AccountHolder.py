class AccountHolder:

    def __init__(self, name, addr, phone, bd, ssn):
        self._name = name
        self._addr = addr
        self._phone = phone
        self._bd = bd
        self._ssn = ssn

    def get_name(self):
        return self._name

    def get_phone(self):
        return self._phone

    def set_phone(self, phone):
        self._phone = phone

    def get_addr(self):
        return self._addr

    def set_addr(self, addr):
        self._addr = addr
