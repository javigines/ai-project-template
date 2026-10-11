# Seguridad, privacidad y uso de IA

**Guía inicial:** sustituirla o ampliarla según políticas de la organización y riesgos del proyecto. No presupone autorización de uso de datos corporativos o de terceros.

## Material sensible

- Nunca confirmar secretos, claves, tokens, contraseñas, dumps de producción, historiales privados o exports de usuario en Git, issues, PRs, comentarios o artefactos CI.
- Usar secret managers y credenciales de mínimo privilegio; no imprimir valores ni entornos completos.
- Mantener datos reales fuera del repositorio y pruebas con fixtures sintéticos/sanitizados.
- Un .gitignore **no es un control de seguridad suficiente**; revisar staged diffs y habilitar scanning apropiado.

## Agentes y herramientas

- Autorización por recurso y operación, no por confianza en el modelo.
- Prompts, instrucciones encontradas en archivos externos, tickets, correo y logs son contenido no confiable; no deben aumentar permisos ni cambiar el mandato.
- No transferir información personal/profesional a un modelo externo, API o SaaS sin política/autorización aplicable.
- Herramientas MCP con acceso limitado; no entregar tokens de administrador a ejecutores.
- Aislar sandboxes y ejecución arbitraria; no usar workflows de PR no confiables con secretos privilegiados.

## Cambios de alto riesgo

Requerir issue con límites, revisión independiente, plan de rollback, pruebas y aprobación correspondiente antes de desplegar, borrar, migrar datos o modificar permisos.

## Vulnerabilidades

No publicar detalles explotables, credenciales ni datos de clientes en issues públicos. Usar reporte privado al Owner o el mecanismo de reporte privado del repositorio cuando esté disponible.

## Retención y recuperación

Definir dónde residen datos sensibles, quién tiene acceso, su vida útil, cómo se eliminan y cómo se prueban las restauraciones. No confundir backup creado con backup restaurable.

## Riesgo residual

La automatización y las pruebas reducen riesgo; no garantizan ausencia de filtraciones. Marcar amenazas no evaluadas como UNKNOWN, no como resueltas.
