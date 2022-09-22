class PhoneNumber:
    def __init__(self, phone):
        self.phone = phone
        self.clean_err()

    def clean_number_phone(self):
        for char in ".- ,()+":
            self.phone = self.phone.replace(char, "")
        return self.phone

    def pretty(self):
        self.clean_number_phone()
        self.start_with_11()
        phone_pretty = f'({self.phone[:3]})-{self.phone[3:6]}-{self.phone[6:]}' 
        return phone_pretty
    
    def start_with_11(self):
        self.clean_number_phone()
        first_number_code_area_len11 = self.phone[0]
        if len(self.phone) == 11 and first_number_code_area_len11 == '1':
            self.phone = self.phone.replace('1', '')
        return self.phone

    @property
    def area_code(self):
        self.clean_number_phone()
        self.start_with_11()
        return self.phone[:3]
    
    @property
    def number(self):
        self.clean_number_phone()
        self.start_with_11()
        return self.phone

    def __str__(self) -> str:
        return self.phone

    def clean_err(self):
        self.clean_number_phone()

        first_number_code_area = self.phone[0]
        first_number_code_area_len11 = self.phone[1]
        first_exchange_code = self.phone[3]
        first_exchange_code_len11 = self.phone[4] 

        for char in self.phone:
            if char in "!@:;?":
                raise ValueError("punctuations not permitted")
            if char in "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ":
                raise ValueError("letters not permitted")
                
        if len(self.phone) < 10:
            raise ValueError("incorrect number of digits")
        elif len(self.phone) == 11:
            if first_number_code_area_len11 == '0':
                raise ValueError("area code cannot start with zero")
            elif first_number_code_area_len11 == '1':
                raise ValueError("area code cannot start with one") 
            elif first_exchange_code_len11 == '0':
                raise ValueError("exchange code cannot start with zero")
            elif first_exchange_code_len11 == '1':
                raise ValueError("exchange code cannot start with one")
            elif self.phone[0] != '1':
                raise ValueError("11 digits must start with 1")
        elif len(self.phone) > 11:
            raise ValueError("more than 11 digits")
        else:
            if first_number_code_area == '0':
                raise ValueError("area code cannot start with zero")
            elif first_number_code_area == '1':
                raise ValueError("area code cannot start with one")
            elif first_exchange_code == '0':
                raise ValueError("exchange code cannot start with zero")
            elif first_exchange_code == '1':
                raise ValueError("exchange code cannot start with one")
        

