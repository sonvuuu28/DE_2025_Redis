import csv
import pymysql

# Kết nối MySQL
conn = pymysql.connect(
    host="localhost", port=3307, user="root", password="123", database="grab"
)
cursor = conn.cursor()

# Đọc CSV và insert
with open("../docker/mysql/data/drivers.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute(
            """
            INSERT INTO drivers (id, full_name, latitude, longitude)
            VALUES (%s, %s, %s, %s)
        """,
            (row["id"], row["full_name"], row["latitude"], row["longitude"]),
        )

conn.commit()
cursor.close()
conn.close()
