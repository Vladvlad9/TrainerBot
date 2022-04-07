from sqlalchemy.future import select
from sqlalchemy.orm import Session

from utils.db_api.loader import engine
from utils.db_api.models import Users


class UsersCrud(object):
    @staticmethod
    def add_user(id_user: int, name: str):
        with Session(binds=engine) as sessions:
            sessions.execute(
                Users(
                    id_user=id_user,
                    name=name
                )
            )
            sessions.commit()
