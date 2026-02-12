from fastapi import APIRouter
import dal


route = APIRouter(prefix="/analytics")

@route.get("/top-customers")
def get_top_customers():
    return dal.get_top_customers()

@route.get("/customers-without-orders")
def get_customerswithout_orders():
    pass

@route.get("/zero-credit-active-customers")
def get_zero_credit_active_customers():
    pass
