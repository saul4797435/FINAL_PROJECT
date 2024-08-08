# Diseño de Base de Datos

Este documento describe el diseño de la base de datos para el administrador de contraseñas.

## Tablas Principales

### Usuarios

- **ID:** Clave primaria.
- **Username:** Nombre de usuario único.
- **Password Hash:** Hash de la contraseña del usuario.

### Contraseñas

- **ID:** Clave primaria.
- **User ID:** Clave foránea a la tabla Usuarios.
- **Password:** Contraseña encriptada.
- **Description:** Descripción de la contraseña.

## Diagrama de Base de Datos

![Diagrama de Base de Datos](path_to_database_diagram)
