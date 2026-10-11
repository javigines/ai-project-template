# Runbook operativo (completar si hay servicios)

**Estado:** N/A mientras el proyecto no tenga despliegue operativo.

## Norma por defecto: hosts productivos y GHCR

Si el proyecto utiliza un host productivo (Mac Mini, servidor doméstico u otro), este **ya presta servicio** y no puede tratarse como sandbox. Para cualquier prueba autorizada que lo toque:

1. Antes: confirmar scope y autorización; inventariar servicios existentes relevantes, comprobar salud y obtener baseline sanitario de CPU/RAM/I/O/espacio/red/puertos.
2. Durante: límites de recursos, nombres/puertos/volúmenes aislados; sin reinicios ni cambios de otros servicios; mantener lista de artefactos temporales propios y cleanup preparado para error o interrupción.
3. Después (incluso FAIL): retirar únicamente lo creado para las pruebas y que no sea parte del despliegue final autorizado; verificar salud/baseline y **CLEANUP=PASS**. Si queda algún resto o no se puede comprobar, reportar **HOLD** con remediación. Nunca ejecutar `docker system prune` indiscriminado ni borrar recursos compartidos.

**Imágenes publicadas:** exclusivamente GHCR `ghcr.io/<OWNER>/<IMAGE>` **PRIVATE**, comprobar permisos/visibilidad específicos del paquete en GitHub, publicar con mínima autorización, registrar digest/version y verificar pull y rollback. No copiar secretos en imágenes.

Estas son reglas operativas; **no** implican tests automáticos de documentación.

## Entornos y servicios

| Entorno | Responsable | Cómo acceder | Restricciones |
|---|---|---|---|
| [Entorno] | [Owner] | [Acceso aprobado] | [Política] |

## Build y deployment

[Pasos reproducibles; enlace a workflow y versión; rollback.]

## Operación

[Health checks, observabilidad, logs seguros, alertas, costes, cuotas y ownership.]

## Incidentes

[Cómo evaluar severidad, pausar, diagnosticar y escalar; no incorporar secretos a tickets.]

## Backups y recuperación

[Ubicación segura, cifrado, frecuencia, RPO/RTO si aplica y último restore **probado**.]

## Criterios de operabilidad

[Pruebas de arranque, actualización, reinicio, recuperación y eliminación controlada.]

Actualizar este documento únicamente con hechos verificados; no declarar PASS para operaciones no probadas.
