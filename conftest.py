# conftest 檔案用來存放fixture
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models import Base

# 這邊會仿照第二章的方式寫一個in_memory的SQLie 的 session
# 會作為fixture直接用來測試資料庫的寫入
@pytest.fixture(name="sqlite_session")
def sqlite_session_fixture() -> Session:
    engine_url = "sqlite://"
    engine = create_engine(engine_url)

    Base.metadata.create_all(engine)

    with sessionmaker(bind=engine)() as session:
        yield session

    Base.metadata.drop_all(engine)