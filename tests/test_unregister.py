"""Tests for DELETE /activities/{activity_name}/unregister endpoint"""


def test_unregister_success_removes_participant(client):
    """Test that unregistering removes participant from activity."""
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already signed up

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert "Removed" in response.json()["message"]

    # Verify participant was removed
    activities_response = client.get("/activities")
    activities = activities_response.json()
    assert email not in activities[activity_name]["participants"]


def test_unregister_not_enrolled_returns_400(client):
    """Test that unregistering non-enrolled student returns 400."""
    # Arrange
    activity_name = "Chess Club"
    email = "notstudent@mergington.edu"  # Not signed up

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 400
    assert "not signed up" in response.json()["detail"]


def test_unregister_nonexistent_activity_returns_404(client):
    """Test that unregistering from nonexistent activity returns 404."""
    # Arrange
    activity_name = "Nonexistent Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_unregister_returns_success_message(client):
    """Test that successful unregister returns correct message format."""
    # Arrange
    activity_name = "Drama Club"
    email = "charlotte@mergington.edu"  # Already signed up

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert f"Removed {email} from {activity_name}" in response.json()["message"]
