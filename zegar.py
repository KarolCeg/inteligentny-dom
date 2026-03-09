import time
import sys

def simulate_clock():
    # Początkowy stan zegara
    hours = 0
    minutes = 0
    seconds = 0

    # 1 symulowana sekunda = 0.001 rzeczywistej sekundy(1000 razy)
    speed_multiplier = 1000
    sleep_duration = 1.0 / speed_multiplier

    print("Rozpoczynam symulację zegara 24h. Naciśnij Ctrl+C, aby zatrzymać.\n")

    try: #sprawia ze jedynie ctrl + c moze przerwac program
        while True:
            # Formatowanie czasu do postaci HH:MM:SS
            # Znak '\r' na początku powoduje powrót karetki - zegar odświeża się w tej samej linijce
            time_display = f"\r{hours:02d}:{minutes:02d}:{seconds:02d}"
            
            # Wypisujemy czas na ekran (bez przejścia do nowej linii)
            sys.stdout.write(time_display)
            sys.stdout.flush()

            # Usypiamy program na 0.01 sekundy, co symuluje upływ czasu w przyspieszeniu
            time.sleep(sleep_duration)

            # Logika upływu czasu
            seconds += 1
            if seconds == 60:
                seconds = 0
                minutes += 1
                if minutes == 60:
                    minutes = 0
                    hours += 1
                    if hours == 24:
                        hours = 0

    except KeyboardInterrupt:
        print("\nSymulacja zatrzymana przez użytkownika.")

if __name__ == "__main__":
    simulate_clock()