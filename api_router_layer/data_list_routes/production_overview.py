from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

from presentation_layer.production_overview_controllers.production_overview_controllers import get_production_overview, update_production_overview, get_product_overview

app = APIRouter();

# WEBSOCKET MANAGER
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
manager = ConnectionManager();

@app.get("/update_production_overview", response_class=HTMLResponse)
async def get_current_production_overview_function():
    html_data = update_production_overview();
    return HTMLResponse(content=html_data, status_code=200)

@app.get("/get_production_overview", response_class=HTMLResponse)
async def get_production_overview_function():
    html_data = get_production_overview();
    return HTMLResponse(content=html_data, status_code=200)

@app.websocket("/current_production")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try: 
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You have updated the Current product to: {data}", websocket)
            await manager.broadcast(f"{data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client has left the chat")

@app.get("/get_product_overview/{product_id}", response_class=HTMLResponse)
async def get_product_overview_function(product_id):
    html_data = get_product_overview(product_id);
    return HTMLResponse(content=html_data, status_code=200)
