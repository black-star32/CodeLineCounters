# coding:utf-8
import click

from CodeLineCounters.models import db
from CodeLineCounters.models.user import Users
from CodeLineCounters.models.record import Record

def initdb(drop=None):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息

if __name__ == '__main__':
    initdb(drop=True)
