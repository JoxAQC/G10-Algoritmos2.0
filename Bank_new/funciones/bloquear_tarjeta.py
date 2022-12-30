from validaciones.validar_registro_cliente import Validar_registro_cliente
from consultas.db_validar_cliente import Db_validar_cliente
from consultas.db_buscar_num_cuenta import Db_buscar_num_cuenta
from consultas.db_validar_tarjeta import Db_validar_tarjeta
from consultas.db_devolver_num_cuenta import Db_devolver_num_cuenta
import sqlite3

class Bloquear_tarjeta:
    def __init__(self):
        self.dni = input("DNI: ")
        self.clave_tarjeta = str(input("Clave tarjeta: "))
        self.bloquear_tarjetita()

    def validacion(self):
        validar = Validar_registro_cliente(self.dni)
        if validar.convalidar_dni() == True:
            db_validar = Db_validar_cliente(self.dni)
            if db_validar.existe_cuenta_cliente() == True:
                db_buscar = Db_buscar_num_cuenta(self.dni)
                if db_buscar.buscar() == True:
                    db_devolver_cuenta = Db_devolver_num_cuenta(self.dni)
                    num_cuenta = db_devolver_cuenta.devolver_num_cuenta()
                    db_tarjeta = Db_validar_tarjeta(num_cuenta)
                    if db_tarjeta.existe_tarjeta() == True:
                        return True,num_cuenta
                    else:
                        return False
        else:
            return False

    def bloquear_tarjetita(self):
        connection_obj = sqlite3.connect('Bank_new/DataBase/banquito.db')
        cur = connection_obj.cursor() 
        cur.execute(f"SELECT num_cuenta FROM cuentas_bancarias WHERE dni like '%{self.dni}%'")
        dato = cur.fetchone()
        connection_obj.close()
        print(dato[0])
        num_cuenta = str(dato[0]) 
        connection_obj2 = sqlite3.connect('Bank_new/DataBase/banquito.db')
        cursor_obj = connection_obj2.cursor()
        new_column = f"UPDATE tarjeta SET bloqueo='bloqueado' WHERE num_cuenta='{num_cuenta}'"
        cursor_obj.execute(new_column)
        connection_obj2.commit()
        connection_obj2.close()