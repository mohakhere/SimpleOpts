from flask import Flask, render_template, request


app = Flask(__name__, template_folder='template')
app.debug = True
@app.route('/', methods=['GET', 'POST'])
def primes():
    if request.method == 'POST':
        n = int(request.form['number'])
        primelist = []
        for u in range(1, n+1):
            if u > 1:
                for i in range(2, u):
                    if (u % i) == 0:
                        break
                else:
                    primelist.append(u)
        return render_template('primes.html', primes=primelist)
    else:
        return render_template('primes.html')
# handling errors: "rescures" to be added!
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

y = 3
if x>8:
    primes()
else:
    return y

if __name__ == '__main__':
    app.run()
