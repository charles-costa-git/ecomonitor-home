"""
EcoMonitor Home — Backup do InfluxDB
Realiza backup dos buckets do InfluxDB para uma pasta local.
Recomendado: agendar via cron para execução diária.

Cron exemplo (todo dia às 2h da manhã):
    0 2 * * * /usr/bin/python3 /caminho/para/backup.py

Uso:
    python backup.py
"""

import os
import subprocess
from datetime import datetime

# ─── Configurações ────────────────────────────────────────────
INFLUX_BIN    = "/usr/bin/influx"          # caminho do binário influx CLI
BACKUP_DIR    = os.path.expanduser("~/ecomonitor-backups")
RETENTION_DAYS = 30                        # manter backups dos últimos N dias

def executar_backup():
    data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M")
    destino   = os.path.join(BACKUP_DIR, f"backup_{data_hora}")
    os.makedirs(destino, exist_ok=True)

    print(f"📦 Iniciando backup em: {destino}")

    cmd = [INFLUX_BIN, "backup", destino]
    resultado = subprocess.run(cmd, capture_output=True, text=True)

    if resultado.returncode == 0:
        print(f"✅ Backup concluído com sucesso.")
    else:
        print(f"❌ Erro no backup:\n{resultado.stderr}")

def limpar_backups_antigos():
    """Remove backups com mais de RETENTION_DAYS dias."""
    import time
    agora = time.time()
    limite = agora - (RETENTION_DAYS * 86400)

    for entry in os.scandir(BACKUP_DIR):
        if entry.is_dir() and entry.stat().st_mtime < limite:
            import shutil
            shutil.rmtree(entry.path)
            print(f"🗑️  Backup antigo removido: {entry.name}")

if __name__ == "__main__":
    os.makedirs(BACKUP_DIR, exist_ok=True)
    executar_backup()
    limpar_backups_antigos()
