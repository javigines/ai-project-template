# AI Project Template

Plantilla reutilizable de **gobernanza, ingeniería y colaboración con agentes de IA** para nuevos proyectos en GitHub.

> Este repositorio es una plantilla, no un proyecto productivo. Antes de empezar a desarrollar un nuevo proyecto, personaliza el [Project Charter](docs/PROJECT_CHARTER.md) y crea sus primeros issues. **No copies historiales, secretos ni datos reales a la plantilla.**

## Qué proporciona

- **GitHub como sistema de registro:** Issues = trabajo; PRs = cambios y evidencias; ADRs = decisiones duraderas.
- **Coordinación escalable:** Owner / Coordinator / Iteration Manager opcional / ejecutores Codex u otros agentes.
- **Ciclo verificable:** problema → alcance → ejecución → pruebas → revisión → merge → borrado de rama.
- **Seguridad por defecto:** permisos mínimos, clasificación de datos, fuentes no confiables y operaciones sensibles sujetas a gates.
- **Entornos productivos protegidos:** toda prueba en un servidor en uso debe ser no disruptiva, aislada y dejarlo sin restos de recursos temporales, con limpieza verificada.
- **Imágenes Docker privadas:** publicación exclusivamente en **GitHub Container Registry (GHCR, `ghcr.io`)**, con visibilidad PRIVATE del paquete comprobada; nunca Docker Hub o un registro público por defecto.
- **Continuidad:** cada agente nuevo puede reconstruir el contexto leyendo los archivos y el estado actual de GitHub, sin depender de una conversación antigua.
- **Complejidad proporcional:** proyecto pequeño = issue + PR; proyecto grande = charter, iteraciones y mandatos.

## Cómo crear un proyecto nuevo

1. En GitHub, selecciona **Use this template → Create a new repository** (si no aparece, el Owner debe activar **Settings → General → Template repository** en este repositorio).
2. Configura GitHub en el repositorio nuevo: **Issues** habilitados, **Automatically delete head branches**, método de merge y protecciones de la rama principal según su riesgo.
3. Sustituye el título de este README por el proyecto real; elimina las explicaciones de la plantilla que no apliquen.
4. Completa [PROJECT_CHARTER](docs/PROJECT_CHARTER.md) con propósito, alcance, criterios de cierre, seguridad y límites de autonomía.
5. Revisa [GOVERNANCE](docs/GOVERNANCE.md), [WORKFLOW](docs/WORKFLOW.md) y [QUALITY_GATES](docs/QUALITY_GATES.md). Mantén los principios, ajusta los parámetros al proyecto.
6. Completa [ARCHITECTURE](docs/ARCHITECTURE.md) y [ROADMAP](docs/ROADMAP.md) con lo conocido; deja **UNKNOWN** donde falte evidencia.
7. Abre los issues iniciales (los issues del repositorio plantilla **no se copian** al generar un repositorio nuevo). Cada trabajo debe tener un responsable y aceptación verificable.
8. Entrega a los agentes [AGENTS.md](AGENTS.md) y un issue concreto; evita delegaciones vagas.

## Documentación

| Recurso | Para qué sirve |
|---|---|
| [AGENTS.md](AGENTS.md) | Instrucciones persistentes para agentes de programación |
| [Project Charter](docs/PROJECT_CHARTER.md) | Misión, límites y definición de éxito |
| [Governance](docs/GOVERNANCE.md) | Roles, autoridad, escalado y fuentes de verdad |
| [Workflow](docs/WORKFLOW.md) | Trabajo con issues, ramas, PRs y cierre |
| [Quality Gates](docs/QUALITY_GATES.md) | Riesgo, pruebas, review y PASS/HOLD/UNKNOWN |
| [Security](docs/SECURITY.md) | Reglas de secretos, IA, herramientas y datos |
| [Architecture](docs/ARCHITECTURE.md) | Diseño propuesto / vigente y dependencias |
| [Roadmap](docs/ROADMAP.md) | Outcomes, etapas y milestones sin fechas ficticias |
| [ADR index](docs/decisions/README.md) | Decisiones registradas y alternativas |
| [Templates](docs/templates/) | Mandato de iteración, handoff y research |
| [Runbook](docs/RUNBOOK.md) | Operación, recovery y despliegue cuando aplique |

## Reglas que no deberían desaparecer de un proyecto nuevo

1. Una afirmación **PASS** necesita evidencia; **UNKNOWN** no es **PASS**.
2. No trabajar contra un scope inventado ni asumir acceso a sistemas o credenciales.
3. No guardar secretos, conversaciones privadas ni dumps en el repositorio, issues, PRs o CI.
4. Los documentos no sustituyen el estado de GitHub; contrastar información que puede caducar.
5. Tras un merge confirmado, eliminar la rama de trabajo si no tiene dependencias; conservar ramas protegidas.
6. Las automatizaciones deben reducir trabajo humano, sin ampliar implícitamente sus permisos.
7. Toda prueba en un host productivo debe preservar los servicios existentes y terminar con **CLEANUP=PASS**; nunca realizar `docker system prune` indiscriminado.
8. Toda imagen Docker publicada debe alojarse **de forma privada en GHCR**, comprobando visibilidad y permisos de acceso.
7. **Solo se prueban el código y su comportamiento.** No ejecutar tests automáticos de Markdown, enlaces, estructura o contenido de documentación; los cambios exclusivamente documentales se marcan `tests: N/A`.

**Recomendación de continuidad:** usa el Charter y los issues para transmitir el contexto; esto es una práctica de trabajo, no un test ni una condición de CI documental.
