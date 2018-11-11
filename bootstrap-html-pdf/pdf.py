from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)


@app.route("/")
def gen_custom_pdf():
    
    rendered = render_template('test.html',variable1='1112131415', variable2='12345678')
    
    pdf = pdfkit.from_string(rendered,False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf' 
    response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'
    return response


if __name__ == "__main__":
    app.run()
    
    
