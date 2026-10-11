# Contribuir

Este proyecto usa GitHub como fuente de verdad y un flujo de cambios basado en issues y PRs.

**Antes de cambiar código:** lee [el Charter](docs/PROJECT_CHARTER.md), [las normas de trabajo](docs/WORKFLOW.md), [los gates](docs/QUALITY_GATES.md) y [la política de seguridad](docs/SECURITY.md).

- Cambios sustanciales deben estar vinculados a un issue.
- No hagas push directo a la rama principal después del bootstrap, salvo excepción explícita del Owner.
- Ejecuta pruebas relevantes **solo para código ejecutable y su comportamiento**. Los cambios solo de documentación tienen `tests: N/A`; no validar Markdown, enlaces, estructura o contenido de documentos mediante tests automáticos.
- Si cambia una decisión arquitectónica, crea o actualiza un ADR.
- Tras el merge, elimina la rama de trabajo no utilizada.
- Reporta limitaciones como UNKNOWN/HOLD; nunca como PASS.

Los agentes deben seguir también [AGENTS.md](AGENTS.md).
