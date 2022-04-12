from sqlalchemy import create_engine

from data.config import DATABASE

engine = create_engine(f'postgresql://postgres:postgres@localhost:5432/{DATABASE}')
