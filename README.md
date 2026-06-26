# 🍽️ Sistema de Gestión de Restaurante

**Nombre:** Isabel Montaño

## 📋 Descripción
Este proyecto consiste en una aplicación básica desarrollada en Python 
utilizando Programación Orientada a Objetos (POO). El sistema permite 
registrar productos y clientes dentro de un restaurante, almacenando 
la información mediante objetos y organizando el código en diferentes 
módulos para facilitar su comprensión y mantenimiento.

## 📁 Estructura del Proyecto
```
restaurante_app/
│
├── 📂 modelos/
│   ├──  producto.py
│   └──  cliente.py
│
├── 📂 servicios/
│   └──  restaurante.py
│
├──  main.py
│
└── 📄 README.md
```

### Explicación de la estructura

- **modelos/**: Contiene las clases `Producto` y `Cliente`, que representan las entidades principales del sistema.
- **servicios/**: Contiene la clase `Restaurante`, encargada de administrar las listas de productos y clientes mediante diferentes métodos.
- **main.py**: Es el punto de inicio del programa. Aquí se crean los objetos, se agregan al restaurante y se muestra la información registrada en consola.
- **README.md**: Contiene la descripción del proyecto, la estructura, los tipos de datos utilizados y una breve reflexión sobre el desarrollo de la aplicación.

## 📊 Tipos de Datos
| Tipo    | Ejemplo                          |
|---------|----------------------------------|
| 🔤 str  | nombre, categoria, correo        |
| 🔢 int  | calorias, edad                   |
| 💲 float| precio                           |
| ✅ bool | disponible, es_frecuente         |

## 💡 Reflexión
Usar identificadores descriptivos como nombre, precio o agregar_plato 
permite entender el código sin necesidad de explicarlo. Elegir el tipo 
de dato correcto evita errores: float para precios, bool para estados 
y listas para almacenar varios objetos. Un proyecto modular bien 
organizado es más fácil de mantener y mejorar.