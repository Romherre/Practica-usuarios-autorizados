# Práctica Usuarios Autorizados

Proyecto de práctica con **Django** (backend/API) y **Angular** (frontend) para implementar un sistema de usuarios autorizados: registro, login y control de acceso.

## Funcionalidad

- API en Django (`user_api`) para gestión de usuarios.
- App de usuarios (`users`) con lógica de autenticación/autorización.
- Frontend en Angular (`user-app`) que consume la API.

## Tecnologías

Python, Django, Angular.

## Cómo correrlo localmente

Este es un proyecto backend (Django + Angular), por lo que no tiene demo en vivo vía GitHub Pages. Para probarlo localmente:

1. Cloná el repositorio.
2. Instalá las dependencias de Python (`pip install -r requirements.txt` si existe, o Django manualmente) y corré `python manage.py runserver`.
3. Instalá las dependencias de Angular dentro de `user-app` (`npm install`) y corré `ng serve`.

**Nota:** el archivo `db.sqlite3` quedó incluido en el repositorio. Al ser un proyecto de práctica no es crítico, pero en un proyecto real se recomienda excluir la base de datos del control de versiones (agregarla a `.gitignore`).

---
Desarrollado por **Romina Herrera** · [LinkedIn](https://www.linkedin.com/in/romina-herreramicv/)
