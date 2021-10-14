def test_get_goals_no_saved_goals(client):
    # Act
    response = client.get("/goals")
    response_body = response.get_json()

    # Assert (replace ... with the correct values)
    assert response.status_code == ...
    assert response_body == ...


def test_get_goals_one_saved_goal(client, one_goal):
    # Act
    response = client.get("/goals")
    response_body = response.get_json()

    # Assert (replace ... with the correct values)
    assert response.status_code == ...
    assert len(response_body) == ...
    assert response_body == ...


def test_get_goal(client, one_goal):
    # Act
    response = client.get("/goals/1")
    response_body = response.get_json()

    # Assert (there should be at least 3 assertions)
    


def test_get_goal_not_found(client):
    # Act
    response = client.get("/goals/1")
    response_body = response.get_json()

    # Assert (there should be at least 2 assertions)



def test_create_goal(client):
    # Act
    response = client.post("/goals", json={
        "title": "My New Goal"
    })
    response_body = response.get_json()

    # Assert (there should be at least 3 assertions)

def test_create_goal_missing_title(client):
    # Act
    response = client.post("/goals", json={})
    response_body = response.get_json()

    # Assert (there should be at least 2 assertions)

def test_update_goal(client, one_goal):
    pass
    # Act

    # Assert

def test_update_goal_not_found(client):
    pass
    # Act

    # Assert



def test_delete_goal(client, one_goal):
    # Act

    # Assert

    # Check that the goal was deleted
    response = client.get("/goals/1")
    assert response.status_code == 404


def test_delete_goal_not_found(client):
    # Act

    # Assert




