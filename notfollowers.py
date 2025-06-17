import re
from colorama import init, Fore

init(autoreset=True)  # Activa color en Windows CMD

def banner():
    print(Fore.RED + r"""
  _   _       _   ______    _ _
 | \ | |     | | |  ____|  | | |
 |  \| | ___ | |_| |__ ___ | | | _____      _____ _ __ ___
 | . ` |/ _ \| __|  __/ _ \| | |/ _ \ \ /\ / / _ | '__/ __|
 | |\  | (_) | |_| | | (_) | | | (_) \ V  V |  __| |  \__ \
 |_| \_|\___/ \__|_|  \___/|_|_|\___/ \_/\_/ \___|_|  |___/
""" + "by: @meelo1".center(59))

def extraer_usuarios(ruta_html, nombre_archivo_salida):
    print(f"\n[INFO] Cargando archivo: {ruta_html}")
    try:
        with open(ruta_html, "r", encoding="utf-8") as f:
            contenido = f.read()
    except Exception as e:
        print(f"[X] Error al abrir el archivo: {e}")
        return set()

    print("[INFO] Buscando nombres de usuario...")
    usuarios = re.findall(r'https://www\.instagram\.com/([a-zA-Z0-9_.]+)', contenido)
    print(f"[OK] {len(usuarios)} usuarios encontrados.")
    usuarios_unicos = sorted(set(usuarios))
    try:
        with open(nombre_archivo_salida, "w", encoding="utf-8") as f:
            for usuario in usuarios_unicos:
                f.write(usuario + "\n")
        print(f"[OK] Guardado en: {nombre_archivo_salida}")
    except Exception as e:
        print(f"[X] Error al guardar: {e}")

    return set(usuarios_unicos)

def main():
    banner()
    print("="*50)
    print("[START] INICIO DEL PROCESO DE COMPROBACIÓN DE FOLLOWERS")
    print("="*50)

    ruta_followers = r"C:\Users\Meelo\Desktop\notfollowers\followers.html"
    ruta_following = r"C:\Users\Meelo\Desktop\notfollowers\following.html"

    followers = extraer_usuarios(ruta_followers, "followers.txt")
    following = extraer_usuarios(ruta_following, "following.txt")

    print("\n[INFO] Comparando archivos...")
    notfollowers = sorted(following - followers)
    print(f"[RESULT] Usuarios que SIGUES pero NO te siguen: {len(notfollowers)}")

    try:
        with open("notfollowers.txt", "w", encoding="utf-8") as f:
            for usuario in notfollowers:
                f.write(usuario + "\n")
        print("[OK] Resultado guardado en: notfollowers.txt")
    except Exception as e:
        print(f"[X] Error al guardar notfollowers.txt: {e}")

    print("="*50)
    print("[END] PROCESO COMPLETADO")
    print("="*50)

if __name__ == "__main__":
    main()
