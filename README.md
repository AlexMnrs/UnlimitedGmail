# UnlimitedGmail

Generador de alias para cuentas de Gmail, explotando la característica de que Gmail ignora los puntos en el nombre de usuario. Esto permite generar miles de direcciones de correo electrónico "diferentes" que redirigen a la misma bandeja de entrada.

## Características

- **Generación Inteligente**: Algoritmo iterativo optimizado para generar todas las combinaciones posibles de puntos.
- **Validación**: Asegura que el formato de los alias generados sea válido.
- **Salida Organizada**: Guarda todos los resultados automáticamente en `gmail_aliases.txt`.
- **Interfaz en Español**: Fácil de usar, con instrucciones claras.

## Requisitos

- Python 3.6 o superior.
- No se requieren librerías externas.

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Abre una terminal en la carpeta del proyecto.

## Uso

Ejecuta el script principal:

```bash
python main.py
```

Sigue las instrucciones en pantalla:
1. Introduce tu nombre de usuario de Gmail (la parte antes del `@`).
2. El script generará todas las combinaciones y las guardará en `gmail_aliases.txt`.
3. ¡Disfruta de tus múltiples alias!

### Ejemplo

Si tu usuario es `ejemplo`, se generarán validaciones como:
- `e.jemplo@gmail.com`
- `ej.emplo@gmail.com`
- `e.j.e.m.p.l.o@gmail.com`
...

## Notas Importantes

- **Política de Gmail**: Gmail no distingue los puntos en el nombre de usuario. `usuario@gmail.com` es lo mismo que `u.s.u.a.r.i.o@gmail.com`.
- **Uso Responsable**: Recomendamos usar esta herramienta para pruebas de software, registros múltiples en servicios propios o filtrado de correo.

## Autor

**Alex Monrás**

---
© 2026 Alex Monrás. Todos los derechos reservados.