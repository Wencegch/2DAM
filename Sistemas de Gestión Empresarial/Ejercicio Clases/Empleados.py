class Empleado():
    multiplicador = 1
   
    def __init__(self,nombre="",apellido1="",apellido2="",dni="",direccion="",telefono=0,salario=1,supervisor=""):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.salario = salario
        self.supervisor = supervisor
        pass
    
    def toString(self):
        aux = "Nombre: " + self.nombre + "\nApellidos :" + self.apellido1 + " " + self.apellido2
        aux = aux + "\nDNI: " + self.dni + "\nDireccion: " + str(self.direccion) + "\nTelefono: " + str(self.telefono)
        aux = aux + "\nSalario: " + str(self.salario) + "\nSupervisor: " + self.supervisor
        return aux
    
    def setSupervisor(self,supervisor=""):
        self.supervisor = supervisor
    
    def incrementarSalario(self):
        self.salario *= self.multiplicador
class Secretario(Empleado):
    
    def __init__(self, nombre="", apellido1="", apellido2="", dni="", direccion="", telefono=0, salario=1, supervisor=""
    ,despacho="",fax=0):
        super().__init__(nombre, apellido1, apellido2, dni, direccion, telefono, salario, supervisor)
        self.despacho = despacho
        self.fax = fax
        self.multiplicador = 1.05
    
    def toString(self):
        return "Secrectario/a: \n" + super().toString() + "\nDespacho: " + self.despacho +"\nFax: " + str(self.fax)

class Coche():
    
    def __init__(self,matricula="", marca="", modelo=""):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo

class Vendedor(Empleado):
    
    def __init__(self, nombre="", apellido1="", apellido2="", dni="", direccion="", telefono=0, salario=1, supervisor="",
    coche=Coche(),telefonoMovil=0,areaTrabajo="",listaClientes=list(),porcentajeVentas=0):
        super().__init__(nombre, apellido1, apellido2, dni, direccion, telefono, salario, supervisor)
        self.multiplicador = 1.10
        self.coche = coche
        self.telefonoMovil = telefonoMovil
        self.areaTrabajo = areaTrabajo
        self.listaClientes = listaClientes
        self.porcentajeVentas= porcentajeVentas
    
    def cambiarCoche(self,coche=Coche()):
        self.coche = coche
    
    def altaCliente(self,cliente=""):
        self.listaClientes.append(cliente)
    
    def bajaCliente(self,cliente=""):
        self.listaClientes.remove(cliente)
    
    def toString(self):
        aux = "Vendedor: \n" + super().toString() + "\nCoche" + self.coche.matricula + "\nTelefono Movil: " + str(self.telefonoMovil)
        aux = aux + "\nArea de trabajo: " + self.areaTrabajo + "\nLista de clientes: " + self.clientes()
        aux = aux + "\nPorecentaje de las ventas: " + str(self.porcentajeVentas)
        return aux
    
    def clientes(self):
        aux =""
        if len(self.listaClientes) != 0:
            for cliente in self.listaClientes:
                if len(self.listaClientes) == 1:
                    aux = aux + cliente
                else:
                    aux = aux + ", " +cliente
        return aux

class JefeZona(Empleado):
    
    def __init__(self, nombre="", apellido1="", apellido2="", dni="", direccion="", telefono=0, salario=1, supervisor="",
    secretario=Secretario(),despacho="",listaVendedores=list(),coche=Coche()):
        super().__init__(nombre, apellido1, apellido2, dni, direccion, telefono, salario, supervisor)
        self.multiplicador = 1.20
        self.secretario = secretario
        self.despacho=despacho
        self.listaVendedores = listaVendedores
        self.coche = coche
    
    def toString(self):
        aux = "Jefe de Zona: \n" + super().toString() + "\nSecretario: " + self.secretario.dni + "\nDespacho: " + self.despacho
        aux = aux + "\nLista de Vendedores: " + self.vendedores() + "\nCoche: " + self.coche.matricula
        return aux
    
    def setSecretario(self,secretario=Secretario()):
        self.secretario = secretario
    
    def setCoche(self,coche=Coche()):
        self.coche = coche
    
    def vendedores(self):
        aux =""
        for vendedor in self.listaVendedores:
            aux = aux + vendedor.nombre +", "
        return aux

empleado1 = Empleado("Wenceslao","García","Chando","1234567F","C/ Ayala, 4",655555555,1600)
secretario1 = Secretario("Miguel","Ángel","Rubiño","2345678G","C/ Atocha, 3",644444444, 1500,empleado1.dni,"Despacho1",47543)
vendedor1 = Vendedor("Antonio","Alcalde","Gómez","3456789H","C/ Culmen,3",633333333, 1400,empleado1.dni,Coche("1234str","Seat","Ibiza"),72534,"Madrid",["Cliente1"],1.03)
jefe1 = JefeZona("José","Luis","Carrasco","4567890J","C/ Ron Barceló,5",123123123,1400,"Sin Supervisor",secretario1,"GranDespacho1",[vendedor1],Coche("5555abz","Seat","Panda"))
print("---------------------")
print(empleado1.toString())
print("")
print(secretario1.toString())
print("")
print(vendedor1.toString())
print("")
print(jefe1.toString())
print("---------------------")
empleado1.incrementarSalario()
secretario1.incrementarSalario()
vendedor1.incrementarSalario()
jefe1.incrementarSalario()
print("---------------------")
print(empleado1.toString())
print("")
print(secretario1.toString())
print("")
print(vendedor1.toString())
print("")
print(jefe1.toString())
print("---------------------")