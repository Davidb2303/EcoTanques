# REQUERIMIENTOS FUNCIONALES Y ARQUITECTURA

## Tecnologías

- **Backend (Microservicios):** Node.js + TypeScript (NestJS o Express)
- **Base de datos:** PostgreSQL (recomendado), MongoDB (opcional para datos no estructurados)
- **Mensajería y eventos:** MQTT (microservicio en Python), RabbitMQ o Redis para eventos internos
- **Notificaciones Push:** Firebase Cloud Messaging (FCM)
- **Autenticación:** JWT, OAuth2
- **Contenedores:** Docker
- **Orquestación:** Docker Compose o Kubernetes
- **Documentación API:** Swagger/OpenAPI

---

## Arquitectura General

- **Microservicios independientes** para cada dominio funcional.
- Comunicación entre microservicios vía HTTP (REST) y eventos (RabbitMQ/Redis).
- El microservicio MQTT (Python) recibe datos de sensores y los distribuye al resto del sistema.
- Cada microservicio tiene su propia base de datos (Database per Service).

---

## Microservicios y Requerimientos Funcionales

### 1. Microservicio de Usuarios (`users-service`)

**Tecnologías:** Node.js, TypeScript, Express/NestJS, PostgreSQL

**Funcionalidades:**
- Registro y autenticación de usuarios.
- Gestión de roles y permisos.
- Actualización y eliminación de usuarios.
- Exposición de API REST para gestión de usuarios.

---

### 2. Microservicio de Tanques (`tanks-service`)

**Tecnologías:** Node.js, TypeScript, Express/NestJS, PostgreSQL

**Funcionalidades:**
- Alta, baja y modificación de tanques.
- Asociación de tanques a usuarios.
- Consulta de estado y características de tanques.
- API REST para gestión de tanques.

---

### 3. Microservicio de Sensores (`sensors-service`)

**Tecnologías:** Node.js, TypeScript, Express/NestJS, PostgreSQL

**Funcionalidades:**
- Registro y administración de sensores.
- Asociación de sensores a tanques.
- Consulta de sensores y su estado.
- API REST para gestión de sensores.

---

### 4. Microservicio de Mediciones (`meditions-service`)

**Tecnologías:** Node.js, TypeScript, Express/NestJS, PostgreSQL

**Funcionalidades:**
- Recepción y almacenamiento de mediciones desde el microservicio MQTT.
- Consulta de mediciones históricas y en tiempo real.
- Generación de reportes y tendencias.
- API REST para consulta de mediciones.

---

### 5. Microservicio de Notificaciones (`notifications-service`)

**Tecnologías:** Node.js, TypeScript, Express/NestJS, Firebase Cloud Messaging

**Funcionalidades:**
- Envío de notificaciones push a usuarios.
- Gestión de plantillas y tipos de notificaciones.
- Integración con eventos del sistema (por ejemplo, niveles críticos).
- API REST para gestión y consulta de notificaciones.

---

### 6. Microservicio de Inteligencia Artificial (`ai-service`)

**Tecnologías:** Polards, TensorFlow.js

**Funcionalidades:**
- Procesamiento de datos históricos para predicción y análisis.
- Generación de alertas inteligentes.
- Exposición de endpoints para consulta de predicciones.

---

### 7. Microservicio MQTT (`mqtt-service`)

**Tecnologías:** Python, paho-mqtt, Django ORM (opcional para integración)

**Funcionalidades:**
- Suscripción a tópicos MQTT para recibir datos de sensores.
- Procesamiento y validación de datos recibidos.
- Envío de datos procesados a los microservicios correspondientes (por HTTP o eventos).
- Registro de errores y eventos.

---

## Ejemplo de Flujo de Datos

1. **Sensor** envía datos a **Broker MQTT**.
2. **Microservicio MQTT (Python)** recibe los datos, los valida y los reenvía al **meditions-service**.
3. **meditions-service** almacena la medición y, si detecta un evento relevante, notifica a **notifications-service**.
4. **notifications-service** envía una notificación push al usuario correspondiente.
5. **ai-service** puede analizar los datos para generar predicciones o alertas inteligentes.

---

## Notas

- Todos los microservicios (excepto MQTT y Machine Learning) deben implementarse en TypeScript.
- Cada microservicio debe ser desplegable y escalable de forma independiente.
- La comunicación entre microservicios debe ser segura y autenticada.
- El microservicio MQTT debe permanecer en Python por requerimiento del sistema.

---
