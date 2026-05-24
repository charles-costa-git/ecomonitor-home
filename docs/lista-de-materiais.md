# Lista de Materiais — EcoMonitor Home

## Hardware

| # | Componente | Quantidade | Finalidade | Estimativa (R$) |
|---|---|---|---|---|
| 1 | ESP32 DevKit v1 | 2 | Microcontrolador (energia + água) | 40–60 un |
| 2 | PZEM-004T v3.0 | 1 | Medição de energia elétrica | 60–80 |
| 3 | Sensor de fluxo YF-S201 | 1 | Medição de vazão de água | 25–35 |
| 4 | Sensor ultrassônico JSN-SR04T | 1 | Nível da caixa d'água (impermeável) | 35–50 |
| 5 | Fonte chaveada 5V/2A | 2 | Alimentação dos ESP32 | 20 un |
| 6 | Protoboard 830 pontos | 2 | Montagem dos circuitos | 15 un |
| 7 | Kit jumpers M-M / M-F / F-F | 1 | Conexões | 20 |
| 8 | Caixa de proteção ABS | 2 | Proteção dos circuitos | 20 un |
| 9 | Cabo USB (programação ESP32) | 1 | Upload de firmware | — |
| **Total estimado** | | | | **~R$ 310–370** |

---

## Onde Comprar (Brasil)

- **Mercado Livre / Shopee:** componentes eletrônicos em geral, boa variedade de ESP32 e sensores
- **FilipeFlop** (filipeflop.com): loja especializada em eletrônica maker, boa qualidade
- **Baudaeletrônica** (baudaeletronica.com.br): boa variedade e entrega rápida
- **AliExpress:** preços menores, prazo de entrega maior (15–30 dias)

---

## Software (gratuito / open source)

| Software | Versão | Onde baixar |
|---|---|---|
| Ubuntu Server | 22.04 LTS ou 24.04 LTS | ubuntu.com |
| Arduino IDE | 2.x | arduino.cc |
| VSCode | Atual | code.visualstudio.com |
| Mosquitto | Atual | apt install mosquitto |
| Node-RED | Atual | nodered.org |
| InfluxDB | v2.x | influxdata.com |
| Grafana | Atual | grafana.com |
| Nginx | Atual | apt install nginx |
| Cloudflared | Atual | developers.cloudflare.com |
| Python | 3.x | Já incluso no Ubuntu |
| Git | Atual | Já incluso no Ubuntu |

---

## Bibliotecas Arduino (ESP32)

| Biblioteca | Finalidade |
|---|---|
| `PZEM004Tv30` | Leitura do sensor de energia PZEM-004T |
| `PubSubClient` | Cliente MQTT para ESP32 |
| `WiFi.h` | Conexão Wi-Fi (inclusa no core ESP32) |
| `NewPing` | Sensor ultrassônico JSN-SR04T |
| `ArduinoJson` | Serialização de dados em JSON para MQTT |
