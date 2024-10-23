import wave
import numpy as np
import os

class VirtualMachine:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise Exception("La pila está vacía.")
        return self.stack.pop()

    def add(self):
        if len(self.stack) < 2:
            raise Exception("No hay suficientes elementos en la pila.")
        self.stack.append(self.stack.pop() + self.stack.pop())

    def sub(self):
        if len(self.stack) < 2:
            raise Exception("No hay suficientes elementos en la pila.")
        self.stack.append(self.stack.pop() - self.stack.pop())

    def mul(self):
        if len(self.stack) < 2:
            raise Exception("No hay suficientes elementos en la pila.")
        self.stack.append(self.stack.pop() * self.stack.pop())

    def div(self):
        if len(self.stack) < 2:
            raise Exception("No hay suficientes elementos en la pila.")
        divisor = self.stack.pop()
        if divisor == 0:
            raise Exception("División por cero.")
        self.stack.append(self.stack.pop() / divisor)

    def execute(self, operation):
        tokens = operation.split()
        command = tokens[0].upper()

        if command == "PUSH":
            value = int(tokens[1])
            self.push(value)
            return value
        elif command == "POP":
            return self.pop()
        elif command == "ADD":
            self.add()
            return self.stack[-1]
        elif command == "SUB":
            self.sub()
            return self.stack[-1]
        elif command == "MUL":
            self.mul()
            return self.stack[-1]
        elif command == "DIV":
            self.div()
            return self.stack[-1]
        else:
            raise Exception("Comando no reconocido.")

    def execute_from_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line: 
                    self.execute(line)
        if not self.stack:
            raise Exception("No se pudo obtener un resultado de la pila.")
        return self.stack[-1]  

    def create_audio(self, result, file_path):  
        if result <= 0:
            raise ValueError("Total bars must be greater than zero.")

        sample_rate = 44100
        duration_per_bar = 2.0 
        total_bars = result

        audio = np.zeros(int(sample_rate * duration_per_bar * total_bars))

        kick_sample = self.load_wave_file("samples/kick.wav")
        kick_length = kick_sample.shape[0]
        
        hat_sample = self.load_wave_file("samples/hat.wav")
        hat_length = hat_sample.shape[0]
        
        cymbal_sample = self.load_wave_file("samples/cymbal.wav")
        cymbal_length = cymbal_sample.shape[0]

        # Sonido en los tiempos 1, 2, 3, 4 de cada compás
        for i in range(total_bars):
            start_sample = int(i * sample_rate * duration_per_bar)

            end_idx = start_sample + kick_length
            if end_idx <= len(audio):
                audio[start_sample:end_idx] += kick_sample
            
            end_idx = start_sample + int(sample_rate * 1) + kick_length
            if end_idx <= len(audio):
                audio[start_sample + int(sample_rate * 1):end_idx] += kick_sample

            # Hats si el resultado está entre 10 y 29
            if 10 <= result < 30:
                hats_times = [0.25, 0.75, 1.25, 1.75]
                for hat_time in hats_times:
                    end_idx = start_sample + int(sample_rate * hat_time) + hat_length
                    if end_idx <= len(audio):
                        audio[start_sample + int(sample_rate * hat_time):end_idx] += hat_sample

            # Cymbals si el resultado está entre 20 y 29
            if 20 <= result < 30:
                cymbal_times = [0.5, 1.5]
                for cymbal_time in cymbal_times:
                    end_idx = start_sample + int(sample_rate * cymbal_time) + cymbal_length
                    if end_idx <= len(audio):
                        audio[start_sample + int(sample_rate * cymbal_time):end_idx] += cymbal_sample

            # Guardar el archivo WAV
            with wave.open(file_path, 'wb') as wf:
                wf.setnchannels(1)  
                wf.setsampwidth(2) 
                wf.setframerate(sample_rate)
                wf.writeframes((audio * 32767).astype(np.int16)) 


    def load_wave_file(self, file_path):
        with wave.open(file_path, 'rb') as wf:
            n_channels = wf.getnchannels()
            sample_width = wf.getsampwidth()
            framerate = wf.getframerate()
            n_frames = wf.getnframes()
            raw_data = wf.readframes(n_frames)
            audio_data = np.frombuffer(raw_data, dtype=np.int16)
            if n_channels > 1:
                audio_data = audio_data[::n_channels]  
            return audio_data / 32767.0 
