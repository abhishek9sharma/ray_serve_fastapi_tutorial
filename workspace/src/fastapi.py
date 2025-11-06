from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal


app = FastAPI(title="Ray FastAPI POST Example")

class TransactionPayload(BaseModel):
    txn_id: str = Field(..., description="Transaction ID")
    cif: str = Field(..., description="Customer CIF")
    amount: float = Field(..., gt=0, description="Transaction amount")
    proxytype: Literal["TYPE1", "TYPE2", "TYPE3"] = Field(..., description="Proxy type")
    
    

@app.post("/transaction")
async def create_transaction(payload: TransactionPayload):
    """
    Accept a transaction payload and return it for confirmation.
    """
    # Example logic: you could save to DB or send to another service
    response = {
        "status": "success",
        "txn_id": payload.txn_id,
        "cif": payload.cif,
        "amount": payload.amount,
        "proxytype": payload.proxytype
    }
    return response