from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/data_model.html')  # Adicione esta rota para a página data_model.html
def data_model():
    return render_template('data_model.html')

@app.route('/skeleton.html')  # Adicione esta rota para a página data_model.html
def skeleton():
    return render_template('skeleton.html')

@app.route('/compare.html')  # Adicione esta rota para a página data_model.html
def compare():
    return render_template('compare.html')




if __name__ == '__main__':
    app.run(debug=True)
