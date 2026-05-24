# Arquitetura do Sistema — EcoMonitor Home

## Visão Geral

O EcoMonitor Home é composto por três camadas principais:

1. **Camada de campo (hardware):** ESP32 com sensores físicos
2. **Camada de processamento (servidor local):** stack de software no Ubuntu Server
3. **Camada de acesso (internet):** Cloudflare Tunnel + Grafana

---

## Diagrama de Fluxo de Dados

```
[PZEM-004T]──┐
             ├──[ESP32 #1 - Energia]──┐
             │                        │  MQTT (Wi-Fi)
[YF-S201]───┐│                        ▼
            ├┼──[ESP32 #2 - Água]──[Mosquitto Broker]
[JSN-SR04T]─┘│                        │
             │                        ▼
             │                    [Node-RED]
             │                        │
             │              ┌─────────┴──────────┐
             │              ▼                    ▼
             │          [InfluxDB]          [Telegram Bot]
             │              │                (alertas)
             │              ▼
             │          [Grafana]
             │              │
             │           [Nginx]
             │              │
             │    [Cloudflare Tunnel]
             │              │
             └──────[Navegador/Celular]
```

---

## Componentes de Software

### Mosquitto MQTT Broker
- **Função:** Recebe mensagens dos ESP32 e distribui para os subscritos
- **Protocolo:** MQTT v3.1.1
- **Porta:** 1883 (local), 8883 (TLS, futuro)
- **Tópicos:**
  - `ecomonitor/energia/tensao`
  - `ecomonitor/energia/corrente`
  - `ecomonitor/energia/potencia`
  - `ecomonitor/energia/kwh`
  - `ecomonitor/agua/vazao`
  - `ecomonitor/agua/volume`
  - `ecomonitor/agua/nivel_caixa`

### Node-RED
- **Função:** Subscreve os tópicos MQTT, processa dados, aplica regras e salva no InfluxDB
- **Porta:** 1880
- **Responsabilidades:**
  - Cálculo de custo em R$ (energia e água)
  - Projeção de consumo mensal
  - Detecção de anomalias
  - Envio de alertas via Telegram

### InfluxDB v2
- **Função:** Armazenamento de séries temporais
- **Porta:** 8086
- **Buckets:**
  - `energia` — dados de tensão, corrente, potência e kWh
  - `agua` — dados de vazão, volume e nível

### Grafana
- **Função:** Visualização e BI
- **Porta:** 3000
- **Dashboards:**
  - Energia Elétrica (tempo real + histórico)
  - Consumo de Água (tempo real + histórico)
  - Visão Geral (resumo + custos + metas)

### Nginx
- **Função:** Reverse proxy — expõe o Grafana na porta 80/443
- **Configuração:** Redireciona `localhost:80` → `localhost:3000`

### Cloudflare Tunnel
- **Função:** Exposição segura do servidor local para a internet
- **Acesso:** `https://ecomonitor.seudominio.com.br`
- **Segurança:** Cloudflare Access (autenticação por e-mail antes do Grafana)

---

## Frequência de Coleta de Dados

| Sensor | Intervalo | Justificativa |
|---|---|---|
| PZEM-004T (energia) | 10 segundos | Variação rápida de carga |
| YF-S201 (fluxo) | 5 segundos | Detectar início/fim de uso |
| JSN-SR04T (nível) | 60 segundos | Variação lenta |

---

## Segurança

- Mosquitto configurado com autenticação (usuário/senha)
- Grafana com autenticação obrigatória
- Cloudflare Access como camada extra de autenticação
- Nginx com headers de segurança HTTP
- Firewall UFW: apenas portas necessárias abertas
