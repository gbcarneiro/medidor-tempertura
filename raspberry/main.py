import network
import urequests
import dht
import machine
import time

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print("Conectando ao Wi-Fi")
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        pass
    print("Conectado ao Wi-Fi")

dht_sensor = dht.DHT11(machine.Pin(2))  

# Conecta ao Wi-Fi (substitua com suas credenciais de Wi-Fi)
connect_wifi('REDE', 'SENHA')

# Loop principal
while True:
    try:
        # Lê os dados do sensor
        dht_sensor.measure()
        temp = dht_sensor.temperature()

        data = {'temperature': temp}
        
        print(data)
        # Envia os dados via POST
        response = urequests.post('https://flask-hello-world-eight-black.vercel.app/add/temperature', json=data)
        print(response.text)

        print(data)
        time.sleep(5)

    except Exception as e:
        print("Ocorreu um erro:", e)
        time.sleep(5)
