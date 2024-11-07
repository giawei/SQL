#%%
import mysql.connector
def connect_to_database(host, user, password, database):
    """
    建立並返回 MySQL 資料庫的連接與游標。

    參數:
        host (str): 資料庫伺服器的主機名稱
        user (str): 使用者名稱
        password (str): 使用者密碼
        database (str): 資料庫名稱

    回傳:
        tuple: 包含資料庫連接物件與 cursor 物件
    """
    try:
        # 建立資料庫連接
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # 建立 cursor
        cursor = connection.cursor()
        
        print("Successfully connected to the database.")
        
        return connection, cursor

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None

def close_database_connection(connection, cursor):
    """
    關閉給定的 cursor 和資料庫連接。

    參數:
        connection: 資料庫連接物件
        cursor: cursor 物件
    """
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Database connection closed.")

def show_tables(cursor):
    """
    使用提供的 cursor 列出資料庫中的所有表格名稱。

    參數:
        cursor: cursor 物件，用於執行 SQL 查詢
    """
    try:
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor]
        
        print("Tables in the database:")
        for table_name in tables:
            print(table_name)
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def show_table_data(table_name):
    """
    顯示Table的資料

    參數:
        table_name: 要查詢的表格名稱
    回傳:
        list

    """
    cursor.execute(f"SELECT * FROM {table_name}")
    table_datas = cursor.fetchall()
    return table_datas


def get_columns(table_name):
    """
    查詢Table表格名稱

    參數:
        table_name: 查詢table名稱
    回傳:
        list
    """
    # 執行查詢來獲取表格結構
    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    # 取得結果並列印欄位名稱
    columns = cursor.fetchall()  # 取得所有欄位資訊
    column_names = [column[0] for column in columns]  # 提取欄位名稱
    return column_names

#將col_name中等於col1_value的col2_name的值更新成new value
def update_column_value(table_name, col1_name, col1_value, col2_name, col2_new_value):
    """
    參數:
        table_name: 表格名稱
        col1_name: 找尋的column
        col1_value:找尋的column value
        col2_name:要被更改的column
        col2_new_value: 被更改的值
    """
    # 構建 SQL 更新語句
    update_query = f"""
    UPDATE {table_name}
    SET {col2_name} = %s
    WHERE {col1_name} = %s
    """
    # 執行更新
    cursor.execute(update_query, (col2_new_value, col1_value))

    # 提交變更
    connection.commit()

    # 顯示更新的記錄數
    print(f"更新了 {cursor.rowcount} 條記錄")


# 範例用法
host = "localhost"
user = "root"
password = "00000000"
database = "sql_t"

# 建立資料庫連接
connection, cursor = connect_to_database(host, user, password, database)
#%%
# 顯示表格名稱（如果連接成功）
if connection and cursor:
    show_tables(cursor)

#%%
# 關閉資料庫連接
close_database_connection(connection, cursor)
