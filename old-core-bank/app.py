from fastapi import FastAPI, Response

app = FastAPI(title="Old Core Banking API (COBOL-style)")

@app.get("/")
def root():
    return {"message": "Old Core Banking API is running."}

@app.get("/BALINQ")
def balance_inquiry(ACCT_NO: str = "123456789"):
    acct = ACCT_NO.ljust(9)

    # 00 SUCCESS 123456789 00000001050000 THB 20260206153000 OLD
    response = (
        "00"                  # RESP_CODE (2)
        "SUCCESS"             # RESP_DESC (7)
        f"{acct}"             # ACCT_NO (9)
        "00000001050000"      # AVAIL_BAL (15, no decimal)
        "THB"                 # CURR (3)
        "20260206153000"      # LAST_UPD (yyyyMMddHHmmss)
        "OLD"                 # CORE_ID (3)
    )

    return Response(
        content=response,
        media_type="text/plain"
    )

# EOF
