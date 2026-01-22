# Registro de Cambios

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [1.0.0] - 2026-01-22

### Añadido
- **Lógica Iterativa**: Nueva implementación para generar alias de Gmail utilizando un enfoque iterativo bit a bit, eliminando limitaciones de recursión y mejorando el rendimiento.
- **Validación de Entrada**: Verificación robusta del nombre de usuario para evitar caracteres inválidos (especialmente `@`).
- **Interfaz en Español**: Traducción completa de todos los mensajes, menús y comentarios del código.
- **Manejo de Archivos**: Guardado automático de resultados en `gmail_aliases.txt`.
- **Documentación**: README actualizado con instrucciones claras de uso e instalación.

### Cambiado
- Refactorización completa de `main.py` para seguir estándares profesionales.
- Eliminación de variables globales en favor de una funciones puras y limpias.
