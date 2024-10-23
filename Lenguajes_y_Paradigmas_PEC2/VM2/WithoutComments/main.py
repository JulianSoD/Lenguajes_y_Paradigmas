import random
import subprocess
import os

class StackBasedVM:
    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def push_a(self, value):
        self.stack_a.append(value)
        print(f"Pushed {value} onto Fighter A's stack. Current stack A: {self.stack_a}")

    def push_b(self, value):
        self.stack_b.append(value)
        print(f"Pushed {value} onto Fighter B's stack. Current stack B: {self.stack_b}")

    def pull_a(self):
        if self.stack_a:
            value = self.stack_a.pop()
            print(f"Pulled {value} from Fighter A's stack. Current stack A: {self.stack_a}")
            return value
        return 0

    def pull_b(self):
        if self.stack_b:
            value = self.stack_b.pop()
            print(f"Pulled {value} from Fighter B's stack. Current stack B: {self.stack_b}")
            return value
        return 0

    def mul_a(self):
        b = self.pull_a()  # Arma
        a = self.pull_a()  # Experiencia
        result = a * b
        self.push_a(result)
        print(f"Fighter A: Multiplied experience * weapon = {result}. Current stack A: {self.stack_a}")

    def add_a(self):
        b = self.pull_a()  # Resultado de experiencia * arma
        a = self.pull_a()  # Armadura
        result = a + b
        self.push_a(result)
        print(f"Fighter A: Added armor + (weapon * experience) = {result}. Current stack A: {self.stack_a}")

    def mul_b(self):
        b = self.pull_b()  # Arma
        a = self.pull_b()  # Experiencia
        result = a * b
        self.push_b(result)
        print(f"Fighter B: Multiplied experience * weapon = {result}. Current stack B: {self.stack_b}")

    def add_b(self):
        b = self.pull_b()  # Resultado de experiencia * arma
        a = self.pull_b()  # Armadura
        result = a + b
        self.push_b(result)
        print(f"Fighter B: Added armor + (weapon * experience) = {result}. Current stack B: {self.stack_b}")

    def curse_a(self, divisor):
        total_power = self.pull_a()  # Poder total de A
        result = total_power / divisor
        self.push_a(result)  # Guardar el poder reducido
        print(f"Fighter A: Cursed! Divided power by {divisor}, result = {result}. Current stack A: {self.stack_a}")

    def curse_b(self, divisor):
        total_power = self.pull_b()  # Poder total de B
        result = total_power / divisor
        self.push_b(result)  # Guardar el poder reducido
        print(f"Fighter B: Cursed! Divided power by {divisor}, result = {result}. Current stack B: {self.stack_b}")

    def bless_a(self, blessing):
        total_power = self.pull_a()  # Poder total de A
        result = total_power + blessing
        self.push_a(result)  # Guardar el poder aumentado
        print(f"Fighter A: Blessed! Added {blessing}, result = {result}. Current stack A: {self.stack_a}")

    def bless_b(self, blessing):
        total_power = self.pull_b()  # Poder total de B
        result = total_power + blessing
        self.push_b(result)  # Guardar el poder aumentado
        print(f"Fighter B: Blessed! Added {blessing}, result = {result}. Current stack B: {self.stack_b}")

    def compare(self):
        score_a = self.pull_a()  # Puntaje final de A
        score_b = self.pull_b()  # Puntaje final de B
        print(f"Comparing scores: Fighter A = {score_a}, Fighter B = {score_b}")
        if score_a > score_b:
            print("Fighter A wins!")
        elif score_a < score_b:
            print("Fighter B wins!")
        else:
            print("It's a tie!")

    def execute_instruction(self, instruction):
        print(f"Executing instruction: {instruction.strip()}")
        parts = instruction.split()
        command = parts[0]

        if command == "PUSH_A":
            value = float(parts[1])
            self.push_a(value)
        elif command == "PUSH_B":
            value = float(parts[1])
            self.push_b(value)
        elif command == "MUL_A":
            self.mul_a()
        elif command == "ADD_A":
            self.add_a()
        elif command == "MUL_B":
            self.mul_b()
        elif command == "ADD_B":
            self.add_b()
        elif command == "CURSE_A":
            divisor = int(parts[1])
            self.curse_a(divisor)
        elif command == "CURSE_B":
            divisor = int(parts[1])
            self.curse_b(divisor)
        elif command == "BLESS_A":
            blessing = int(parts[1])
            self.bless_a(blessing)
        elif command == "BLESS_B":
            blessing = int(parts[1])
            self.bless_b(blessing)
        elif command == "COMPARE":
            self.compare()
        elif command == "END":
            print("End of the program.")

    def run(self, program):
        for instruction in program:
            self.execute_instruction(instruction)

def menu():
    while True:
        print("\nMenu:")
        print("1. Establish fighters")
        print("2. Curse fighter")
        print("3. Bless fighter")
        print("4. View fighters' power")
        print("5. Fight")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == "1":
            generar_fighters()
        elif choice == "2":
            if existe_programa():
                curse_fighter()
            else:
                print("No fighters assigned.")
        elif choice == "3":
            if existe_programa():
                bless_fighter()
            else:
                print("No fighters assigned.")
        elif choice == "4":
            if existe_programa():
                peek()
            else:
                print("No fighters assigned.")
        elif choice == "5":
            if existe_programa():
                fight()
            else:
                print("No fighters assigned.")
        elif choice == "6":
            eliminar_programa()
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

def generar_fighters():
    # Ejecutar el generador de archivo
    subprocess.run(['python', 'generador.py'])
    print("Fighters established.")

def peek():
    # Cargar y ejecutar el programa
    vm = StackBasedVM()
    program = cargar_programa("programa.fight")
    vm.run(program)  # Ejecutar para actualizar las pilas
    # Ahora podemos acceder a los poderes
    if vm.stack_a and vm.stack_b:
        # Recuperar solo los poderes originales
        power_a = vm.pull_a()  # Poder de A
        power_b = vm.pull_b()  # Poder de B
        print(f"Fighter A's power: {power_a}")
        print(f"Fighter B's power: {power_b}")
    else:
        print("No fighters assigned or their powers are not set.")

def curse_fighter():
    # Lógica para maldecir un combatiente
    fighter = input("Which fighter to curse? (A/B): ").strip().upper()
    if fighter in ['A', 'B']:
        divisor = random.randint(1, 10)  # Generar número aleatorio para la maldición
        with open("programa.fight", "r") as file:
            lines = file.readlines()
        # Añadir la instrucción de maldición antes del END
        curse_instruction = f"CURSE_{fighter} {divisor}\n"
        lines.insert(-1, curse_instruction)  # Insertar antes del END
        with open("programa.fight", "w") as file:
            file.writelines(lines)
        print(f"Fighter {fighter} cursed with divisor {divisor}.")
    else:
        print("Invalid fighter. Choose A or B.")

def bless_fighter():
    # Lógica para bendecir un combatiente
    fighter = input("Which fighter to bless? (A/B): ").strip().upper()
    if fighter in ['A', 'B']:
        blessing = random.randint(0, 10)  # Generar número aleatorio para la bendición
        with open("programa.fight", "r") as file:
            lines = file.readlines()
        # Añadir la instrucción de bendición antes del END
        bless_instruction = f"BLESS_{fighter} {blessing}\n"
        lines.insert(-1, bless_instruction)  # Insertar antes del END
        with open("programa.fight", "w") as file:
            file.writelines(lines)
        print(f"Fighter {fighter} blessed with {blessing} additional power.")
    else:
        print("Invalid fighter. Choose A or B.")

def fight():
    # Ejecutar la comparación de los combatientes
    vm = StackBasedVM()
    program = cargar_programa("programa.fight")
    # Añadir la comparación antes del END
    program.insert(-1, "COMPARE ; compare results\n")
    vm.run(program)  # Ejecutar para calcular resultados

def cargar_programa(filename):
    with open(filename, "r") as file:
        return file.readlines()

def existe_programa():
    return os.path.exists("programa.fight")

def eliminar_programa():
    if existe_programa():
        os.remove("programa.fight")
        print("Program file deleted.")

if __name__ == "__main__":
    menu()