#app/main.py
from fastapi import FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from db import database, Order
from models import OrderSchema
import uvicorn


app = FastAPI(title="prova1 API Rest nivel 2")

@app.post("/novo", tags=["pedido"])
async def novo_pedido(order: OrderSchema = Body(default=None)):
    if not database.is_connected:
        await database.connect()
    await Order.objects.create(
        name = order.name,
        email = order.email,
        description = order.description
    )
    return {"status do pedido": "criado com sucesso"}

@app.get("/pedidos", tags=["pedidos"])
async def read_all_orders():
    return await Order.objects.all()

@app.get("/pedidos/{id}", tags=["pedidos"])
async def read_user(id: int):
    if not database.is_connected:
        await database.connect()
    return await Order.objects.get(id=id)

@app.put("/pedidos/{id}", tags=["pedidos"])
async def update_todo(id: int, order: OrderSchema):
    if not database.is_connected:
        await database.connect()
    try:
        # Tenta encontrar a tarefa com o ID especificado
        pedido = await Order.objects.get_or_none(id=id)
        if pedido:
            # Atualiza os campos de título e conteúdo
            pedido.name = order.name
            pedido.email = order.email
            pedido.description = order.description
            await pedido.update()
            return {"message": "Order updated successfully"}
        else:
            # Se a tarefa não for encontrada, levanta uma exceção
            raise HTTPException(status_code=404, detail=f"Order with id {id} not found")
    except Exception as e:
        # Se ocorrer qualquer outra exceção, levanta uma exceção HTTP 404 com detalhes
        print("Error:", e)
        raise HTTPException(status_code=404, detail=f"Order with id {id} not found")

@app.delete("/pedidos/{id}", tags=["pedidos"])
async def delete_todo(id: int):
    if not database.is_connected:
        await database.connect()
    return await Order.objects.delete(id=id)

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()

origins = ["*"]  
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)