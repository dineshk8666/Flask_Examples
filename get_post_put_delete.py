from flask import Flask, jsonify, request
app = Flask(__name__)

languages = [{"name":"java"}, {"name": "python"}, {"name":"ruby"}]

@app.route('/', methods=["GET"])
def ServerStatus():
    return jsonify({"message":"Server is up!"})

@app.route('/lang', methods=["GET"])
def returnAll():
    return jsonify({"languages": languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    lang=[language for language in languages if language['name'] == name]
    return jsonify({'language':lang[0]})

@app.route('/lang', methods=['POST'])
def addOne():
    json = request.get_json(force=True)
    language = {'name': json['name']}
    languages.append(language)
    return jsonify({"languages":languages})

@app.route('/lang/<string:name>', methods=["PUT"])
def updateOne(name):
    langs = [language for language in languages if language['name'] == name]
    json = request.get_json(force=True)
    print json
    langs[0]['name']=json['name']
    return jsonify({'language':langs[0]})

@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
    lang = [language for language in languages if language['name'] == name]
    languages.remove(lang[0])
    return jsonify({'languages': languages})

if __name__ == '__main__':
    app.run(debug=True, host="192.168.33.20")
