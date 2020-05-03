# coding:utf-8
import pymysql
from setting import config

def connect():
    conn = config.POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    return conn, cursor

def connect_close(conn, cursor):
    cursor.close()
    conn.close()

def fetch_all(sql, args):
    conn,cursor = connect()
    cursor.execute(sql, args)
    result = cursor.fetchall()
    connect_close(conn, cursor)

    return result


def fetch_one(sql, args):
    conn,cursor = connect()
    cursor.execute(sql, args)
    result = cursor.fetchone()
    connect_close(conn, cursor)

    return result


def insert(sql, args):
    conn,cursor = connect()
    row = cursor.execute(sql, args)
    conn.commit()
    connect_close(conn, cursor)

    return row
