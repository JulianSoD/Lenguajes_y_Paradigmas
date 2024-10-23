# MAQUINA VIRTUAL 

Este proyecto implementa una **Máquina Virtual (VM)** que opera sobre una pila de números y puede realizar operaciones aritméticas básicas (suma, resta, multiplicación, división), así como cargar y ejecutar archivos de texto con comandos. También es capaz de generar archivos de audio WAV basados en los resultados de las operaciones.

## ¿Qué es?

El proyecto **VM Pila** es una simulación de una máquina virtual que utiliza una interfaz gráfica de usuario (GUI) desarrollada en **Tkinter**. La VM permite al usuario ejecutar operaciones sobre una pila y producir sonidos basados en esos resultados. El proyecto incluye un componente visual que permite ingresar operaciones manualmente o cargar archivos de texto con comandos, y la VM genera archivos de audio si el resultado cumple con ciertos criterios.





## ¿Qué puede hacer?

- **Operaciones en la pila**: La VM puede realizar las siguientes operaciones:
  - `PUSH <número>`: Añadir un número a la pila.
  - `POP`: Eliminar el número en la parte superior de la pila.
  - `ADD`, `SUB`, `MUL`, `DIV`: Realizar operaciones aritméticas entre los dos números en la parte superior de la pila.
  
- **Generación de audio**: Dependiendo del resultado de las operaciones en la pila, la VM puede generar archivos WAV que incluyen sonidos de bombo, hi-hat, y platillo. El número de compases (medido por el resultado de la operación) determina cómo se genera el audio.
  
- **Carga de archivos**: Es posible cargar archivos de texto con una serie de comandos para ser ejecutados por la VM.




## ¿Qué necesitas para usarlo?
### Requisitos:

- **Python 3.x** instalado.
- Las siguientes librerías de Python:
  - **Tkinter**: Se utiliza para la interfaz gráfica.
  - **Numpy**: Para trabajar con datos numéricos y generar las ondas de sonido.
  - **Wave**: Para la manipulación de archivos WAV.
  
  Puedes instalar las dependencias con:
  ```
  pip install numpy
  ```

- **Archivos de sonido**: Se utilizan archivos WAV específicos para generar los sonidos de bombo (`kick.wav`), hi-hat (`hat.wav`), y platillo (`cymbal.wav`). Estos archivos deben estar en la carpeta `samples/` dentro del proyecto.






## ¿Cómo usarlo?

1. **Ejecutar el programa**:
   
   El archivo principal es `main.py`, el cual lanza la interfaz gráfica. Puedes ejecutarlo con:

   ```
   python main.py
   ```

2. **Operaciones**:

   - Puedes ingresar operaciones en el campo de texto de la interfaz, como `PUSH 5`, `ADD`, `POP`, etc.
   - También puedes cargar un archivo de texto que contenga varias operaciones. El archivo debe tener una operación por línea.
   
3. **Generar archivos de audio**:
   
   Si el resultado de las operaciones está entre 0 y 29, puedes generar un archivo WAV utilizando el botón correspondiente en la interfaz gráfica.




## Estructura del proyecto
```
proyecto_vm_pila/
├── main.py
├── src/
│   ├── vm_interface.py
│   └── virtual_machine.py
└── samples/
    ├── kick.wav
    ├── hat.wav
    └── cymbal.wav
```



### Archivos del proyecto:

- **main.py**: Este archivo es el punto de entrada del programa y se encarga de crear la ventana principal de la aplicación utilizando Tkinter. Carga la interfaz de la VM.

- **vm_interface.py**: Define la interfaz gráfica de la aplicación. Los usuarios pueden ingresar operaciones manualmente o cargar archivos de texto con comandos, y también generar archivos WAV según el resultado de las operaciones.
 
- **virtual_machine.py**: Implementa la lógica de la VM, incluyendo las operaciones aritméticas, el manejo de la pila, y la creación de archivos WAV basados en el resultado de las operaciones.

- **samples/**: Contiene los archivos de sonido (`kick.wav`, `hat.wav`, `cymbal.wav`) que son utilizados para generar el audio cuando se crea un archivo WAV.




## Requisitos adicionales

- **Archivos WAV**: Asegúrate de que los archivos `kick.wav`, `hat.wav`, y `cymbal.wav` estén presentes en la carpeta `samples/`, ya que son necesarios para la generación de audio.

- **Tkinter**: Es parte de la instalación estándar de Python, pero asegúrate de tenerlo disponible en tu sistema.





## Funcionamiento general

Este proyecto simula una máquina virtual que maneja una pila de números. El usuario puede ejecutar operaciones, cargar archivos de comandos, y generar audio en función de los resultados obtenidos. Cada parte del código está dividida en archivos para facilitar la gestión de la interfaz gráfica, la lógica de la VM, y la generación de sonidos.

