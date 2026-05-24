"""
EcoMonitor Home — Simulador de Dados
Simula leituras dos sensores de energia e água via MQTT,
permitindo testar toda a stack sem o hardware físico.

Uso:
    pip install paho-mqtt
    python simulador.py
"""

import time
import random
import json
import paho.mqtt.client as mqtt

# ─── Configurações ────────────────────────────────────────────
BROKER_HOST = "localhost"
BROKER_PORT = 1883
BROKER_USER = ""       # preencher se o Mosquitto tiver autenticação
BROKER_PASS = ""

INTERVALO_ENERGIA = 10   # segundos
INTERVALO_AGUA    = 5    # segundos

# ─── Tópicos MQTT ─────────────────────────────────────────────
TOPICO_ENERGIA = "ecomonitor/energia"
TOPICO_AGUA    = "ecomonitor/agua"

# ─── Acumuladores ─────────────────────────────────────────────
kwh_acumulado    = 0.0
litros_acumulado = 0.0


def simular_energia():
    """Gera leituras simuladas de energia elétrica."""
    global kwh_acumulado
    tensao   = round(random.uniform(215.0, 225.0), 1)
    corrente = round(random.uniform(1.0, 8.0), 2)
    potencia = round(tensao * corrente * random.uniform(0.85, 0.95), 1)
    kwh_acumulado += potencia / 3600 / 1000 * INTERVALO_ENERGIA
    return {
        "tensao_v":   tensao,
        "corrente_a": corrente,
        "potencia_w": potencia,
        "kwh":        round(kwh_acumulado, 4),
        "fator_pot":  round(random.uniform(0.85, 0.98), 2),
    }


def simular_agua():
    """Gera leituras simuladas de consumo de água."""
    global litros_acumulado
    em_uso = random.random() > 0.6   # 40% do tempo com água correndo
    vazao  = round(random.uniform(3.0, 12.0), 2) if em_uso else 0.0
    litros_acumulado += vazao / 60 * INTERVALO_AGUA
    nivel_caixa = round(random.uniform(60.0, 95.0), 1)
    return {
        "vazao_lpm":        vazao,
        "volume_total_l":   round(litros_acumulado, 2),
        "nivel_caixa_pct":  nivel_caixa,
    }


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado ao broker MQTT")
    else:
        print(f"❌ Falha na conexão. Código: {rc}")


def main():
    client = mqtt.Client()
    if BROKER_USER:
        client.username_pw_set(BROKER_USER, BROKER_PASS)
    client.on_connect = on_connect
    client.connect(BROKER_HOST, BROKER_PORT, 60)
    client.loop_start()

    print("🚀 Simulador EcoMonitor iniciado. Pressione Ctrl+C para parar.\n")

    contador_energia = 0
    contador_agua    = 0

    while True:
        now = time.time()

        if contador_energia == 0 or (now - contador_energia) >= INTERVALO_ENERGIA:
            dados = simular_energia()
            payload = json.dumps(dados)
            client.publish(TOPICO_ENERGIA, payload)
            print(f"⚡ Energia → {payload}")
            contador_energia = now

        if contador_agua == 0 or (now - contador_agua) >= INTERVALO_AGUA:
            dados = simular_agua()
            payload = json.dumps(dados)
            client.publish(TOPICO_AGUA, payload)
            print(f"💧 Água    → {payload}")
            contador_agua = now

        time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Simulador encerrado.")
