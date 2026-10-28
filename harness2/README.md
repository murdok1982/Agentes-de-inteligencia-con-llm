# ⚡ Google Harness² - Configuración Auto-Optimizable (SDD + 8 Componentes)

Configuración completa basada en la arquitectura recursiva **Google Harness² (`google-research/harness2`)**. A diferencia de un agente tradicional, Harness² mejora automáticamente sus propios prompts, skills y scripts de extracción en cada misión (*Propose – Probe – Compose*) y guarda lo aprendido en `harness/3_memory/EXPERIENCE.md`.

## 🚀 Cómo arrancarlo paso a paso

### 1. Instalar `uv` y preparar el entorno
```bash
cd google-harness2
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install playwright telethon pydantic python-dotenv httpx exifread youtube-transcript-api
playwright install chromium
```

### 2. Configurar el archivo `.env`
```bash
cp .env.example .env
nano .env
```

### 3. Capturar tus sesiones de redes sociales (Una sola vez)
```bash
mkdir -p sessions
playwright codegen --save-storage=./sessions/ig_state.json https://www.instagram.com
playwright codegen --save-storage=./sessions/fb_state.json https://www.facebook.com
playwright codegen --save-storage=./sessions/x_state.json https://x.com
playwright codegen --save-storage=./sessions/yt_state.json https://www.youtube.com
```

### 4. Lanzar en Docker 24/7
```bash
docker compose up -d --build
```
