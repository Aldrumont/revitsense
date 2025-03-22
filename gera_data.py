import requests
import time

# Configurações do servidor (altere conforme necessário)
SERVER_URL = "http://localhost:3000/api/sensors"

# Parâmetros de cada sensor:
# Cada sensor possui: valor mínimo, valor máximo, passo de variação, valor atual e direção (1 para subida, -1 para descida)
sensors = {
    "temp": {
        "min": 18,
        "max": 28,
        "step": 3,  # aumento de 3 em 3 para a temperatura
        "value": 18,
        "direction": 1
    },
    "umidade": {
        "min": 483,
        "max": 640,
        "step": (640 - 483) * 0.1,  # 10% do intervalo
        "value": 483,
        "direction": 1
    },
    "co": {
        "min": 0,
        "max": 1000,
        "step": (1000 - 0) * 0.1,  # 10% do intervalo
        "value": 0,
        "direction": 1
    },
    "sensor_4": {
        "min": 0,
        "max": 100,
        "step": (100 - 0) * 0.1,  # 10% do intervalo
        "value": 0,
        "direction": 1
    }
}

def update_sensor(sensor_name):
    """Atualiza o valor do sensor com base no passo e na direção atual."""
    sensor = sensors[sensor_name]
    novo_valor = sensor["value"] + sensor["step"] * sensor["direction"]

    # Verifica se o novo valor extrapola os limites e inverte a direção se necessário
    if novo_valor > sensor["max"]:
        novo_valor = sensor["max"]
        sensor["direction"] = -1
    elif novo_valor < sensor["min"]:
        novo_valor = sensor["min"]
        sensor["direction"] = 1

    sensor["value"] = novo_valor
    return novo_valor

def send_sensor_data():
    """Atualiza todos os sensores, compõe os dados e envia para o servidor."""
    data = {}
    for sensor_name in sensors:
        data[sensor_name] = update_sensor(sensor_name)
    # Adiciona timestamp (em segundos)
    data["time"] = int(time.time())
    
    try:
        response = requests.post(SERVER_URL, json=data)
        print(f"Dados enviados: {data} | Status: {response.status_code}")
    except Exception as e:
        print(f"Erro ao enviar dados: {e}")

if __name__ == "__main__":
    while True:
        send_sensor_data()
        time.sleep(1)
