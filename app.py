from flask import Flask, render_template, request
import funcs
import json

app = Flask(__name__)

@app.route('/')
def index():
    stats = {'data':{
        'confirmed': '-',
        'recovered': '-',
        'deaths': '-',
        'active': '-'},
        'dt': '-'
    }
    location = "World Wide"
    if len(request.args) == 0 or request.args.get('country')=="worldwide":
        # print(funcs.getCaseWorldWide())
        stats = funcs.getCaseWorldWide()
    else:
        country_name = request.args.get('country')
        stats = funcs.getCaseCountry(country_name)
        if "error" in stats:
            return render_template("errormsg.html")
        location = stats['location']
    # print(stats)
    confirmedc = funcs.addCommas(str(stats['confirmed']))
    deathsc = funcs.addCommas(str(stats['deaths']))
    # print("deathsc:", deathsc)
    activec = funcs.addCommas(str(stats['active']))
    recoveredc = funcs.addCommas(str(stats['recovered']))
    last_updated = stats['lastUpdate']
    # --------------------------------------------------
    goodNews = funcs.getTenGoodNews()
    return render_template("index.html",
        location = location,
        confirmedc = confirmedc,
        deathsc = deathsc,
        recoveredc = recoveredc,
        activec = activec,
        last_updated = last_updated,
        goodNews = goodNews)

@app.route('/motivationabout/')
def motivationabout():
    return render_template("motivationabout.html")

if __name__ == "__main__":
    app.debug = True
    app.run()