from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # ✅ 新增這行
from pydantic import BaseModel
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# ✅ 加入 CORS 中介層（允許跨來源請求）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 可改成 ["https://你的網站.com"] 來限制安全範圍
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class QueryRequest(BaseModel):
    keyword: str

@app.post("/spark/search")
async def search_spark(request: QueryRequest):
    try:
        response = supabase.table("spark").select("*").ilike("content", f"%{request.keyword}%").execute()
        return {"results": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class AddSparkRequest(BaseModel):
    content: str
    tags: list[str] = []
    category: list[str] = []
    status: str = "草稿"

@app.post("/spark/add")
async def add_spark(data: AddSparkRequest):
    try:
        response = supabase.table("spark").insert({
            "content": data.content,
            "tags": data.tags,
            "category": data.category,
            "status": data.status
        }).execute()
        return {"message": "Spark added", "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

