---

# Documentación del Juego "Pin Pon?"

## Introducción
"Pin Pon?" es un juego arcade clásico desarrollado en Python utilizando la biblioteca Pygame. El objetivo del juego es romper los ladrillos ubicados en la parte superior de la pantalla con una bola controlada por el jugador. El juego incluye múltiples niveles de dificultad, puntuación, vidas y efectos de sonido.

## Estructura del Proyecto
El proyecto está organizado en cuatro archivos principales ubicados en el directorio "Clases":
- **Bola.py**: Contiene la clase que define el comportamiento de la bola en el juego.
- **Jugador.py**: Define la clase que representa al jugador y su interacción con la bola.
- **Ladrillo.py**: Contiene la clase que representa los ladrillos que deben ser destruidos para avanzar en el juego.
- **Main.py**: Implementa la lógica principal del juego y gestiona la interfaz gráfica.

## Clase Bola
La clase Bola define el comportamiento de la bola en el juego. Algunas características importantes incluyen:
- Movimiento de rebote dentro del área de juego.
- Detección de colisiones con los bordes y los objetos del juego.
- Métodos para actualizar la posición de la bola y mostrarla en pantalla.

## Clase Jugador
La clase Jugador representa al jugador y su interacción con la bola. Sus funcionalidades clave son:
- Movimiento horizontal controlado por el usuario.
- Detección de colisiones con la bola y los bordes del área de juego.
- Métodos para actualizar la posición del jugador y mostrarlo en pantalla.

## Clase Ladrillo
La clase Ladrillo modela los ladrillos que deben ser destruidos en el juego. Sus características incluyen:
- Vida y color variados que afectan la puntuación del jugador.
- Detección de colisiones con la bola y métodos para reducir su vida.
- Representación visual en la pantalla.

## Lógica del Juego
El archivo Main.py implementa la lógica principal del juego. Algunas de sus características son:
- Inicialización de Pygame y configuración de la pantalla.
- Gestión de eventos de teclado y detección de colisiones.
- Actualización de la posición de los objetos y renderizado en pantalla.
- Manejo de puntuación, vidas, niveles y efectos de sonido.
- Funciones adicionales como la colocación de ladrillos y la detección de fin de juego.

## Conclusiones
El juego "Pin Pon?" ofrece una experiencia entretenida y desafiante para los jugadores de todas las edades. Su código bien estructurado y modular facilita la comprensión y la ampliación del juego con nuevas características. La documentación proporcionada aquí sirve como una guía útil para entender el funcionamiento interno del juego y su implementación en Python con Pygame.

---

# flowchart
```mermaid
graph TD;
    A(Iniciar Juego) --> B(¿Hay colisiones?)
    B -->|Sí| C(¿Choque con Jugador?)
    C -->|Sí| D(Rebotar Bola)
    C -->|No| E(¿Choque con Ladrillo?)
    E -->|Sí| F(Reducir Vida del Ladrillo)
    F -->|Vida <= 0| G(Eliminar Ladrillo)
    G -->|Fin de Nivel| H(Generar nuevos Ladrillos)
    G -->|No| B
    E -->|No| B
    D -->|Fin de Pantalla| I(Perder Vida)
    I -->|Vidas > 0| B
    I -->|Vidas <= 0| J(Mostrar Pantalla de Game Over)
    J --> K(¿Reiniciar Juego?)
    K -->|Sí| A
    K -->|No| L(Terminar Juego)
    H -->|Nuevos Ladrillos| B
    B --> M(Actualizar Puntuación)
    M --> N(¿Bola ha tocado Fondo?)
    N -->|Sí| O(Perder Vida)
    O -->|Vidas > 0| B
    O -->|Vidas <= 0| J(Mostrar Pantalla de Game Over)
```
# class diagram

```mermaid
classDiagram
    class Jugador {
        -posx: int
        -posy: int
        -ancho: int
        -alto: int
        -vel: int
        -color: tuple
        -SIZE: tuple
        +__init__(posx, posy, ancho, alto, vel, color, screen, SIZE)
        +mostrar(): void
        +update(xFac: int): void
        +getRect(): Rect
    }
    class Bola {
        -posx: int
        -posy: int
        -rad: int
        -vel: int
        -color: tuple
        -screen: Surface
        -SIZE: tuple
        -xFac: int
        -yFac: int
        -bola: Circle
        +__init__(posx, posy, rad, vel, color, screen, SIZE)
        +mostrar(): void
        +update(): bool
        +reset(): void
        +golpe(): void
        +getRect(): Circle
    }
    class Ladrillo {
        -posx: int
        -posy: int
        -ancho: int
        -alto: int
        -color: tuple
        -damage: int
        -vida: int
        +__init__(posx, posy, ancho, alto, color, screen)
        +mostrar(): void
        +choque(): void
        +getRect(): Rect
        +getVida(): int
        +getColor(): tuple
    }
    class Main {
        -vidas: int
        -puntuacion: int
        -nivel: int
        -SIZE: tuple
        -NEGRO: tuple
        -BLANCO: tuple
        -VERDE: tuple
        -ROJO: tuple
        -fuenteTexto: Font
        -listaRandColor: list
        -clock: Clock
        -FPS: int
        +sonidoGolpe: Sound
        +sonidoBreak: Sound
        +sonidoWin: Sound
        +sonidoLose: Sound
        +__init__(): void
        +velocidadNivel(nivel: int): int
        +main(): void
        +gameOver(): bool
        +verChoque(ladrillo: Rect, bola: Circle): bool
        +colocarLadrillos(ancho, alto, separacionH, separacionV, nivel): list
    }

    Jugador -- Bola : contiene
    Jugador -- Main : contiene
    Bola -- Main : contiene
    Ladrillo -- Main : contiene


```

# Entity Relationship Diagram

```mermaid
erDiagram
    PARTICIPANTE ||--o{ JUGADOR : juega
    PARTICIPANTE ||--o{ LADRILLO : crea
    PARTICIPANTE ||--o{ BOLA : golpea
    JUGADOR {
        int jugador_id PK
        int posx
        int posy
        int ancho
        int alto
        int vel
        tuple color
        tuple SIZE
    }
    BOLA {
        int bola_id PK
        int posx
        int posy
        int rad
        int vel
        tuple color
        tuple SIZE
        int xFac
        int yFac
        int jugador_id FK
    }
    LADRILLO {
        int ladrillo_id PK
        int posx
        int posy
        int ancho
        int alto
        tuple color
        int vida
        int damage
        int bola_id FK
    }
    JUGADOR ||--o{ BOLA : controla
    BOLA ||--o{ LADRILLO : afecta

```

# Sequence Diagram

```mermaid
sequenceDiagram
    participant Jugador
    participant Bola
    participant Ladrillo
    participant Main

    Main->>Jugador: __init__()
    Main->>Bola: __init__()
    Main->>Ladrillo: __init__()
    Main->>Main: main()

    loop Actualización del juego
        Main->>Jugador: mostrar()
        Main->>Bola: mostrar()
        Main->>Ladrillo: mostrar()
        Jugador->>Jugador: update()
        Bola->>Bola: update()
        Main->>Main: verChoque()
        alt Colisión con Jugador
            Main->>Jugador: golpe()
        else Colisión con Ladrillo
            Main->>Ladrillo: choque()
            alt Vida del Ladrillo <= 0
                Main->>Main: eliminarLadrillo()
            end
            Main->>Main: actualizarPuntuacion()
        end
        alt Fin del Nivel
            Main->>Main: generarNuevosLadrillos()
        end
        alt Fin de Pantalla
            Main->>Bola: reset()
            Main->>Main: perderVida()
        end
    end

```
