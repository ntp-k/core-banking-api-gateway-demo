from fastapi import FastAPI
from datetime import datetime, timezone, timedelta

app = FastAPI(title="New Core Banking API")

@app.get("/")
def root():
    return {"message": "New Core Banking API is running."}

@app.get("/accounts/{account_id}/balance")
def get_balance(account_id: str = "123456789"):
    bangkok_tz = timezone(timedelta(hours=7))
    acct = account_id.ljust(9, '0')

    res = {
    "code": "00",
    "msg": "SUCCESS",
    "acctId": acct,
    "availBal": 10500.99,
    "curr": "THB",
    "lastUpd": datetime(
        2026, 2, 6, 15, 30, 0,
        tzinfo=bangkok_tz
    ).isoformat(),
    "coreId": "NEW"
}

    print('Response:', res)
    return res

# EOF
