"""Tests for GET / endpoint"""


def test_root_redirects_to_static(client):
    """Test that root path redirects to static HTML."""
    # Arrange
    # (client fixture is already set up)

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert "/static/index.html" in response.headers["location"]


def test_root_redirect_is_temporary(client):
    """Test that root redirect uses temporary 307 status."""
    # Arrange
    # (client fixture is already set up)

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    # 307 is Temporary Redirect (POST-preserving)
    assert response.status_code == 307
