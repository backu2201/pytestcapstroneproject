import pytest, datetime, pytz
@pytest.fixture(autouse=True)
def getdateandtime():
    print(datetime.datetime.now(pytz.timezone('Asia/kolkata')))
