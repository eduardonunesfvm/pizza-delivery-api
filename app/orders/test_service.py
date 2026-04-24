from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def get_token():
    response = client.post(
        "/auth/login-form",
        data={"username": "testando158@gmail.com", "password": "123123123"}
    )
    assert response.status_code == 200
    return response.json()["access_token"]


def test_criacao_pedido():
    token = get_token()

    response = client.post(
        "/pedidos/criar_pedido",
        json={"usuario": 1},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200

    data = response.json()
    assert "mensagem" in data


def test_criacao_pedido_unauthorized():
    response = client.post(
        "/pedidos/criar_pedido",
        json={"usuario": 1}
    )

    assert response.status_code == 401


def test_criacao_pedido_usuario_inexistente():
    token = get_token()

    response = client.post(
        "/pedidos/criar_pedido",
        json={"usuario": 9999},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code in [400, 404]