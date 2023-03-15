from flask import Flask, request, Response
from captcha import Solver

app = Flask(__name__)


@app.route("/solve", methods=['POST'])
async def solveRoute():
    try:
        solver = Solver(request.get_json()["imageBase64"])

        result = await solver.solve()

        return result
    except:
        return Response(status=500)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2132)
