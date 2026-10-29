# Agentes de Inteligencia con LLM

Repositorio que agrupa componentes de **agentes de inteligencia** basados en LLM y herramientas auxiliares:

- **Hermes Agent** (`hermes-agent/`): sincronización de inteligencia con GitHub (validación de contratos Pydantic y push automatizado).
- **Google Harness²** (`harness2/`): configuración auto-optimizable basada en la arquitectura recursiva `google-research/harness2`, con scripts de recolección y plugins OPSEC.

> Repositorio objetivo de datos: `murdok1982/DataBaseInt-Osint-socmint-Sigint`.

---

## Estructura del repositorio

```
.
├── README.md
├── .env.example
├── .gitignore
├── requirements.txt
├── harness2/
│   ├── README.md                          # Guía de arranque de Google Harness²
│   └── harness/
│       ├── 6_scripts/
│       │   ├── social_stealth_scraper.py  # Recolector multi-plataforma (placeholder)
│       │   └── github_db_commit.py        # Validación y commit de inteligencia
│       └── 8_plugins/
│           └── opsec_middleware.py         # Redacción de secretos en salidas
└── hermes-agent/
    └── configuracion/
        └── src/
            └── sync/
                └── github_db_sync.py      # Sincronización GitHub (validación + push)
```

## Descripción de componentes

### `hermes-agent/configuracion/src/sync/github_db_sync.py`
Clase `GithubIntelligenceSync`:
- Valida un payload JSON contra el modelo `IntelligenceContract` (Pydantic).
- Persiste el resultado en `operations/<operation_code>/intel_graph_<timestamp>.json`.
- Clona (si es necesario) el repositorio remoto usando `GITHUB_PAT`.
- Realiza `git add`, `commit` y `push` a `main`.

Variables de entorno usadas:
- `LOCAL_REPO_CLONE` (default `./data_repo_clone`)
- `TARGET_REPO` (default `murdok1982/DataBaseInt-Osint-socmint-Sigint`)
- `GITHUB_PAT`

### `harness2/harness/6_scripts/github_db_commit.py`
Versión equivalente/simplificada de la sincronización GitHub (validación + persistencia local).

### `harness2/harness/6_scripts/social_stealth_scraper.py`
Placeholder para recolección autenticada multi-plataforma (`SocialMultiPlatformCollector`).

### `harness2/harness/8_plugins/opsec_middleware.py`
Middleware de seguridad que redacta valores de variables sensibles (`OPENROUTER_API_KEY`, `HARNESS2_CODEX_API_KEY`, `TG_API_HASH`, `GITHUB_PAT`) en cualquier salida de texto, reemplazándolos por `[REDACTED_BY_OPSEC_MIDDLEWARE]`.

### `harness2/README.md`
Guía de arranque de Google Harness²: instalación de `uv`, entorno virtual, dependencias, captura de sesiones y despliegue Docker.

---

## Requisitos previos

- Python 3.12+
- `uv` (recomendado) o `pip`
- Git
- (Opcional) Docker y Docker Compose
- (Opcional) Playwright browsers (`playwright install chromium`)

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/murdok1982/Agentes-de-inteligencia-con-llm.git
cd Agentes-de-inteligencia-con-llm

# 2. Crear entorno virtual
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus valores
```

## Variables de entorno

Ver `.env.example`. **Nunca** subas el archivo `.env` al repositorio.

| Variable | Descripción |
|---|---|
| `LOCAL_REPO_CLONE` | Ruta local del clone de datos |
| `TARGET_REPO` | Repositorio remoto de datos |
| `GITHUB_PAT` | Token personal de GitHub (scopes `repo`) |
| `OPENROUTER_API_KEY` | API key de OpenRouter (Harness²) |
| `HARNESS2_CODEX_API_KEY` | API key adicional de Harness² |
| `TG_API_HASH` | Hash de API de Telegram |

## Seguridad (OPSEC)

- Los secretos se gestionan exclusivamente mediante variables de entorno.
- El middleware `opsec_middleware.py` redacta secretos en salidas/logs.
- `.env` está incluido en `.gitignore`.

## Licencia

No se ha especificado una licencia para este repositorio. Uso interno/educativo salvo indicación contraria.
---

## Agentes del proyecto OSINT Nexus

Este repositorio incluye los agentes del proyecto OSINT Nexus en las mismas rutas que el repositorio de la base de datos:

- `apps/agents/hermes/`: harness Hermes v3.1 (allowlist de tools, OPSEC fail-closed, idempotencia).
- `apps/informant-agent/`: Informante IA (pre-vuelo, extracción referenciada, cliente M2M).
- `contracts/`: contratos sellados que consumen los agentes (`extraction-schema.json`, `openapi.yaml`, `v3/hermes-tools.json`, `v3/agent-contracts.json`).
- `.opencode/agents/` y `.antigravity/`: definiciones y prompts de los agentes.

**Fuente de verdad:** el repositorio [DataBaseInt-Osint-socmint-Sigint](https://github.com/murdok1982/DataBaseInt-Osint-socmint-Sigint). Esta copia se sincroniza desde allí; no editar aquí sin llevar el cambio al repositorio de origen.

Tests: `cd apps/agents/hermes && python -m pytest -q` y `cd apps/informant-agent && python -m pytest -q`.
