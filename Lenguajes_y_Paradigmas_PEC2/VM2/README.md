# Stack-Based Combat Simulator

Este es un simulador de combate basado en una máquina virtual de pila. Puedes establecer combatientes, maldecir o bendecir su poder, visualizar su poder y hacer que luchen entre ellos para ver quién es el ganador. El simulador utiliza un archivo de instrucciones (`programa.fight`) para ejecutar las acciones y modificar las características de los combatientes. Podrás observar que hay 2 MV, una de ellas explica detalladamente cada proceso e interacción que hay con la pila.

## Características

- **Establecer Combatientes:** Configura o sobrescribe las características de dos combatientes, como su armadura, arma y nivel de experiencia.
- **Maldecir Combatiente:** Reduce el poder total de un combatiente dividiendo su poder por un número aleatorio entre 1 y 10.
- **Bendecir Combatiente:** Aumenta el poder total de un combatiente sumándole un número aleatorio entre 0 y 10.
- **Ver Poder de los Combatientes:** Muestra el poder actual de ambos combatientes.
- **Luchar:** Compara el poder de los dos combatientes y determina el ganador.
- **Salir:** Elimina el archivo `programa.fight` y cierra el programa.

## Requisitos

- Python 3.x

## Estructura de Archivos

- `main.py`: El archivo principal que ejecuta el programa de la máquina virtual.
- `generador.py`: El archivo que genera las instrucciones iniciales para establecer los combatientes.
- `programa.fight`: Archivo que contiene las instrucciones que serán ejecutadas por la máquina virtual.

## Cómo Ejecutar

### Paso 1: Ejecutar el Programa

Primero, asegúrate de tener Python instalado en tu sistema. Luego, ejecuta el archivo `main.py` para iniciar el menú principal:

```bash
python main.py
```

### Paso 2: Opciones del Menú

Una vez que ejecutes `main.py`, verás un menú con varias opciones:

1. **Establecer Combatientes:** Ejecuta el script `generador.py` para configurar los combatientes. Si ya existe un archivo `programa.fight`, este se sobrescribirá al crear nuevos combatientes.
   
2. **Maldecir Combatiente:** Reduce el poder de uno de los combatientes dividiendo su poder por un número aleatorio. Si no hay combatientes establecidos (es decir, si no existe `programa.fight`), verás un mensaje indicando que no hay combatientes.

3. **Bendecir Combatiente:** Aumenta el poder de uno de los combatientes sumando un número aleatorio. Esta opción tampoco estará disponible si no se han establecido combatientes previamente.

4. **Ver Poder de los Combatientes:** Muestra el poder actual de ambos combatientes. Si no se han establecido combatientes, también verás un mensaje que indicará que no hay combatientes disponibles.

5. **Luchar:** Compara el poder de los dos combatientes y determina el ganador. Esta opción no estará disponible si no hay combatientes establecidos.

6. **Salir:** Elimina el archivo `programa.fight` y cierra el programa.

### Nota Importante

Si no has configurado los combatientes con la opción **Establecer Combatientes**, las opciones de **Maldecir**, **Bendecir** y **Ver Poder de los Combatientes** no estarán disponibles hasta que se establezcan los combatientes.

## Paso 3: Ejemplo de Ejecución

1. **Establecer Combatientes:**

   Configura las armaduras, armas y experiencia de ambos combatientes a través del script `generador.py`. Si ya existen combatientes, serán sobrescritos.

2. **Maldecir o Bendecir Combatientes:**

   Puedes reducir o aumentar el poder de un combatiente usando un número aleatorio que se añadirá al archivo de instrucciones `programa.fight`.

3. **Ver Poder de los Combatientes:**

   Visualiza el poder actual de los combatientes en cualquier momento.

4. **Luchar:**

   Compara los poderes de los dos combatientes y determina el ganador basándose en sus atributos actuales.

## Salir

Eligiendo la opción **Salir**, se eliminará el archivo `programa.fight`, lo que evitará que las opciones de bendecir, maldecir o visualizar el poder de los combatientes funcionen hasta que se configuren nuevamente.

## Contribuciones

Julián Sopeña