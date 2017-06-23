from sqlalchemy import Boolean, Column, DateTime, BigInteger
from sqlalchemy import MetaData, String, Table

def define_tables(meta):
    # 定义一个 Table 对象
    blog_category = Table(
        "Blog_category", meta,
        Column("category_id", String(length=50),primary_key=True),
        Column("category_name", String(20), unique=True),
        Column("category_degree", int),
        Column("creat_date", DateTime),
        Column("category_child", String(150)),)

    return blog_category


def upgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    # create all tables
    # Take care on create order for those with FK dependencies
    table = define_tables(meta)
    try:
        table.create()
    except Exception:
        # LOG.info(_LE('Exception while creating table.'))
        raise


def downgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine
    table = define_tables(meta)
    table.reverse()
    table.drop()