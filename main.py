import sys
from controllers.LoginController import LoginHLP
from models.views import Views
sys.path.append("")
#clear = lambda: os.system('cls')

#def controllerEstadoMain(e):


view = Views()

#if __name__ == "__main__":
while True:
    usuario = view.display_login_screen() #mostrar login
    while usuario == None:
        usuario = view.display_login_screen()

    eleccion = view.display_main_view()
    while eleccion != 3: # main menu
        try:
            if eleccion == 1: # buscar producto
                carrito = view.display_catalogo_productos_view()


            elif eleccion == 2: # gestionar carrito
                view.display_gestionar_carrito_view(carrito)
            else:
                print("Opción inválida.")
        except ValueError:
            print("Error, intente nuevamente")

        eleccion = view.display_main_view()

