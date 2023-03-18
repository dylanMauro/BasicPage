import pymysql
from os import system as sys
import subprocess

conn = pymysql.connect(
    host= "localhost",
    user="root",
    passwd="dylan1296",
    db="pruebas1"
)

cur = conn.cursor()
# Cerrar la conexion a la base de datos
cur.execute("SELECT * FROM products;")
for product in cur.fetchall():
    print(product[1])

conn.close()

resultado = subprocess.check_output("wmic bios get serialnumber")
resultado = str(resultado)
resultado = resultado[2:-2]
