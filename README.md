# 📧 UnlimitedGmail

**Generador masivo de alias para Gmail mediante permutación de puntos.**

Este script de Python explota la característica nativa de Gmail que ignora los puntos en el nombre de usuario (parte local de la dirección). Esto permite generar **miles de direcciones de correo electrónico únicas** que redirigen a la misma bandeja de entrada principal.

Ideal para:
- 🧪 Pruebas de Software (QA)
- 📝 Registros múltiples en servicios
- 🕵️ Filtrado y organización de correo

---

## ✨ Características

- 🚀 **Generación Inteligente**: Algoritmo recursivo optimizado para cubrir el 100% de las combinaciones posibles.
- ✅ **Validación Automática**: Asegura la integridad del formato de correo.
- 📂 **Salida Organizada**: Exportación automática a un archivo limpio (`gmail_aliases.txt`).
- 🇪🇸 **100% en Español**: Interfaz y documentación claras y accesibles.
- ⚡ **Ligero**: Sin dependencias pesadas, solo Python puro.

## 🛠️ Requisitos

- **Sistema Operativo**: Windows, macOS, o Linux.
- **Lenguaje**: [Python 3.6](https://www.python.org/downloads/) o superior.
- **Librerías**: No requiere instalación de librerías externas (Standard Library).

## 📥 Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/AlexMnrs/UnlimitedGmail.git
   ```
2. **Navega al directorio**:
   ```bash
   cd UnlimitedGmail
   ```

## 💻 Uso

1. **Ejecuta el script**:
   ```bash
   python main.py
   ```

2. **Sigue las instrucciones**:
   - El programa te pedirá tu usuario de Gmail (lo que va antes del `@`).
   - *Ejemplo*: Si tu correo es `usuario@gmail.com`, escribe `usuario`.

3. **Revisa los resultados**:
   - El script generará un archivo llamado `gmail_aliases.txt` en la misma carpeta.
   - Abre este archivo para ver todos los alias generados.

### 📝 Ejemplo de Salida

Si ingresas `alex`, el archivo contendrá:
```text
alex@gmail.com
a.lex@gmail.com
al.ex@gmail.com
a.l.ex@gmail.com
...
a.l.e.x@gmail.com
```

## ⚠️ Notas Importantes

- **Política de Google**: Gmail oficialmente trata `t.u.n.o.m.b.r.e` igual que `tunombre`. Todos los correos llegarán a tu bandeja de entrada principal.
- **Límites**: Aunque puedes generar miles de alias, algunos servicios externos pueden tener filtros para detectar y bloquear este comportamiento.
- **Uso Ético**: Esta herramienta está diseñada con fines educativos y de productividad. Por favor, úsala responsablemente.

## 👨‍💻 Autor

**Alex Monrás**
*Desarrollador de Software & Entusiasta de la Automatización*

## 📄 Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE).

---
© 2026 Alex Monrás.