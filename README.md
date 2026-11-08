# Kit de transmisión · Espíritu Imperial

Gráficos en vivo para OBS de la premiación "Espíritu Imperial", que destaca al mejor trabajador de cada sucursal. Estilo de gala televisiva con la marca Imperial tomada de imperial.cl: azul marino, rojo y blanco, con Roboto Condensed y Roboto.

## Contenido

| Archivo / carpeta | Para qué sirve |
|---|---|
| `MATERIAL_IMPERIAL.html` | Panel de muestra de todo el material: pantallas, gráficos en vivo, PiP, transiciones y control. Ábrelo en Chrome para revisar o mostrar el kit. |
| `CONTROL_EN_VIVO.html` | Página de control. Se conecta a OBS y maneja sucursales y destacados, lower thirds, sucursal en pantalla, mensajes, mosca, pantallas, repeticiones y transiciones. |
| `PANEL_MIDI.html` | Para manejar todo desde un controlador MIDI. Ábrelo en el mismo Chrome que el control. |
| `Paneles/` | Gráficos para OBS: Inicio, Sucursal, Destacado, Destacados (tablero), Pausa, Final y overlays (lower third, sucursal en pantalla, mensaje, mosca, repetición), más los stingers HTML. |
| `Transiciones/` | Las 4 transiciones (Telón, Destello, Franjas, Marco) en video con transparencia y sonido: 4 s (corte 2000 ms) y **Corta** de 2 s (corte 1000 ms), en 1080p y `720p/`. |
| `Logos/` | Logo blanco de imperial.cl (300 px). Reemplázalo por el oficial en alta cuando lo tengas. |

## Puesta en marcha (una vez, en el PC de OBS)

1. Descomprime el kit en una carpeta fija, por ejemplo Documentos.
2. En OBS, ve a **Herramientas → Ajustes del servidor WebSocket**, habilítalo y copia la contraseña.
3. Abre `CONTROL_EN_VIVO.html` en Chrome, pega la contraseña y pulsa **CONECTAR**.
4. Pulsa **⚙ Instalar gráficos en OBS**. Se crean las escenas INICIO, ESTUDIO, SUCURSAL, DESTACADO, DESTACADOS, PAUSA, REPLAY, FINAL y las cinco PIP_ con sus gráficos, y la fuente del stinger HTML encima de todo. No se borra nada de lo que ya tengas.
5. En la escena ESTUDIO, agrega tus cámaras **debajo** de los gráficos.
6. En **Datos del evento** completa nombre, fecha, hora, lugar y web.
7. En **Sucursales y destacados** pega una línea por sucursal con este formato: `Sucursal | Nombre | Cargo | Ciudad | Años | Motivo`. Ciudad, años y motivo son opcionales. Con el botón **Foto** de cada fila cargas la foto del destacado; Shift + clic la quita.

## Durante el evento

Por cada sucursal:

1. **SUCURSAL**: presenta la sucursal ("Sucursal 3 de 12").
2. **DESTACADO**: revela al trabajador con su foto (o sus iniciales), cargo, sucursal, años en Imperial y motivo.
3. **ESTUDIO**: la cámara, con su lower third y la sucursal en pantalla.
4. **SIGUIENTE ▶**: pasa a la sucursal siguiente.

**DESTACADOS** muestra el tablero de todas las sucursales. Las que todavía no se premian aparecen como "Por revelar"; esto se desactiva en el control.

Las transiciones se eligen en la tarjeta **Transiciones HTML**. La animación tapa la pantalla y el control cambia la escena con un corte justo a la mitad.

Atajos de teclado: `1` a `9` ponen una escena en vista previa, `Shift` + número la pasa directo al aire, `P` repite y `M` guarda un momento.

## Picture in picture (PiP)

Cinco marcos en `Paneles/IMP_PIP_<Formato>.html`. El fondo de marca tapa todo menos las ventanas, que quedan transparentes para que se vea lo que pongas debajo en OBS:

| Escena | Formato | Ventanas |
|---|---|---|
| `PIP_PRESENTACION` | Presentación + cámara | 1340×754 y 420×236 |
| `PIP_DOS` | Dos cámaras | 885×498 cada una |
| `PIP_TRES` | Tres cámaras | 580×326 cada una |
| `PIP_VERTICAL` | Cámara + video vertical (celular) | 1150×647 y 460×818 |
| `PIP_ESQUINA` | Cámara chica sobre una pantalla completa | 420×236 |

*Instalar gráficos* crea las cinco escenas con el marco, una fuente de color del tamaño exacto en cada ventana (reemplázala por tu cámara, presentación o video y ajústala con *Transformar → Ajustar a la pantalla*) y el stinger HTML encima. En la tarjeta **Picture in picture** del control escribes el título y el nombre y cargo de cada ventana (por ejemplo el destacado y quien lo entrevista); **Persona actual en la ventana A** pone ahí al destacado del momento.

## Notas

- Imperial.cl solo publica su logo en 300 px, así que en las pantallas grandes manda el título del evento. Si consigues el logo oficial en alta (PNG grande o SVG), se puede reemplazar en todo el kit.
- Los nombres y cargos de ejemplo son de muestra; reemplázalos por los reales en el control.
- La carpeta `fuente/` tiene los scripts que generan el kit, para hacer cambios.
