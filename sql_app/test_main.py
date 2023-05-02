from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_post_jobs():
  response = client.post("/jobs/",json={
    "title":"Python Developer",
    "company":"My Company",
    "location":"Paris",
    "posted_date":"2023-04-23T12:30",
    "description":"A python developer with good skills",
    "skills":"python,django,fastapi"
  })
  assert response.status_code == 200

def test_get_jobs():
  response=client.get("/jobs/")
  assert response.status_code==200

def test_search_skill():
  response=client.get("/jobs/search-skill/")
  assert response.status_code==200

def test_search_location():
  response=client.get("/jobs/search-location/")
  assert response.status_code==200
  