from requests import get, post, put, delete


post('http://127.0.0.1:5000/post',
           json={
  "meta": {
    "locale": "ru-RU",
    "timezone": "UTC",
    "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
    "interfaces": {
      "screen": {},
      "payments": {},
      "account_linking": {}
    }
  },
  "session": {
    "message_id": 0,
    "session_id": "30fa20d4-d895-4fc0-b22c-81e63c325c06",
    "skill_id": "b490873b-daf7-441f-82ff-c19489daae66",
    "user_id": "D0288F4FE1254A72C67A03B843F8BFAFBC1789A7F0ED48011C464F00A5425484",
    "new": True
  },
  "request": {
    "command": "fgbhnjmk",
    "original_utterance": "fgbhnjmk",
    "nlu": {
      "tokens": [
        "fgbhnjmk"
      ],
      "entities": []
    },
    "markup": {
      "dangerous_context": False
    },
    "type": "SimpleUtterance"
  },
  "version": "1.0"
}).json()
