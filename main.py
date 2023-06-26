import sys
from controllers.LoginController import LoginHLP
from models.views import Views
sys.path.append("")
#clear = lambda: os.system('cls')

#def controllerEstadoMain(e):


view = Views()

#if __name__ == "__main__":
while True:
    usuario = view.display_login_screen()
    while usuario == None:
        usuario = view.display_login_screen()

    eleccion = view.display_main_view()
    while eleccion != 3:
        try:
            eleccion = view.display_main_view()
        except ValueError:
            print("Error, intente nuevamente")

    if eleccion == 1:
        view.display_buscar_producto_view()
    elif eleccion == 2:
        view.display_gestionar_carrito_view()






