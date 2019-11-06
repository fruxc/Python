class err(Exception):
    def __init__(self,error):
        self.error_name=error;

    def get_error(self):
        return "{}".format(self.error_name);



try:
    name=input("Enter name ");
    if not name:
        raise(err("String  cannot be empty"));
    email=input("Enter email ");
    if not email:
        raise(err("Email cannot be empty"));
    if "@" not in email or "." not in email:
        raise(err("Invalid email address"));
    age=int(input("Enter age "));
    if age < 18:
        raise(err("Age cannot be less than 18"));

    print("The entered information is valid ");
    print("Name = ",name);
    print("Age = ",age);
    print("Email = ",email);
except err as e:
    print(e.get_error());

