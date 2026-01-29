from sqlalchemy import create_engine 
from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:6010@localhost:5432/postgres"
db = create_engine(db_connection_string)

# def test_db_connection():#Получить список таблиц
# 	names = db.table_names()
# 	assert names[1] == 'species'#первая таблица
# 	assert names[2] == 'places'#вторая таблица	
   
# def test_places():#Получить строки из таблицы: places
#     rows = db.execute("SELECT * FROM places").fetchall()
#     print(rows)
#     row1 = rows[0]

#     assert row1[0] == 1
#     assert row1["place_name"] == "дом"

# def test_insert():#Добавиv places(места)
#     sql = text("INSERT INTO company(\"name\") VALUES (:new_name)")     
#     rows = db.execute(sql, new_name = 'Directum RX')

def test_insert_place_simple():#добавление места
    # 1. Получаем следующий ID
    sql_max = text("SELECT COALESCE(MAX(place_id), 0) + 1 FROM places")
    next_id_result = db.execute(sql_max).fetchone()
    next_id = next_id_result[0]
    
    # 2. Вставляем запись
    sql_insert = text("""
        INSERT INTO places (place_id, place_name) 
        VALUES (:place_id, :place_name)
        RETURNING place_id
    """)
    
    result = db.execute(sql_insert, place_id=next_id, place_name='Работа')
    new_id = result.fetchone()[0]
    
    # 3. Проверяем
    sql_check = text("SELECT place_name FROM places WHERE place_id = :id")
    check_result = db.execute(sql_check, id=new_id).fetchone()
    
    assert check_result['place_name'] == 'Работа'
    
    # 4. Очищаем 
    sql_delete = text("DELETE FROM places WHERE place_id = :id")
    db.execute(sql_delete, id=new_id)

def test_update():# Обновить места
    sql_max = text("SELECT COALESCE(MAX(place_id), 0) + 1 FROM places")
    next_id_result = db.execute(sql_max).fetchone()
    next_id = next_id_result[0]
    
    sql_insert = text("""
        INSERT INTO places (place_id, place_name) 
        VALUES (:place_id, :place_name)
        RETURNING place_id
    """)
    
    result = db.execute(sql_insert, place_id=next_id, place_name='Каторга')
    new_id = result.fetchone()[0]

    #обновляем
    sql = text("UPDATE places SET place_name = :new_place_name WHERE place_id = :place_id")
    rows = db.execute(sql, new_place_name = 'Офис', place_id = next_id)
    
    #Очищаем
    sql_delete = text("DELETE FROM places WHERE place_id = :id")
    db.execute(sql_delete, id=new_id)

def test_delete():#Удалуние места:
   # 1. Получаем следующий ID
    sql_max = text("SELECT COALESCE(MAX(place_id), 0) + 1 FROM places")
    next_id_result = db.execute(sql_max).fetchone()
    next_id = next_id_result[0]
    
    # 2. Вставляем запись
    sql_insert = text("""
        INSERT INTO places (place_id, place_name) 
        VALUES (:place_id, :place_name)
        RETURNING place_id
    """)
    
    result = db.execute(sql_insert, place_id=next_id, place_name='Магазин')
    new_id = result.fetchone()[0]

    sql_delete = text("DELETE FROM places WHERE place_id = :id")
    db.execute(sql_delete, id=new_id)