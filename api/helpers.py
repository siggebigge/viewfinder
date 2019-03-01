from db.models import User


def set_up_tables():
    """
    Warning: Drops existing tables and recreates database
    """
    if User.table_exists():
        User.drop_table()

    User.create_table()
