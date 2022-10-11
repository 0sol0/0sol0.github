class Profile():
    def __init__(self):
        self.profile = {
                        'name': '-',
                        'gender': '-',
                        'birthday': '-',
                        'age': '-',
                        'phone': '-',
                        'email': '-'
                        }
    
    def set_profile(self, profile):
        self.profile = profile

    def get_name(self):
        return self.profile['name']

    def get_gender(self):
        return self.profile['gender']

    def get_birthday(self):
        return self.profile['birthday']

    def get_age(self):
        return self.profile['age']

    def get_phone(self):
        return self.profile['phone']

    def get_email(self):
        return self.profile['email']

            

profile = Profile()
profile.set_profile({
    'name': 'DaSol',
    'gender': 'woman',
    'birthday': '05/21',
    'age': 26,
    'phone': '010-1234-5678',
    'email': 'jdsmy1004@gmail.com'
})

print(profile.get_name())
print(profile.get_gender())
print(profile.get_birthday())
print(profile.get_age())
print(profile.get_phone())
print(profile.get_email())