# Explicación Técnica y Diagrama de Comunicación Web

## Actividad 1. Narración integrada del proceso HTTP

Cuando un usuario interactúa con la aplicación (por ejemplo, para calcular el importe de una compra), todo el ciclo de vida de la petición sigue la arquitectura cliente-servidor tradicional del desarrollo web.

1. *Inicio de la petición: El usuario interactúa con el **cliente* (navegador web como Chrome o Firefox) e introduce en la barra de direcciones el identificador del servicio (por ejemplo, http://127.0.0.1:5000/compra).
2. *Resolución de red y conexión: El sistema utiliza la **dirección IP* 127.0.0.1 (que representa la interfaz local o localhost) junto con el *puerto* 5000 para ubicar exactamente el proceso del *servidor* donde se ejecuta la aplicación.
3. *Envío de datos mediante HTTP: Al llenar el formulario con la cantidad y el precio, y hacer clic en el botón de envío, el **frontend* desencadena un mensaje estándar del protocolo *HTTP* especificando el método *POST. Los datos capturados viajan dentro del cuerpo de la petición (request*).
4. *Procesamiento en el Servidor: En el **backend, el entorno de ejecución en **Python* impulsado por el microframework *Flask* recibe el *request. **Flask* consulta su tabla de enrutamiento y determina que la *ruta* /compra debe procesar la solicitud.
5. *Ejecución de la lógica de negocio: La función asociada en **Python* extrae los parámetros recibidos, realiza los cálculos aritméticos correspondientes (subtotal, descuento del 10% si aplica y total) y prepara los datos resultantes.
6. *Renderizado de la plantilla: El **backend* invoca el motor Jinja2 para procesar el *template* HTML (compra.html), inyectando las variables de los resultados en la estructura visual estructurada con el framework *Bootstrap* y reglas en *CSS*.
7. *Retorno de la Respuesta: El **servidor* construye un paquete *response* de *HTTP* (con código de estado 200 OK) cargado con el documento *HTML* dinámicamente generado.
8. *Despliegue visual: El **cliente* procesa el *HTML* y los estilos *CSS* (apoyándose si fuera necesario en funciones interactivas del navegador mediante *JavaScript*) para renderizar la pantalla final que visualiza el empleado con todos los importes calculados.

---

## Actividad 2. Diagrama de flujo de la comunicación

```mermaid
sequenceDiagram
    autonumber
    actor Cliente as Cliente (Navegador Web)
    participant Servidor as Servidor (127.0.0.1:5000)
    participant FlaskApp as Backend (Python / Flask)
    participant Template as Template (Jinja2 / HTML)

    Cliente->>Servidor: Petición HTTP POST a /compra (IP: 127.0.0.1, Puerto: 5000) con datos del form
    Servidor->>FlaskApp: Entrega Request a la ruta @app.route('/compra')
    Note over FlaskApp: Python evalúa el método POST,<br/>calcula subtotal, descuento y total
    FlaskApp->>Template: Envía datos calculados para renderizar compra.html
    Note over Template: Se combina la estructura HTML,<br/>Bootstrap y estilos CSS con los datos
    Template-->>FlaskApp: Devuelve HTML compilado
    FlaskApp-->>Servidor: Prepara la Response HTTP (Código 200 OK)
    Servidor-->>Cliente: Envía el HTML procesado en la Response
    Note over Cliente: El navegador renderiza el HTML/CSS<br/>y muestra el resultado final al usuario
    