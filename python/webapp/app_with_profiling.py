from flask import Flask, render_template, request
import cProfile
from functools import wraps
import pstats

app = Flask(__name__)
app.config.from_object(__name__)

def profiling():

    def _profiling(f):
        @wraps(f)
        def __profiling(*rgs, **kwargs):
            pr = cProfile.Profile()
            pr.enable()

            result = f(*rgs, **kwargs)

            pr.disable()
            # save stats into file
            pr.dump_stats('profile_dump')
            p = pstats.Stats('profile_dump')
            # skip strip_dirs() if you want to see full path's
            p.strip_dirs().print_stats()

            return result
        return __profiling
    return _profiling

@app.route('/')
@profiling()
def welcome():
    return render_template('calculator.html')


@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        result = var_1 + var_2
    elif(operation == 'Subtraction'):
        result = var_1 - var_2
    elif(operation == 'Multiplication'):
        result = var_1 * var_2
    elif(operation == 'Division'):
        result = var_1 / var_2
    else:
        result = 'INVALID CHOICE'
    entry = result
    return render_template('render.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)