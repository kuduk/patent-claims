def test_update_config_endpoint(client):
    """
    Test that the config update endpoint returns success.
    """
    payload = {
        "weaviate_url": "http://localhost:8080",
        "weaviate_api_key": ""
    }
    response = client.post("/api/v1/config/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Configuration updated successfully"}
