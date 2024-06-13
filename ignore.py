import os

def crear_gitignore_proyecto(proyecto_path):
    gitignore_path = os.path.join(proyecto_path, '.gitignore')
    contenido_gitignore = """
# Ignorar la carpeta .idea
.idea/

# Ignorar todo en .venv excepto la carpeta Scripts y el archivo .py principal
.venv/*
!.venv/Scripts/
.venv/Scripts/*
!.venv/Scripts/*.py

# Ignorar archivo específico que no se debe subir
activate_this.py

# No ignorar el archivo readme.txt dentro de .venv/Scripts
!.venv/Scripts/readme.txt
    """

    with open(gitignore_path, 'w') as gitignore_file:
        gitignore_file.write(contenido_gitignore.strip())

def eliminar_gitignore_venv(venv_path):
    gitignore_path = os.path.join(venv_path, '.gitignore')
    try:
        os.remove(gitignore_path)
        print(f"Archivo .gitignore eliminado en: {venv_path}")
    except FileNotFoundError:
        print(f"No se encontró archivo .gitignore en: {venv_path}")

def procesar_proyectos():
    script_dir = os.path.dirname(os.path.realpath(__file__))  # Directorio del script actual
    base_path = os.getcwd()  # Directorio actual donde se ejecuta el script

    for root, dirs, files in os.walk(base_path):
        if '.git' in dirs:
            dirs.remove('.git')  # Ignorar el directorio .git del repositorio raíz

        for dir_name in dirs:
            proyecto_path = os.path.join(root, dir_name)

            # Ignorar carpetas .idea y .venv de los proyectos
            if dir_name == ".idea" or dir_name == ".venv":
                continue
            
            # Evitar procesar el directorio donde reside el script actual
            if proyecto_path == script_dir:
                continue

            # Crear .gitignore en el proyecto
            crear_gitignore_proyecto(proyecto_path)
            print(f"Creado .gitignore en: {proyecto_path}")

            # Eliminar .gitignore en .venv si existe
            venv_path = os.path.join(proyecto_path, '.venv')
            if os.path.exists(venv_path):
                eliminar_gitignore_venv(venv_path)

        # No seguir recorriendo subdirectorios recursivamente dentro de cada proyecto
        dirs[:] = []

if __name__ == "__main__":
    procesar_proyectos()
