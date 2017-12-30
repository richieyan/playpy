# -*- coding: utf-8 -*-

from contextlib import contextmanager
from itertools import cycle
import time
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import sessionmaker

master_engine = create_engine(
    'mysql+mysqldb://root@localhost:3306/blog?charset=utf8', echo=False,
    pool_size=2, max_overflow=48,
    pool_timeout=0, pool_recycle=3600)
MasterSession = sessionmaker(bind=master_engine)

@contextmanager
def create_mysql_client(master=False, expire_on_commit=False):
    session = MasterSession(expire_on_commit=expire_on_commit, autoflush=False)
    session.execute('SET innodb_lock_wait_timeout = 1')
    try:
        yield session
    except DBAPIError as e:
        logging.exception("mysql error")
    finally:
        session.close()
        session.connection().close()

def main():
    with create_mysql_client(True) as session:
        print('session 1 start')
        time.sleep(15)
        print('session 1 ----------->done')
    print('next sleep........')
    time.sleep(10)
    print('next session--------->')
    with create_mysql_client(True) as session:
        print('session2----->')
        time.sleep(15)
    print('session2 done---->')
    time.sleep(10)

if __name__ == '__main__':
    main()
