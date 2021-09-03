from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.
# Your API almost always has to send a response body. But clients don't necessarily need to send request bodies all the time.
# Request body = data sent by the client to your API. (pydantic's BaseModel)
# Response body = data your API sends to the client.


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    result = {"item_id": item_id, **item_dict}
    if q:
        result.update({"q": q})
    return result


if __name__ == "__main__":
    import os

    os.system("uvicorn request_body:app --reload")
