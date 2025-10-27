# Exemplo de Comunicação MQTT com Python

Este projeto demonstra um sistema simples de publicação e recebimento de mensagens MQTT usando a biblioteca `paho-mqtt` em Python. O cenário simula um inversor de energia solar enviando dados de telemetria para um broker MQTT, e um script "assinante" que recebe e exibe esses dados.

## Funcionalidades

- **`publisher.py`**:
  - Conecta-se a um broker MQTT público (`broker.hivemq.com`).
  - Simula dados de telemetria de um inversor (potência, energia gerada, temperatura).
  - Publica os dados em formato JSON no tópico `inversores/id_001/telemetria` a cada 5 segundos.

- **`subscriber.py`**:
  - Conecta-se ao mesmo broker MQTT.
  - Inscreve-se no tópico `inversores/id_001/telemetria`.
  - Aguarda por mensagens, e quando uma é recebida, decodifica o JSON e exibe os dados de forma legível no console.

## Pré-requisitos

- Python 3.x
- A biblioteca `paho-mqtt`

## Instalação

1. **Clone o repositório (ou baixe os arquivos):**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_DIRETORIO>
   ```

2. **Instale a biblioteca `paho-mqtt`:**
   É recomendado o uso de um ambiente virtual (`venv`) para isolar as dependências.
   ```bash
   # Crie um ambiente virtual (opcional, mas recomendado)
   python -m venv venv
   # Ative o ambiente virtual
   # No Windows:
   # venv\Scripts\activate
   # No macOS/Linux:
   # source venv/bin/activate

   # Instale a dependência
   pip install paho-mqtt
   ```

## Como Usar

Para ver o sistema em ação, você precisará executar os dois scripts (`publisher.py` e `subscriber.py`) simultaneamente, em dois terminais separados.

1. **Abra o primeiro terminal e execute o `subscriber.py`:**
   Este script ficará aguardando por mensagens.
   ```bash
   python subscriber.py
   ```
   Você verá uma mensagem indicando que ele está conectado e aguardando.

2. **Abra um segundo terminal e execute o `publisher.py`:**
   Este script começará a enviar dados imediatamente.
   ```bash
   python publisher.py
   ```

3. **Observe a saída:**
   - No terminal do **publisher**, você verá as mensagens JSON que estão sendo enviadas.
   - No terminal do **subscriber**, você verá os dados recebidos, formatados de maneira legível.

## Formato dos Dados

A mensagem enviada pelo publisher é uma string no formato JSON com a seguinte estrutura:

```json
{
  "power_w": 3500.00,
  "energy_today_kwh": 10.1,
  "temperature_c": 45.5,
  "status": "Gerando"
}
```

- `power_w`: Potência instantânea em Watts.
- `energy_today_kwh`: Energia total gerada no dia em quilowatt-hora.
- `temperature_c`: Temperatura do equipamento em graus Celsius.
- `status`: Status operacional do inversor.
