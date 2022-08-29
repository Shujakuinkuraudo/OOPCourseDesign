from waitress import serve
from flask import Flask, render_template, request, redirect
import utils
import re
# 创建程序
# web应用程序
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("seg.html")


@app.route('/seg', methods=['POST', 'GET'])
def login():
    string = request.form.get('string')
    core = request.form.get('core')
    seg = ""
    posseg = ""
    if string:
        text = re.sub("\\r", "", string)
        text = text.split('\n')
        count = 0
        for sentence in text:
            count += 1
            if sentence:
                seg += "line" + str(count) + "   "
                posseg += "line" + str(count) + "   "
                SegTool = eval(f"utils.SegTools.{core}")
                Textposseg, TestTextSplit, TestPOSSplit = SegTool(sentence)
                for i in range(len(TestTextSplit)):
                    seg += f"{TestTextSplit[i]} "
                    posseg += f"{TestTextSplit[i]}\\{TestPOSSplit[i]} "
                seg += "\r\n"
                posseg += "\r\n"
    return render_template('seg.html', posseg=posseg, original=string, seg=seg)
    # return render_template('test.html',msg = "登录失败！")


serve(app, host="0.0.0.0", port=5000)
