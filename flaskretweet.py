from flask import Flask,render_template,request

from bot import *
from usuarios import *

app = Flask(__name__)


def identify_bot(user,ck,cs,at,atc):
    global the_bot
    the_bot = Bot(user,ck,cs,at,atc)
    wordToFilter = the_bot.botname
    return wordToFilter,user


@app.route("/")
def hello():
    return render_template('login.html')


@app.route("/login",methods=['POST'])
def imprime():
    opcion1 = request.form['opcion1']
    opcion2 = request.form['opcion2']

    if ((opcion1=='SEGOB') and (opcion2=='veracruz123')):

        return render_template("profile.html",opcion1=opcion1)
    else:

        return render_template('error.html')



@app.route("/profile",methods=['POST'])
def retweet_me():
    #identifica
    user, ck, cs, at, atc = [line.rstrip('\n') for line in open('my_twitter_info.txt', 'r')]
    wordToFilter, user = identify_bot(user, ck, cs, at, atc)
    global botname
    botname = user
    #fin identifica

    tweet_id = request.form['tweet_id']
    retrived_tweet = the_bot.get_tweet_by_id(tweet_id)
    texto=retrived_tweet.text
    usuario_id=int(request.form['usuario_id'])

    if usuario_id == 1:
        agustin_paez.api.retweet(tweet_id)
        return render_template("profile.html", tweet_id=texto, usuario_id='retuiteando agustin_paez')

    elif usuario_id == 2:
        dani_mar2343.api.retweet(tweet_id)
        print("dani_mar2343  retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 3:
        edgar_s3212.api.retweet(tweet_id)
        print("edgar_s3212 retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        #      elif usuario_id == '4':
        #          vercomunica.api.retweet(tweet_id)
        #          print("vercomunica retuiteando")

    elif usuario_id == 4:
        silvia_gut1.api.retweet(tweet_id)
        print("silvia_gut1 retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 5:
        karla_truji.api.retweet(tweet_id)
        print("karla_truji retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 6:
        la_basicamente.api.retweet(tweet_id)
        print("la_basicamente retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 7:
        agustin_mac.api.retweet(tweet_id)
        print("agustin_mac retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 8:
        yol_tenorio.api.retweet(tweet_id)
        print("yol_tenorio retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 9:
        robledomartin.api.retweet(tweet_id)
        print("robledomartin retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        #       elif usuario_id == 10:
        #           adizan86.api.retweet(tweet_id)
        #           print("adizan86 retuiteando")

    elif usuario_id == 11:
        jor_moca.api.retweet(tweet_id)
        print("jor_moca retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 12:
        guz_nelly.api.retweet(tweet_id)
        print("guz_nelly retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 13:
        rodriguezbre81.api.retweet(tweet_id)
        print("rodriguezbre81 retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 14:
        Informativo_Ver.api.retweet(tweet_id)
        print("Informativo_Ver retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 15:
        SamsaraCervant.api.retweet(tweet_id)
        print("SamsaraCervant retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 16:
        odalys_mendoz.api.retweet(tweet_id)
        print("odalys_mendoz retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 17:
        prinzoeherrera.api.retweet(tweet_id)
        print("prinzoeherrera retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 18:
        greta_reyes21.api.retweet(tweet_id)
        print("greta_reyes21 retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 19:
        PamyRoche.api.retweet(tweet_id)
        print("PamRoche retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 20:
        GleyFernando.api.retweet(tweet_id)
        print("GleyFernando retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 21:
        ArrolloRodolfo.api.retweet(tweet_id)
        print("ArrolloRodolfo retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 22:
        EpicentroVer.api.retweet(tweet_id)
        print("EpicentroVer retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 23:
        armandoferrarif.api.retweet(tweet_id)
        print("armandoferrarif retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 24:
        leocasol.api.retweet(tweet_id)
        print("leocasol retuiteando")
        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

    elif usuario_id == 25:
        try:
            agustin_paez.api.retweet(tweet_id)
            print("agustin_paez retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en agustin_paez ")
            pass
        time.sleep(60)

        try:
            dani_mar2343.api.retweet(tweet_id)
            print("dani_mar2343 retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en dani_mar2343 ")
            pass
        time.sleep(60)

        try:
            edgar_s3212.api.retweet(tweet_id)
            print("edgar_s3212 retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en edgar_s3212 ")
            pass
        time.sleep(60)
        #  try:
        #    vercomunica.api.retweet(tweet_id)
        #    print("vercomunica retuiteando")
        #  except Exception as e:
        #    print("EXCEPTION :(", e)
        #    print("error en vercomunica ")
        #    pass
        #  time.sleep(120)
        try:
            silvia_gut1.api.retweet(tweet_id)
            print("silvia_gut1 retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en silvia_gut1 ")
            pass
        time.sleep(60)
        try:
            karla_truji.api.retweet(tweet_id)
            print("karla_truji retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en karla_truji ")
            pass
        time.sleep(60)
        try:
            la_basicamente.api.retweet(tweet_id)
            print("la_basicamente retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en la_basicamente ")
            pass
        time.sleep(60)
        try:
            agustin_mac.api.retweet(tweet_id)
            print("agustin_mac retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en agustin_mac ")
            pass
        time.sleep(60)
        try:
            yol_tenorio.api.retweet(tweet_id)
            print("yol_tenorio retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en yol_tenorio ")
            pass
        time.sleep(60)
        try:
            robledomartin.api.retweet(tweet_id)
            print("robledomartin retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en robledomartin ")
            pass
        time.sleep(60)
        try:
            adizan86.api.retweet(tweet_id)
            print("adizan86 retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en adizan86 ")
            pass
        time.sleep(60)
        try:
            jor_moca.api.retweet(tweet_id)
            print("jor_moca retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en jor_moca ")
            pass
        time.sleep(60)
        try:
            guz_nelly.api.retweet(tweet_id)
            print("guz_nelly retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en guz_nelly ")
            pass
        time.sleep(60)
        try:
            rodriguezbre81.api.retweet(tweet_id)
            print("rodriguezbre81 retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en rodriguezbre81 ")
            pass
        time.sleep(60)
        try:
            Informativo_Ver.api.retweet(tweet_id)
            print("Informativo_Ver retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en Informativo_Ver ")
            pass
        time.sleep(60)
        try:
            SamsaraCervant.api.retweet(tweet_id)
            print("SamsaraCervant retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en SamsaraCervant ")
            pass
        time.sleep(60)
        try:
            odalys_mendoz.api.retweet(tweet_id)
            print("odalys_mendoz retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en odalys_mendoz ")
            pass
        time.sleep(60)
        try:
            prinzoeherrera.api.retweet(tweet_id)
            print("prinzoeherrera retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en prinzoeherrera ")
            pass
        time.sleep(120)
        try:
            greta_reyes21.api.retweet(tweet_id)
            print("greta_reyes21 retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en greta_reyes21 ")
            pass
        time.sleep(120)

        try:
            PamyRoche.api.retweet(tweet_id)
            print("PamyRoche retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)

        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en PamRoche ")
            pass
        time.sleep(120)

        try:
            GleyFernando.api.retweet(tweet_id)
            print("GleyFernando retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)


        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en GleyFernando ")
            pass
        time.sleep(120)

        try:
            ArrolloRodolfo.api.retweet(tweet_id)
            print("ArrolloRodolfo retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)


        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en ArrolloRodolfo ")
            pass
        time.sleep(120)

        try:
            EpicentroVer.api.retweet(tweet_id)
            print("EpicentroVer retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)


        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en EpicentroVer ")
            pass
        time.sleep(120)

        try:
            armandoferrarif.api.retweet(tweet_id)
            print("armandoferrarif retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)


        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en armandoferrarif ")
            pass
        time.sleep(120)

        try:
            leocasol.api.retweet(tweet_id)
            print("leocasol retuiteando")
            return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)


        except Exception as e:
            print("EXCEPTION :(", e)
            print("error en leocasol ")
            pass
        time.sleep(120)

        return render_template("profile.html", tweet_id=texto, usuario_id=usuario_id)


if __name__ == "__main__":
    app.run()