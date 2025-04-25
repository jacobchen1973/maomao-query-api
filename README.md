# MaoMao Query API

這是一個為「毛毛語言查詢系統 v1.0」設計的 FastAPI 應用程式，負責處理語意查詢與 Supabase 整合。

## 功能包含：
- 查詢火花內容（/spark/search）
- 新增火花資料（/spark/add）
- 支援標籤與分類系統
- 未來可擴充語意分析、Notion 整合、Webhook 觸發

## 部署環境：
- Python 3.11
- FastAPI
- supabase-py
- Docker + Render

## 環境變數（.env）設定：
```
SUPABASE_URL=你的 supabase 專案網址  
SUPABASE_KEY=你的 anon key
```

## 啟動方式（本機端）：
```
uvicorn main:app --reload --port 8000
```

---

✨ 作者：@jacobchen1973（aka 群之）
