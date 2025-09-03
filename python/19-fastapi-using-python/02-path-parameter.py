from fastapi import FastAPI

app = FastAPI()

# Base URL route
@app.get('/')
def base_url():
    return "Base url"

# Example of a static route (matches only /base/2)
@app.get('/base/2')
def base_static():
    return {"data": 2}

# Example of a dynamic path parameter (matches /base/{id})
# Note: This will override the static route above if both are present.
@app.get("/base/{id}")
def base_dynamic(id: int):
    """
    Returns the dynamic data from the path parameter.
    Example: /base/100 -> {"dynamic_data": 100}
    """
    return {"dynamic_data": id}

# Example of a static route with a string path (matches only /base/name)
# WARNING: If /base/{id} is defined above this route, visiting /base/name will cause a validation error.
# This happens because FastAPI checks routes in the order they are defined.
# When you visit /base/name, FastAPI first tries to match /base/{id} and attempts to convert "name" to an int,
# which fails and results in a validation error. The static route /base/name is never reached.
# To avoid this, always define static routes (like /base/name) before dynamic routes (like /base/{id}).
@app.get("/base/name")
def base_name():
    """
    Returns static data for the /base/name route.
    If /base/{id} is defined above, visiting /base/name will result in a validation error,
    because FastAPI tries to parse 'name' as an int for the {id} parameter.
    """
    return {"dynamic_data": '10'}

# Example of a completely different static route (uncomment to use)
# @app.get('/dynamic_url/name')
# def dynamic_url():
#     return "new route"

"""
NOTES:
- If you visit /base/100, you'll get {"dynamic_data": 100}.
- If you visit /base/name, you'll get a validation error if /base/{id} is defined above,
  because FastAPI tries to parse 'name' as an int for {id}.
- To avoid conflicts, do not overlap static and dynamic routes at the same path level.
- Query parameters can be used for more flexibility.
"""
