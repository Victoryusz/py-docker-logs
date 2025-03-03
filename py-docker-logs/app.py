import time

def main():
    count = 0
    while True:
        print(f"Contador: {count}")
        count += 1
        time.sleep(1)
if __name__ == "__main__":
    main()
    
# Este código cria um contador simples que imprime o valor na tela a cada SEGUNDO.