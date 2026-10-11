# Architecture Decision Records (ADRs)

Los ADR registran **por qué** tomamos decisiones duraderas, no tareas ni conversaciones completas.

## Cuándo escribir uno

Cuando una elección cambia arquitectura, fuentes de verdad, privacidad, seguridad, despliegue, coste operativo, contrato público o patrón de trabajo.

No convertir cada pequeño cambio de código en un ADR; el issue y la PR suelen ser suficientes.

## Ciclo de vida

1. Copiar ADR-0000-template.md a ADR-NNNN-descripcion.md.
2. Estado **PROPOSED** mientras se evalúan alternativas.
3. Registrar drivers, opciones, implicaciones, evidencia y autoridad que acepta.
4. Marcar **ACCEPTED** tras decisión autorizada.
5. Si cambia la decisión, crear un ADR nuevo y enlazar el anterior como **SUPERSEDED**, sin reescribir el pasado.

Las decisiones deben poder verificarse por un agente nuevo leyendo el ADR y las pruebas enlazadas.

## Índice

- ADR-0000: plantilla, no una decisión aceptada.

Añadir entradas aquí conforme se aprueben decisiones.
