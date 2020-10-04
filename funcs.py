import requests
import json

# BASE_URL = "https://covid2019-api.herokuapp.com/"
BASE_URL = "https://covid19.mathdro.id/api"
SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key=AIzaSyBIW5uhggFIcZGBinkl8X2JUySI7S5HKjg&cx=2f08ca55844d8d1d8&q=good+news+on+covid+2020+happy&lr=lang_en&start=0&num=10&excludeTerms=Stephanapoulos"
cases = ["confirmed","recovered", "deaths", "active"]
countries = {"AF":"Afghanistan", "AX":"Aland Islands","AL":"Albania","DZ":"Algeria","AS":"American Samoa","AD":"Andorra",
"AO":"Angola","AI":"Anguilla","AQ":"Antarctica","AG":"Antigua and Barbuda","AR":"Argentina","AM":"Armenia",
"AW":"Aruba","AU":"Australia","AT":"Austria","AZ":"Azerbaijan",
"BS":"Bahamas","BH":"Bahrain","BD":"Bangladesh","BB":"Barbados","BY":"Belarus","BE":"Belgium","BZ":"Belize","BJ":"Benin",
"BM":"Bermuda","BT":"Bhutan","BO":"Bolivia, Plurinational State of",
"BQ":"Bonaire, Sint Eustatius and Saba","BA":"Bosnia and Herzegovina","BW":"Botswana","BV":"Bouvet Island",
"BR":"Brazil","IO":"British Indian Ocean Territory","BN":"Brunei Darussalam","BG":"Bulgaria","BF":"Burkina Faso","BI":"Burundi",
"KH":"Cambodia","CM":"Cameroon","CA":"Canada","CV":"Cape Verde","KY":"Cayman Islands","CF":"Central African Republic","TD":"Chad","CL":"Chile",
"CN":"China","CX":"Christmas Island","CC":"Cocos (Keeling) Islands","CO":"Colombia","KM":"Comoros","CG":"Congo","CD":"Congo, The Democratic Republic of the","CK":"Cook Islands",
"CR":"Costa Rica","CI":"Côte d'Ivoire","HR":"Croatia","CU":"Cuba","CW":"Curaçao","CY":"Cyprus","CZ":"Czech Republic","DK":"Denmark","DJ":"Djibouti","DM":"Dominica",
"DO":"Dominican Republic","EC":"Ecuador","EG":"Egypt","SV":"El Salvador","GQ":"Equatorial Guinea","ER":"Eritrea","EE":"Estonia","ET":"Ethiopia",
"FK":"Falkland Islands (Malvinas)","FO":"Faroe Islands","FJ":"Fiji","FI":"Finland","FR":"France","GF":"French Guiana","PF":"French Polynesia","TF":"French Southern Territories","GA":"Gabon",
"GM":"Gambia","GE":"Georgia","DE":"Germany","GH":"Ghana","GI":"Gibraltar","GR":"Greece","GL":"Greenland","GD":"Grenada","GP":"Guadeloupe","GU":"Guam","GT":"Guatemala","GG":"Guernsey",
"GN":"Guinea","GW":"Guinea-Bissau","GY":"Guyana","HT":"Haiti","HM":"Heard Island and McDonald Islands",
"VA":"Holy See (Vatican City State)","HN":"Honduras","HK":"Hong Kong","HU":"Hungary","IS":"Iceland","IN":"India","ID":"Indonesia","IR":"Iran, Islamic Republic of","IQ":"Iraq","IE":"Ireland",
"IM":"Isle of Man","IL":"Israel","IT":"Italy","JM":"Jamaica","JP":"Japan","JE":"Jersey","JO":"Jordan","KZ":"Kazakhstan","KE":"Kenya","KI":"Kiribati","KP":"Korea, Democratic People's Republic of",
"KR":"Korea, Republic of","KW":"Kuwait","KG":"Kyrgyzstan","LA":"Lao People's Democratic Republic","LV":"Latvia","LB":"Lebanon","LS":"Lesotho","LR":"Liberia","LY":"Libya","LI":"Liechtenstein",
"LT":"Lithuania","LU":"Luxembourg","MO":"Macao","MK":"Macedonia, Republic of","MG":"Madagascar","MW":"Malawi","MY":"Malaysia","MV":"Maldives","ML":"Mali","MT":"Malta","MH":"Marshall Islands","MQ":"Martinique",
"MR":"Mauritania","MU":"Mauritius","YT":"Mayotte","MX":"Mexico","FM":"Micronesia, Federated States of","MD":"Moldova, Republic of","MC":"Monaco",
"MN":"Mongolia","ME":"Montenegro","MS":"Montserrat","MA":"Morocco","MZ":"Mozambique","MM":"Myanmar","NA":"Namibia","NR":"Nauru",
"NP":"Nepal","NL":"Netherlands","NC":"New Caledonia","NZ":"New Zealand","NI":"Nicaragua","NE":"Niger","NG":"Nigeria","NU":"Niue","NF":"Norfolk Island","MP":"Northern Mariana Islands","NO":"Norway","OM":"Oman","PK":"Pakistan","PW":"Palau",
"PS":"Palestinian Territory, Occupied","PA":"Panama","PG":"Papua New Guinea","PY":"Paraguay","PE":"Peru","PH":"Philippines","PN":"Pitcairn","PL":"Poland","PT":"Portugal",
"PR":"Puerto Rico","QA":"Qatar","RE":"Réunion","RO":"Romania","RU":"Russian Federation","RW":"Rwanda","BL":"Saint Barthélemy","SH":"Saint Helena, Ascension and Tristan da Cunha",
"KN":"Saint Kitts and Nevis","LC":"Saint Lucia","MF":"Saint Martin (French part)","PM":"Saint Pierre and Miquelon","VC":"Saint Vincent and the Grenadines",
"WS":"Samoa","SM":"San Marino","ST":"Sao Tome and Principe","SA":"Saudi Arabia","SN":"Senegal","RS":"Serbia","SC":"Seychelles","SL":"Sierra Leone",
"SG":"Singapore","SX":"Sint Maarten (Dutch part)","SK":"Slovakia","SI":"Slovenia","SB":"Solomon Islands","SO":"Somalia","ZA":"South Africa",
"GS":"South Georgia and the South Sandwich Islands","ES":"Spain","LK":"Sri Lanka","SD":"Sudan","SR":"Suriname","SS":"South Sudan","SJ":"Svalbard and Jan Mayen",
"SZ":"Swaziland","SE":"Sweden","CH":"Switzerland","SY":"Syrian Arab Republic","TW":"Taiwan, Province of China","TJ":"Tajikistan","TZ":"Tanzania, United Republic of",
"TH":"Thailand","TL":"Timor-Leste","TG":"Togo","TK":"Tokelau","TO":"Tonga","TT":"Trinidad and Tobago","TN":"Tunisia","TR":"Turkey","TM":"Turkmenistan",
"TC":"Turks and Caicos Islands","TV":"Tuvalu","UG":"Uganda","UA":"Ukraine","AE":"United Arab Emirates","GB":"United Kingdom","US":"United States","UM":"United States Minor Outlying Islands",
"UY":"Uruguay","UZ":"Uzbekistan","VU":"Vanuatu","VE":"Venezuela, Bolivarian Republic of","VN":"Viet Nam","VG":"Virgin Islands, British","VI":"Virgin Islands, U.S.","WF":"Wallis and Futuna",
"EH":"Western Sahara","YE":"Yemen","ZM":"Zambia","ZW":"Zimbabwe"}


def getCaseWorldWide():
    '''
        Getting # cases worldwide
    '''
    c = json.loads(requests.get(BASE_URL).text)
    # print(c)
    fin = {}
    fin["confirmed"] = c["confirmed"]["value"]
    fin["recovered"] = c["recovered"]["value"]
    fin["deaths"] = c["deaths"]["value"]
    fin["active"] = fin["confirmed"]-fin["recovered"]-fin["deaths"]
    fin["lastUpdate"] = c["lastUpdate"]
    return fin

def getCaseCountry(country):
    '''
        Getting # cases from country c
    '''
    full_url = "https://covid19.mathdro.id/api/countries/{}".format(country)
    c = json.loads(requests.get(full_url).text)
    # print("c:",c)
    if "error" in c:
        return c
    fin = {}
    fin["confirmed"] = c["confirmed"]["value"]
    fin["recovered"] = c["recovered"]["value"]
    fin["deaths"] = c["deaths"]["value"]
    fin["active"] = fin["confirmed"]-fin["recovered"]-fin["deaths"]
    fin["lastUpdate"] = c["lastUpdate"]
    fin["location"] = country
    if country in countries:
        fin["location"] = countries[country]
    return fin

def getTenGoodNews():
    res = json.loads(requests.get(SEARCH_URL).text)["items"]
    finres = []
    for r in res:
        print("finres this far:", len(finres))
        c = {}
        try:
            heading = r['title']
            if "Google Alerts" in heading:
                continue
        except:
            print("bummer")
            continue
        urlh = r['link']
        desc = ""
        try:
            desc = r['snippet']
        except:
            pass
        c['heading'] = heading
        c['url'] = urlh
        c['desc'] = desc
        finres.append(c)
    return finres

def addCommas(num):
    '''adding commas to numbers >999
        num is a string'''
    if len(num) > 3:
        lenwithc = len(num)//3
        if len(num)%3==0:
            lenwithc -=1
        for i in reversed(range(1,lenwithc+1)):
            ii = i*-3
            num = num[:ii]+","+num[ii:]
    return num

if __name__ == "__main__":
    # print(getTenGoodNews())
    # print(addCommas("255645643275"))
    # print(getCaseWorldWide())
    print(getCaseCountry('CD'))
