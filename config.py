import os

API_ID = API_ID =  20200825

API_HASH = os.environ.get("API_HASH", "7e7f93e266c390d9cc5c2bffbe921e36")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7186933202:AAH7yxM3KP14n6jnIJcd_MWMh9LSVVTEJYI")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1923922961))

LOG = -1001605524352,

UPDATE_GRP = -1002097681261,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1923922961").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


