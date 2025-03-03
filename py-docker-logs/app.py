import time 
import random

def main():
    count = 0
    log_levels = ["INFO", "DEBUG", "ERROR","PERIGO"]
    
    with open("app.log", "a") as log_file:
        while True:
            # Escolhendo um nível de log aleatório
            log_level = random.choice(log_levels)
            
            # Msg fictícias para logs
            log_message = f"[{log_level}] - Contador: {count} - Log Gerado em: {time.strftime('%Y-%m-%d %H:%M:%S')}\n" 

            # mostra os logs no console e escreve no arquivo
            print(log_message, end='') # mostra no console
            log_file.write(log_message) # escreve no arquivo
            
            count += 1
            time.sleep(1)
if __name__ == "__main__":
    main()