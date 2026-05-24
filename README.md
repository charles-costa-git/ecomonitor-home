# 🏠 EcoMonitor Home

> Sistema de monitoramento em tempo real de **energia elétrica** e **consumo de água** residencial, baseado em IoT com ESP32, stack open source e acesso remoto via Cloudflare Tunnel.

---

## 📋 Sobre o Projeto

O EcoMonitor Home é um projeto pessoal de IoT desenvolvido com o objetivo de monitorar, registrar e analisar o consumo de energia elétrica e água de uma residência, fornecendo dashboards em tempo real acessíveis de qualquer lugar do mundo.

O projeto integra hardware embarcado (ESP32) com uma stack de software profissional rodando em Ubuntu Server local, exposta com segurança via Cloudflare Tunnel.

---

## 🎯 Objetivos

- Monitorar em tempo real o consumo de energia elétrica (tensão, corrente, potência, kWh)
- Monitorar em tempo real o consumo de água (vazão, volume acumulado, nível da caixa d'água)
- Calcular e projetar custos mensais de energia e água
- Detectar anomalias como possíveis vazamentos ou consumo fora do padrão
- Enviar alertas via Telegram
- Disponibilizar dashboards acessíveis remotamente via navegador

---

## 🏗️ Arquitetura do Sistema

```
[Sensores Físicos]
      │
   [ESP32]  ←── coleta e envia dados via Wi-Fi
      │
   [Mosquitto MQTT Broker]  ←── mensageria (Ubuntu Server local)
      │
   [Node-RED]  ←── orquestração, regras e alertas
      │
   [InfluxDB]  ←── banco de dados de séries temporais
      │
   [Grafana]  ←── dashboards e visualização
      │
   [Nginx]  ←── reverse proxy
      │
   [Cloudflare Tunnel]  ←── acesso seguro externo
      │
   [Navegador / Celular]  ←── você em qualquer lugar
```

---

## 🔧 Hardware Utilizado

| Componente | Função |
|---|---|
| ESP32 DevKit v1 (x2) | Microcontrolador principal |
| PZEM-004T v3.0 | Medição de energia elétrica |
| YF-S201 | Sensor de fluxo de água |
| JSN-SR04T | Sensor ultrassônico de nível (caixa d'água) |
| Fonte 5V/2A (x2) | Alimentação dos ESP32 |

---

## 💻 Stack de Software

| Camada | Tecnologia |
|---|---|
| Sistema Operacional | Ubuntu Server (com interface gráfica) |
| Microcontrolador | Arduino IDE (C++) |
| Mensageria | Mosquitto MQTT |
| Orquestração | Node-RED |
| Banco de Dados | InfluxDB v2 |
| Dashboards / BI | Grafana |
| Servidor Web | Nginx |
| Acesso Externo | Cloudflare Tunnel |
| Scripts | Python 3 |
| Versionamento | Git / GitHub |

---

## 🗺️ Roadmap

- [x] Fase 0 — Concepção e estrutura do projeto
- [ ] Fase 1 — Ambiente Linux e infraestrutura base
- [ ] Fase 2 — Firmware ESP32 (Energia Elétrica)
- [ ] Fase 3 — Firmware ESP32 (Água)
- [ ] Fase 4 — Node-RED: orquestração e regras
- [ ] Fase 5 — InfluxDB: modelagem e consultas
- [ ] Fase 6 — Grafana: dashboards e BI
- [ ] Fase 7 — Acesso externo via Cloudflare Tunnel
- [ ] Fase 8 — Documentação final e portfólio

---

## 📁 Estrutura do Repositório

```
ecomonitor-home/
│
├── README.md
├── CHANGELOG.md
├── LICENSE
│
├── docs/
│   ├── arquitetura.md
│   ├── lista-de-materiais.md
│   ├── diagramas/
│   └── prints/
│
├── firmware/
│   ├── energia/
│   └── agua/
│
├── nodered/
├── influxdb/
├── grafana/
│
├── scripts/
│   ├── simulador.py
│   └── backup.py
│
└── infra/
    ├── mosquitto.conf
    ├── nginx.conf
    └── cloudflared/
```

---

## 🚀 Como Executar (em construção)

A documentação de instalação e execução será publicada ao final de cada fase. Consulte a pasta `docs/` para detalhes.

---

## 👤 Autor

**Charles Costa**
Engenheiro Eletricista | Estudante de Bacharelado em TI (UNIVESP) | Entusiasta de IoT e Industry 4.0

[![GitHub](https://img.shields.io/badge/GitHub-charles--costa--git-181717?logo=github)](https://github.com/charles-costa-git)

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
