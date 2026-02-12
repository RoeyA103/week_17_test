from fastapi import APIRouter


route = APIRouter(prefix="/analytics")

@route.get("/top-customers")
def get_top_customers():
    pass
