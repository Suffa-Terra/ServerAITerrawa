from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)


@app.route('/')
def index():
    # HTML que incluye la imagen y un texto.
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Terrawa</title>
        <style>
            /* Estilos generales */
            body {
                text-align: center;
                font-family: 'Arial', sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
            }

            /* Estilo para el título */
            h1 {
                font-size: 2.5em;
                color: #7E3500;
                margin-top: 50px;
                text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
            }

            /* Estilos para la imagen */
            img {
                width: 300px;
                height: auto;
                margin-top: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                transition: transform 0.3s ease;
            }

            /* Efecto al pasar el cursor sobre la imagen */
            img:hover {
                transform: scale(1.05);
            }

            /* Fondo y espaciado */
            .container {
                padding: 20px;
            }
        </style>
    </head>
    <body>

        <div class="container">
            <h1>Bienvenido a Terrawa</h1>
            <img src="{{ url_for('static', filename='Terrawa.jpeg') }}" alt="Logo">
        </div>

    </body>
    </html>
    """
    return render_template_string(html_content)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)
