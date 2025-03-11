# Base64 Encoder/Decoder

![Banner](/screenshots/header.png)  

Un programa interactivo en Python para codificar (encode) y decodificar (decode) texto en formato Base64. Este programa es útil para trabajar con scripts de PowerShell, datos sensibles o cualquier otro contenido que necesite ser convertido a/desde Base64.

## Características

- **Codificación (Encode):** Convierte texto plano a Base64.
- **Decodificación (Decode):** Convierte texto Base64 a texto plano.
- **Interfaz Colorida:** Usa colores para mejorar la experiencia del usuario.
- **Fácil de Usar:** Interfaz interactiva con menú de opciones.

## Requisitos

- **Python 3.x:** El programa está escrito en Python y requiere una versión reciente de Python.
- **Biblioteca `colorama`:** Se utiliza para añadir colores a la terminal.

### Instalación de Dependencias

1. Clona o descarga este repositorio.
2. Instala las dependencias ejecutando el siguiente comando:

   ```bash
   pip install colorama
   ```
3. Sigue las instrucciones en pantalla:
   - Selecciona la opción `1` para codificar texto a Base64.
   - Selecciona la opción `2` para decodificar texto desde Base64.
   - Selecciona la opción `3` para salir del programa.

### Ejemplo de Codificación

Supongamos que quieres codificar el texto `"Hola Mundo"`:

1. Selecciona la opción `1` en el menú.
2. Ingresa el texto: `Hola Mundo`.
3. El programa devolverá algo como: `SG9sYSBNdW5kbyA=`.

### Ejemplo de Decodificación

Si tienes una cadena Base64 como la anterior (`SG9sYSBNdW5kbyA=`):

1. Selecciona la opción `2` en el menú.
2. Ingresa la cadena Base64: `SG9sYSBNdW5kbyA=`.
3. El programa devolverá: `Hola Mundo`


## Contribuciones

Si deseas contribuir al proyecto, ¡eres bienvenido! Puedes hacerlo de las siguientes maneras:

1. **Reportar Problemas:** Si encuentras algún error o problema, abre un issue en el repositorio.
2. **Sugerir Mejoras:** Si tienes ideas para mejorar el programa, compártelas en los issues.
3. **Enviar Pull Requests:** Si has mejorado el código, envía un pull request con tus cambios.

## Autor

Creado por **Folkencillo**.  
Contacto: **juanguerrero.dev@ejemplo.com**.
GitHub: **https://github.com/Folkenciyo/**

---

### Notas Finales

Este programa fue diseñado para ser simple y funcional, pero también visualmente atractivo. Espero que te sea útil para tus proyectos relacionados con Base64. ¡Gracias por usarlo!
