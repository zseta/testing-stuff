import json
import psycopg2
import psycopg2.extras
import os

def lambda_handler(event, context):
    
    db_name = os.environ['DB_NAME']
    db_user = os.environ['DB_USER']
    db_host = os.environ['DB_HOST']
    db_port = os.environ['DB_PORT']
    db_pass = os.environ['DB_PASS']
    
    conn = psycopg2.connect(user=db_user, database=db_name, host=db_host, 
                            password=db_pass, port=db_port)
    
    sql = "SELECT * FROM stocks_intraday WHERE symbol = 'MSFT' ORDER BY time DESC LIMIT 1"
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cursor.execute(sql)
    
    result = cursor.fetchall()
    list_of_dicts = []
    for row in result:
        list_of_dicts.append(dict(row))
    
    return {
        'statusCode': 200,
        'body': json.dumps(list_of_dicts, default=str),
        'headers': {
            "Content-Type": "application/json"
        }
    }