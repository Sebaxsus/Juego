---

# "Pin Pon?" Game Documentation

## Introduction
"Pin Pon?" is a classic arcade game developed in Python using the Pygame library. The objective of the game is to break the bricks located at the top of the screen with a ball controlled by the player. The game includes multiple levels of difficulty, scoring, lives, and sound effects.

## Project Structure
The project is organized into four main files located in the "Classes" directory:
- **Bola.py**: Contains the class that defines the behavior of the ball in the game.
- **Jugador.py**: Defines the class representing the player and its interaction with the ball.
- **Ladrillo.py**: Contains the class representing the bricks that need to be destroyed to advance in the game.
- **Main.py**: Implements the main logic of the game and manages the graphical interface.

## Bola Class
The Bola class defines the behavior of the ball in the game. Some key features include:
- Bouncing movement within the game area.
- Collision detection with the edges and objects of the game.
- Methods to update the position of the ball and display it on the screen.

## Jugador Class
The Jugador class represents the player and its interaction with the ball. Its key functionalities are:
- Horizontal movement controlled by the user.
- Collision detection with the ball and the edges of the game area.
- Methods to update the player's position and display it on the screen.

## Ladrillo Class
The Ladrillo class models the bricks that need to be destroyed in the game. Its features include:
- Varied life and color affecting the player's score.
- Collision detection with the ball and methods to reduce its life.
- Visual representation on the screen.

## Game Logic
The Main.py file implements the main logic of the game. Some of its features include:
- Pygame initialization and screen setup.
- Keyboard event handling and collision detection.
- Update of object positions and rendering on the screen.
- Management of score, lives, levels, and sound effects.
- Additional functions such as brick placement and end-game detection.

## Conclusion
The "Pin Pon?" game offers an entertaining and challenging experience for players of all ages. Its well-structured and modular code facilitates understanding and expansion of the game with new features. The documentation provided here serves as a useful guide to understand the internal workings of the game and its implementation in Python with Pygame.

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
# Variable Dictionary

```markdown
Variable Dictionary
-------------------

### Bola Class
- `posx`: Integer representing the x-coordinate position of the ball.
- `posy`: Integer representing the y-coordinate position of the ball.
- `rad`: Integer representing the radius of the ball.
- `vel`: Integer representing the velocity of the ball.
- `color`: Tuple representing the color of the ball.
- `screen`: Pygame Surface object representing the game screen.
- `SIZE`: Tuple representing the size of the game screen.
- `xFac`: Integer representing the x-direction factor of the ball's movement.
- `yFac`: Integer representing the y-direction factor of the ball's movement.
- `bola`: Pygame Circle object representing the ball.

### Jugador Class
- `posx`: Integer representing the x-coordinate position of the player.
- `posy`: Integer representing the y-coordinate position of the player.
- `ancho`: Integer representing the width of the player.
- `alto`: Integer representing the height of the player.
- `vel`: Integer representing the velocity of the player.
- `color`: Tuple representing the color of the player.
- `screen`: Pygame Surface object representing the game screen.
- `SIZE`: Tuple representing the size of the game screen.
- `jugadorRect`: Pygame Rect object representing the player's rectangle.

### Ladrillo Class
- `posx`: Integer representing the x-coordinate position of the brick.
- `posy`: Integer representing the y-coordinate position of the brick.
- `ancho`: Integer representing the width of the brick.
- `alto`: Integer representing the height of the brick.
- `color`: Tuple representing the color of the brick.
- `damage`: Integer representing the damage inflicted by the brick.
- `screen`: Pygame Surface object representing the game screen.
- `vida`: Integer representing the health of the brick.
- `ladrilloRect`: Pygame Rect object representing the brick's rectangle.

### Main
- `vidas`: Integer representing the number of lives remaining.
- `puntuacion`: Integer representing the player's score.
- `nivel`: Integer representing the current level of the game.
- `SIZE`: Tuple representing the size of the game screen.
- `bgImg`: Pygame Surface object representing the background image.
- `NEGRO`: Tuple representing the color black.
- `BLANCO`: Tuple representing the color white.
- `VERDE`: Tuple representing the color green.
- `ROJO`: Tuple representing the color red.
- `fuenteTexto`: Pygame Font object representing the text font.
- `listaRandColor`: List containing randomly selected colors for bricks.
- `screen`: Pygame Surface object representing the game screen.
- `clock`: Pygame Clock object representing the game clock.
- `FPS`: Integer representing the frames per second of the game.
```