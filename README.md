# Big Bang AI - Coworking Synthetic Data

Este repositorio contiene:

- `synthetic_contacts_100.csv`: 100 contactos sintéticos para un coworking en Tarragona, basados en un esquema exportado de GoHighLevel.
- `generate_synthetic_contacts.py`: generador en Python para crear datasets similares con N registros.

## Contexto
Actividad para el programa Big Bang AI. El dataset simula leads y clientes potenciales que llegan por distintos canales (Facebook Ads, Web, Instagram orgánico, Eventos con QR), con etiquetas normalizadas.

## Esquema
Columnas:
- First Name, Last Name, Business Name, Company Name, Phone, Email, Created, Last Activity, Tags, Razón de Contacto, Propuesta de Valor, Additional Emails, Additional Phones.

Notas:
- Fechas en ISO 8601 con offset +02:00.
- `Tags` incluye etiquetas existentes y nuevas: `source:*`, `sector:*` (MECE), `actividad:*`, `servicio:*`.
- Campos multivalor (emails/teléfonos adicionales) vienen como listas separadas por coma dentro de comillas.

## Sectores (MECE)
- tecnologia-y-software, marketing-y-medios, educacion-y-formacion, salud-y-bienestar, servicios-profesionales, finanzas-y-seguros, comercio-y-ecommerce, hosteleria-y-eventos, inmobiliario-y-construccion, administracion-publica-y-ong, industria-y-fabricacion, creadores-y-artistas, otros.

## Uso del generador
Requiere Python 3.9+.

```bash
python3 generate_synthetic_contacts.py output.csv 100 42
```
Parámetros:
- `output.csv`: ruta de salida (opcional; por defecto `synthetic_contacts_100.csv`).
- `100`: número de filas (opcional; por defecto 100).
- `42`: semilla aleatoria (opcional; por defecto 42).

## Licencia
MIT
