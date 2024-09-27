from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'host': os.getenv('MYSQL_HOST'),
    'database': os.getenv('MYSQL_DATABASE'),
}

# Rota para inserir dados
@app.route('/insert', methods=['POST'])
def insert():
    data = request.json
    name = data.get('name')
    
    if not name:
        return jsonify({'error': 'Name is required'}), 400

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "INSERT INTO users (name) VALUES (%s)"
    cursor.execute(query, (name,))
    conn.commit()
    
    cursor.close()
    conn.close()

    return jsonify({'message': 'User added successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
