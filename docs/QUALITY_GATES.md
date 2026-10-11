# Quality Gates & Definition of Done

Las afirmaciones de aceptación se sustentan en **evidencias comprobables** cuando corresponda: commit SHA, logs sanitizados, pruebas **de código**, artefactos, comprobaciones de seguridad y observación directa del sistema.

## Política de testing — solo código

- Las pruebas automatizadas deben comprobar **código ejecutable y comportamiento funcional**, como tests unitarios, integración o end-to-end.
- **No crear ni ejecutar tests de documentación**, incluyendo Markdown, enlaces, ortografía, existencia/estructura de carpetas o archivos documentales, snapshots y verificaciones del contenido escrito.
- Las PRs **exclusivamente documentales** requieren `tests: N/A`, sin CI documental ni check de documentación bloqueante. La revisión humana del cambio sigue siendo posible y no se presenta como un test.
- Si una PR incluye código y documentación, probar el código afectado; la documentación no adquiere por ello una batería de tests.
- Esta política no autoriza divulgar secretos ni omitir comprobaciones de seguridad aplicables.

## Estados

- **PASS:** requisito cumplido con evidencia reproducible.
- **FAIL:** una prueba o requisito claramente incumplido.
- **HOLD:** operación detenida por un gate, riesgo o dependencia.
- **UNKNOWN:** evidencia ausente o insuficiente; nunca se presenta como PASS.
- **N/A:** requisito realmente no aplicable con razón.

## Niveles de cambio (adaptar al Charter)

| Riesgo | Ejemplos | Gate mínimo |
|---|---|---|
| R0 — Read-only | Inventario, inspección, documentación | Procedencia y límites; no exfiltración; tests documentales N/A |
| R1 — Reversible | Tests sintéticos, cambios acotados en branch | Tests relevantes + PR + revisión proporcional |
| R2 — Sensible | Datos reales, permisos, infraestructura, integración externa | Threat assessment + Owner/política + revisión independiente |
| R3 — Irreversible | Borrados, migración destructiva, pagos, deploy crítico | Autorización explícita, backup/rollback y pruebas de recuperación |

## DoD genérica

- [ ] Objetivo e issue documentados; cambios dentro del scope.
- [ ] Si cambia el código: tests/CI de código relevantes PASS o limitaciones declaradas; si solo cambia documentación: `tests: N/A`.
- [ ] Evidencia de seguridad y no filtración de datos.
- [ ] Feedback y reviews aplicables resueltos.
- [ ] ADR actualizado si cambió una decisión duradera.
- [ ] Plan de rollback/recuperación si procede.
- [ ] PR mergeada bajo autorización.
- [ ] Rama remota efímera eliminada/verificada, salvo dependencia declarada.
- [ ] Issue/estado y próximos pasos actualizados.

## Distinciones importantes

Un build PASS no demuestra por sí mismo que la feature cumpla los criterios de producto. Una revisión de agente no equivale a revisión independiente si utilizó los mismos supuestos y no contrastó el código. Una prueba en CI hosted no valida automáticamente la infraestructura self-hosted.

## Cierre de proyecto

El Owner acepta resultados contra el Charter mediante evidencia de extremo a extremo, operación y mantenimiento adecuados; los issues cerrados no sustituyen esa aceptación.
