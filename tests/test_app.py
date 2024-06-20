from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_ola_mundo():
    client = TestClient(app)  # Organização

    response = client.get('/')  # Execução (Ação literal do teste)

    assert response.status_code == HTTPStatus.OK  # Afirmação (Garantia)
    assert response.json() == {'message': 'Olá Mundo'}
