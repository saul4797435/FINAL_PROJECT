# Password Manager

Este proyecto es un ejemplo de cómo implementar un pipeline de CI/CD utilizando herramientas modernas como Docker, Docker Compose y GitHub Actions. El objetivo es mostrar cómo se puede automatizar el proceso de integración y entrega continua para mejorar la calidad y la seguridad del software.

## Descripción del Proyecto

El proyecto está organizado en varias carpetas y archivos que estructuran el pipeline de CI/CD: - **.github/workflows/**: Contiene el archivo `ci-cd.yml` que define el pipeline de GitHub Actions. - **src/**: Contiene el código fuente del módulo principal del proyecto. - **src/tests/**: Incluye los archivos de pruebas unitarias y de integración. - **docs/**: Contiene la documentación técnica del proyecto, incluyendo arquitectura, diseño de base de datos y reportes de seguridad.

## Cómo Ejecutar el Proyecto

Para ejecutar el proyecto localmente, se utiliza Docker y Docker Compose. Estas herramientas permiten crear un entorno de prueba consistente y reproducible. A continuación se detalla el paso para clonar el repositorio, construir y ejecutar los servicios.

### Paso de Instalación

Clonar el repositorio, construir y correr la aplicación con Docker Compose.

La aplicación estará disponible en `http://localhost:8000`.

## CI/CD con GitHub Actions

El pipeline de CI/CD se automatiza con GitHub Actions, que se configura para ejecutarse cada vez que se realiza un push o pull request al repositorio. El archivo `ci-cd.yml` en la carpeta `.github/workflows/` define los pasos del pipeline, que incluyen la ejecución de pruebas unitarias e integradas, así como análisis de seguridad.

## Descripción de los Servicios

- **app**: Este servicio ejecuta las pruebas unitarias e integradas utilizando pytest, asegurando que el código funcione correctamente y que los diferentes componentes del sistema interactúen según lo esperado.
- **db**: Este servicio gestiona la base de datos PostgreSQL, utilizada para almacenar datos de usuario y contraseñas encriptadas.

## Herramientas Utilizadas

- **Docker**: Docker se utiliza para crear contenedores que encapsulan el entorno de prueba, asegurando que el software se ejecute de manera consistente en cualquier sistema.
- **Docker Compose**: Docker Compose permite orquestar múltiples servicios de contenedores, facilitando la gestión de entornos complejos que requieren varios componentes interdependientes.
- **GitHub Actions**: GitHub Actions se utiliza para la automatización del pipeline de CI/CD, permitiendo ejecutar flujos de trabajo definidos en archivos YAML cada vez que se realizan cambios en el repositorio.
- **pytest**: pytest es una herramienta de pruebas para Python que se utiliza para ejecutar pruebas unitarias e integradas, proporcionando un marco sencillo pero potente para verificar la funcionalidad del código.
- **Snyk**: Snyk es una herramienta de análisis de seguridad para detectar vulnerabilidades en las dependencias del proyecto y asegurar que cumple con las mejores prácticas de seguridad.

## Conclusiones

Implementar un pipeline de CI/CD con pruebas automatizadas y análisis de seguridad mejora significativamente la calidad y seguridad del software. Permite detectar y corregir errores de manera rápida, acelera el proceso de entrega y asegura que el software cumple con los estándares de calidad y seguridad desde el inicio.
