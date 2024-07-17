from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    app.logger.debug(f"Datos recibidos: {data}")
    
    # Verificación básica de los datos recibidos
    if not data or not data.get('username') or not data.get('password') or not data.get('email'):
        return jsonify({"error": "Datos faltantes o incorrectos"}), 400

    # Lógica para registrar el usuario (esto es un ejemplo)
    # En una aplicación real, aquí se haría la inserción en la base de datos, etc.
    
    return jsonify({"message": "Usuario creado"}), 201

if __name__ == '__main__':
    app.run(debug=True)
