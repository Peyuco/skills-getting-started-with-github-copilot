"""Tests for GET /activities endpoint"""


def test_get_activities_returns_all_activities(client):
    """Test that /activities returns all available activities."""
    # Arrange
    # (client fixture is already set up)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert len(activities) == 9
    assert "Chess Club" in activities
    assert "Programming Class" in activities


def test_get_activities_contains_required_fields(client):
    """Test that activity objects have all required fields."""
    # Arrange
    # (client fixture is already set up)

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    for activity_name, activity_data in activities.items():
        assert "description" in activity_data
        assert "schedule" in activity_data
        assert "max_participants" in activity_data
        assert "participants" in activity_data
        assert isinstance(activity_data["participants"], list)


def test_get_activities_participants_are_correct(client):
    """Test that participants list is correct for an activity."""
    # Arrange
    # (client fixture is already set up)

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    assert "michael@mergington.edu" in activities["Chess Club"]["participants"]
    assert "daniel@mergington.edu" in activities["Chess Club"]["participants"]
    assert len(activities["Chess Club"]["participants"]) == 2
