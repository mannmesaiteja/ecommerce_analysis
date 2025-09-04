import mysql.connector as mc
import db_config

def get_connection():
    try:
        return mc.connect(
            host=db_config.db_host,
            user=db_config.db_user,
            password=db_config.db_password,
            database=db_config.db_name
        )
    except Exception as e:
        print("Mysql connection error")
        return {"msg": f'Mysql connection error: {str(e)}'}
