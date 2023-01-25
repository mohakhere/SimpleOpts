# find prime numbers in a range
# Take a value from user, until which the prime numbers will be given
# n = int(input("Enter the number: "))
# for u in range(1, n+1):
#     if u > 1:
#         for i in range(2, u):
#             if (u % i) == 0:
#                 break
#         else:
#             print(u)
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

if __name__ == '__main__':
    app.run()