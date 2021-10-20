class Celular:
    
    screen_size = 5,8

    screen_size2 = 6
    
    smart_color = "negro"

    smart_color2 = "verde"

    company = "xiamoi"

    company2 = "Huawei"

    def reset(self):
        print("Reiniciando")

    def shut_down(self, user_name):
        print("Apagando " + user_name)

    def modo_depuracion(self):
        print("Entraste al modo de depuracion")

    def erase_app(self):
        print("Borrando aplicacion")

    def copy_document(self):
        print("Copiando documento")

    def move_document(self):
        print("Moviendo docuemnto")

celular_one = Celular()
print(celular_one)
print(celular_one.screen_size)
print(celular_one.smart_color)
print(celular_one.company)
celular_one.reset()
celular_one.shut_down("Alejandro")
celular_one.modo_depuracion()


celular_two = Celular()
print(celular_two)
print(celular_two.screen_size2)
print(celular_two.smart_color2)
print(celular_two.company2)
celular_two.erase_app()
celular_two.copy_document()
celular_two.move_document()