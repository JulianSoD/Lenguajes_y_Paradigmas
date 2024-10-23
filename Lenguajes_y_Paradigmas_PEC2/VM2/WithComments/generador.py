import random

def generar_archivo_fight():
    instrucciones = []

    # Función para convertir armaduras a su valor
    def obtener_valor_armadura(opcion):
        opciones = {
            "none": 0,
            "basic": 1,
            "rare": 2,
            "epic": 3,
            "legendary": 4
        }
        return opciones.get(opcion.lower(), 0)

    # Función para convertir armas a su valor
    def obtener_valor_arma(opcion):
        opciones = {
            "none": 0,
            "basic": 1,
            "rare": 2,
            "epic": 3,
            "legendary": 4
        }
        return opciones.get(opcion.lower(), 0)

    # Función para convertir experiencia a su valor
    def obtener_valor_experiencia(opcion):
        opciones = {
            "novice": 0.75,
            "beginner": 1,
            "intermediate": 1.25,
            "advanced": 1.5,
            "expert": 1.75,
            "master": 2
        }
        return opciones.get(opcion.lower(), 1)

    # Introducir datos del Combatiente A
    print("Enter the details for Fighter A:")
    armadura_a = input("Armor (none, basic, rare, epic, legendary): ")
    arma_a = input("Weapon (none, basic, rare, epic, legendary): ")
    experiencia_a = input("Experience (novice, beginner, intermediate, advanced, expert, master): ")
    
    # Convertir armadura, arma y experiencia en sus valores
    armadura_a_valor = obtener_valor_armadura(armadura_a)
    arma_a_valor = obtener_valor_arma(arma_a)
    experiencia_a_valor = obtener_valor_experiencia(experiencia_a)

    # Agregar instrucciones del Combatiente A
    instrucciones.append(f"PUSH_A {armadura_a_valor} ; armor for Fighter A")
    instrucciones.append(f"PUSH_A {arma_a_valor} ; weapon for Fighter A")
    instrucciones.append(f"PUSH_A {experiencia_a_valor} ; experience for Fighter A")
    instrucciones.append("MUL_A ; multiply weapon * experience of A")
    instrucciones.append("ADD_A ; add armor + (weapon * experience of A)")

    # Introducir datos del Combatiente B
    print("\nEnter the details for Fighter B:")
    armadura_b = input("Armor (none, basic, rare, epic, legendary): ")
    arma_b = input("Weapon (none, basic, rare, epic, legendary): ")
    experiencia_b = input("Experience (novice, beginner, intermediate, advanced, expert, master): ")
    
    # Convertir armadura, arma y experiencia en sus valores
    armadura_b_valor = obtener_valor_armadura(armadura_b)
    arma_b_valor = obtener_valor_arma(arma_b)
    experiencia_b_valor = obtener_valor_experiencia(experiencia_b)

    # Agregar instrucciones del Combatiente B
    instrucciones.append(f"PUSH_B {armadura_b_valor} ; armor for Fighter B")
    instrucciones.append(f"PUSH_B {arma_b_valor} ; weapon for Fighter B")
    instrucciones.append(f"PUSH_B {experiencia_b_valor} ; experience for Fighter B")
    instrucciones.append("MUL_B ; multiply weapon * experience of B")
    instrucciones.append("ADD_B ; add armor + (weapon * experience of B)")

    # Agregar una línea de finalización
    instrucciones.append("END ; end of the program")

    # Escribir las instrucciones en el archivo
    with open("programa.fight", "w") as archivo:
        archivo.write("\n".join(instrucciones))

    print("File 'programa.fight' generated successfully.")

# Llamar a la función para generar el archivo
if __name__ == "__main__":
    generar_archivo_fight()