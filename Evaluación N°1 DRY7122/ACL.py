import os

os.system ("clear")

acl_numberr = int(input("Introduce el número de ACL en IPv4: "))

if acl_numberr >= 1 and acl_numberr <= 99 or acl_numberr >= 1300 and acl_numberr <= 1999:
    print("Es una ACL Estándar.")
elif acl_numberr >= 100 and acl_numberr <= 199 or acl_numberr >= 2000 and acl_numberr <= 2699:
    print("Es una ACL Extendida.")
else:
    print("El número no corresponde a los rangos de las ACL.")