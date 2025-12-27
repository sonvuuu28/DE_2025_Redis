from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import redis
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------- MySQL --------
def get_connection_mysql():
    return mysql.connector.connect(
        host="127.0.0.1", port=3307, user="root", password="123", database="grab"
    )


def query_drivers_mysql():
    conn = get_connection_mysql()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM drivers;")
    columns = [col[0] for col in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return results


@app.get("/mysql/test")
def test_mysql():
    conn = get_connection_mysql()
    cursor = conn.cursor()
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    conn.close()
    return {"status": "ok", "time": str(result[0])}


@app.get("/mysql/get_drivers")
def get_drivers_mysql():
    return query_drivers_mysql()


# -------- Redis --------
r = redis.Redis(host="localhost", port=6379, db=0, password="123")


import decimal


@app.get("/redis/get_drivers")
def get_drivers_redis():
    cache = r.get("drivers")
    if cache:
        return json.loads(cache)
    data = query_drivers_mysql()
    r.set(
        "drivers",
        json.dumps(
            data, default=lambda x: float(x) if isinstance(x, decimal.Decimal) else x
        ),
        ex=60,
    )
    return data
