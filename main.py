

import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from models import Board
from datetime import datetime

# 寫一個function
def get_ptt_boards():
    url = "http://www.ptt.cc/bbs/index.html"

    resp = requests.get(url=url) #用requests來呼叫
    soup = BeautifulSoup(resp.text, "lxml")

    result = []
    for tmp in soup.find_all(name="div", attrs={"class": "board-name"}):
        result.append(tmp.text)

    return result #用return來回傳版面的名稱


#先建立一個空的function
def insert_ptt_board(name: str, session: Session):
    board = Board(
        name=name,
        created_time=datetime.now()
    )
    session.add(board)