# You'll need to install PyJWT via pip 'pip install PyJWT' or your project packages file

import jwt
import time

METABASE_SITE_URL = "https://drive.google.com/file/d/1ibdMShZnRF0USkiAqMCmT7h7RM0T92I8/view?usp=sharing"
METABASE_SECRET_KEY = "30e4d730302471dd9c8fc99b70ca4e7bbb08aeb32f06f2bff4710ae26b2b72d4"

payload = {
  "resource": {"dashboard": 2},
  "params": {
    
  },
  "exp": round(time.time()) + (60 * 10) # 10 minute expiration
}
token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token +
  "#bordered=true&titled=true"