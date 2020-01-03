# coding=utf-8
from flask import Flask, jsonify, request
import os
app = Flask(__name__)
print(os.getcwd())
flask_conf_file = os.path.join(os.getcwd(), 'conf', 'flask_conf.cfg')
mail_file = os.path.join(os.getcwd(), 'data', 'personal_info.csv')
app.config.from_pyfile(flask_conf_file)


@app.route('/', methods=['GET'])
def hello():
    result_dict = {}
    mail_address_list = []
    target_prefecture = request.args.get('pref')
    with open(mail_file, 'r') as inf:
        for low_num, line in enumerate(inf):
            if low_num == 0:  # header
                continue
            line = line.rstrip()
            vals = line.split(',')
            mail_add, sex, age, name, prefecture = vals
            if prefecture == target_prefecture:
                mail_address_list.append(mail_add)

    result_dict['mail_address_list'] = mail_address_list
    return jsonify(result_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # 最終的にはここは消す。以下の手順でアプリケーションを起動する。
    # export FLASK_APP=app.py
    # python -m flask run --host=0.0.0.0 --port=3000
