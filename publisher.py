import paho.mqtt.client as mqtt
import json
import time
import random

# --- Configurações do MQTT ---
BROKER_ADDRESS = "broker.hivemq.com"
BROKER_PORT = 1883
TOPIC = "inversores/id_001/telemetria"  # pode escolher outro tópico

print(f"Conectando ao Broker: {BROKER_ADDRESS}...")

# Inicializa o cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id="inversor_001_pub")

try:
    client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
except Exception as e:
    print(f"Não foi possível conectar: {e}")
    exit()

# Inicia o loop de rede em segundo plano
client.loop_start()

print("Conectado! Iniciando publicação...")

# Dados base do inversor
power = 3500.0
energy = 10.0

try:
    while True:
        # 1. Simula uma pequena variação nos dados
        power += random.uniform(-50.0, 50.0)
        energy += 0.1  # Incremento de energia
        temp = 45.0 + random.uniform(-1.0, 1.0)

        # 2. Monta o payload (a mensagem)
        payload_dict = {
            "power_w": round(power, 2),
            "energy_today_kwh": round(energy, 2),
            "temperature_c": round(temp, 1),
            "status": "Gerando",
        }

        # 3. Converte o dicionário para uma string JSON
        json_payload = json.dumps(payload_dict)

        # 4. Publica a mensagem no tópico
        result = client.publish(TOPIC, json_payload)

        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"Publicado: {json_payload}")
        else:
            print(f"Falha ao publicar, código: {result.rc}")

        # Espera 5 segundos
        time.sleep(5)

except KeyboardInterrupt:
    print("\nPublicação interrompida.")
finally:
    client.loop_stop()
    client.disconnect()
    print("Desconectado do broker.")
