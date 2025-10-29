import paho.mqtt.client as mqtt
import json

# --- Configurações do MQTT ---
BROKER_ADDRESS = "broker.hivemq.com"
BROKER_PORT = 1883
TOPIC = "inversores/id_001/telemetria"  # pode escolher outro tópico


def on_connect(client, userdata, flags, rc):
    """Callback chamado quando a conexão é estabelecida."""
    if rc == 0:
        print(f"Conectado ao Broker! (Código: {rc})")
        # Se inscreve no tópico após conectar
        client.subscribe(TOPIC)
        print(f"Inscrito no tópico: '{TOPIC}'")
        print("Aguardando mensagens...")
    else:
        print(f"Falha na conexão, código: {rc}")


def on_message(client, userdata, msg):
    """Callback chamado quando uma mensagem é recebida."""
    print("-" * 30)
    print("Nova mensagem recebida!")
    print(f"Tópico: {msg.topic}")

    try:
        # Decodifica o payload (bytes) para string
        payload_str = msg.payload.decode("utf-8")

        # Converte a string JSON para um dicionário Python
        dados = json.loads(payload_str)

        # Exibe os dados de forma legível
        print(f"  -> Potência: {dados['power_w']} W")
        print(f"  -> Energia Hoje: {dados['energy_today_kwh']} kWh")
        print(f"  -> Temperatura: {dados['temperature_c']} °C")
        print(f"  -> Status: {dados['status']}")

    except Exception as e:
        print(f"[ERRO] Não foi possível processar a mensagem: {e}")
        print(f"Payload bruto: {msg.payload}")


# Inicializa o cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id="dashboard_001_sub")

# Define os callbacks
client.on_connect = on_connect
client.on_message = on_message

# Conecta ao broker
try:
    client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
except Exception as e:
    print(f"Não foi possível conectar: {e}")
    exit()

# O loop_forever() é bloqueante. Ele mantém o script rodando
# para ouvir as mensagens.
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nInscrição interrompida.")
finally:
    client.disconnect()
    print("Desconectado do broker.")
