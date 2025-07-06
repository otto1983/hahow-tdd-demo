# 會用來抓取版面的名稱
#會先進行呼叫，讓他亮紅燈
from main import get_ptt_boards, insert_ptt_board
from models import Board #import一個資料模型

# 根據ＴＤＤ開發方式，需要先準備測試資料
def test_get_ptt_boards():
    expected = "Stock" # Stock是ＰＴＴ版面名稱

    result = get_ptt_boards() # get_ptt_boards這邊就可以理解成會回傳一個充滿版面名稱的list
    print(result) # 把result print 出來

    # 這邊先寫驗證，預期expected這個字串應該要在result內
    assert expected in result


def test_insert_ptt_board(sqlite_session):
    expected = "test"

    insert_ptt_board(name=expected, session=sqlite_session)

    assert sqlite_session.query(Board).first().name == expected #直接透過查詢的方法查詢board這個資料表的第一個，接著直接驗證name這個欄位是不是等於預期的資料