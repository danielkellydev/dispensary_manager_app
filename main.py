import json

dispensary_items = {
    1001: {"herb": "bai zhu", "grams": 230},
    1002: {"herb": "fu ling", "grams": 150},
    1003: {"herb": "zhi gan cao", "grams": 330},
    1004: {"herb": "huang qin", "grams": 430},
    1005: {"herb": "fu zi", "grams": 110},
    1006: {"herb": "huang lian", "grams": 235},
    1007: {"herb": "gan jiang", "grams": 112},
    1008: {"herb": "ren shen", "grams": 80},
    1009: {"herb": "ban xia", "grams": 45},
    1010: {"herb": "bai shao", "grams": 324},
    1011: {"herb": "gui zhi", "grams": 334},
    1012: {"herb": "da zao", "grams": 26},
}

js = json.dumps(dispensary_items)
js

fd= open("data.json", 'w')

fd.write(js)
fd.close()