import re
email="11249A167@gmail.com"
print("valid "if re.match(r"^[\w.+-]+@[\w.-]+\.[A-za-z]{2,}$",email) else "invalid")
