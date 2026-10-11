# Engineering workflow — issues → PR → merge → cleanup

## 1. Planificar

- Para trabajo sustancial: abrir o actualizar **un issue** con problema, alcance, no-objetivos, criterios de aceptación, riesgos y evidencia.
- Investigar primero cuando el problema todavía sea UNKNOWN. Evitar codificar contra hipótesis no verificadas.
- Cambios mínimos de documentación o erratas pueden ir directamente a una PR según criterio del Owner.
- Identificar qué se puede ejecutar autónomamente y qué requiere un gate.

## 2. Rama y ejecución

- Crear rama acotada: feat/<issue>-slug, fix/<issue>-slug, docs/<issue>-slug o research/<issue>-slug.
- Nunca usar una rama global de cambios no relacionados ni hacer push directo a main/master tras bootstrap sin una excepción explícita.
- Commits acotados y reproducibles; no secretos, historiales privados ni dumps.
- Si cambia arquitectura o contratos duraderos, añadir ADR propuesto y la decisión aprobada.

## 3. Pruebas y revisión

- Ejecutar pruebas de la superficie afectada y aportar comando, entorno, versión y resultado.
- Diferenciar PASS / FAIL / HOLD / UNKNOWN. La ausencia de pruebas nunca es PASS.
- En trabajos de riesgo elevado, encargar una revisión independiente con acceso al diff y evidencias.
- Resolver comentarios pendientes o documentar el bloqueo antes de solicitar merge.
- Utilizar .github/PULL_REQUEST_TEMPLATE.md como contrato de entrega.

## 4. Merge y cierre

1. Comprobar que la PR corresponde al issue y que los cambios no amplían el alcance.
2. Comprobar los gates de seguridad, tests y review exigidos.
3. Fusionar por el método configurado en el repositorio, por defecto preferentemente squash para cambios lineales.
4. **Verificar que el merge realmente terminó**, y actualizar/ cerrar el issue con las evidencias.
5. **Eliminar la rama remota de trabajo** cuando ninguna PR o proceso activo dependa de ella. **Nunca eliminar la rama principal ni las protegidas.**
6. Confirmar que la rama desapareció. Si no se puede borrar, registrar el impedimento y no declarar limpieza completada.

**Recomendación de GitHub:** Settings → General → Pull Requests → Automatically delete head branches. Configurar esa opción en **cada repositorio nuevo**; no se debe asumir que se hereda del template.

## 5. Incidentes y hotfixes

Para urgencias: abrir issue breve, acotar impacto, priorizar reversibilidad, capturar pruebas esenciales y documentar posmortem cuando haga falta. La urgencia no autoriza falsificar evidencias o introducir secretos en GitHub.

## 6. Evidencia mínima en la PR

Issue, diff, pruebas realmente ejecutadas, riesgos, permisos relevantes, review, rollback cuando corresponda y gates PASS/HOLD. Si una comprobación es inaplicable, marcar N/A con justificación.
