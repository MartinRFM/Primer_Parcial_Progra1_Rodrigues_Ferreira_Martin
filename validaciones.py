def validacion(min_num:int, max_num: int) -> int:
    opciones = input(f"Ingresar una opcion entre {min_num} y {max_num}: ")
    if not opciones or not opciones.isdigit() or not (min_num <= int(opciones) <= max_num):
        return (validacion(min_num, max_num))
    else:
        opciones = int(opciones)
        return opciones
