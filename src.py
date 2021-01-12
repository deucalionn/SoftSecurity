import requests
import json
from fpdf import FPDF
from pynotifier import Notification



def create_report():

            
    Notification(
        title='SoftSecurity Notification',
        description='Test lancé ! ',
        icon_path='logo_dino.png',
        duration=2,
        urgency=Notification.URGENCY_CRITICAL
    ).send()


    #report total
    pdf_report = FPDF()
    pdf_report.add_page()
    pdf_report.set_font("Arial", size=15)


    #report global
    pdf_report_global = FPDF()
    pdf_report_global.add_page()
    pdf_report_global.set_font("Arial", size=15)


    
    p_site(pdf_report, pdf_report_global)




def getjson():
    with open("json.json", "r") as f:
        return json.load(f)






def p_site(pdf_report, pdf_report_global):
    #print("Lancement du test ...")
    pdf_report.cell(200,10, txt="STEP 1 : PORN SITE CONNEXION", ln=1, align="L")
    #print("STEP 1 : Porn site")
    with open("/home/deucalion/Documents/work_code/ids/json.json", "r") as f:
        obj = json.load(f)
    OBJ = obj["site"]
    total_p = len(OBJ)
    print(total_p)
    i = 0
    bloqued_p = 0
    result_porno = {}
    error_p = 0
    while i < total_p:
        try:
            r = requests.get(OBJ[i])
            if r.status_code == 200:
                result_porno[OBJ[i]] = 'Not Bloqued'
                pdf_report.cell(200,10, txt="{} : {}".format(result_porno[OBJ[i]], OBJ[i]), ln=1, align="L")
            elif r.status_code == 403:
                result_porno[OBJ[i]] = 'Bloqued'
                pdf_report.cell(200,10, txt="{} : {}".format(result_porno[OBJ[i]], OBJ[i]), ln=1, align="L")
                bloqued_p+=1
            else:
                result_porno[OBJ[i]] = 'Error'
                pdf_report.cell(200,10, txt="{} : {}".format(result_porno[OBJ[i]], OBJ[i]), ln=1, align="L")
                error_p+=1
        except:
            result_porno[OBJ[i]] == 'Can not create the request'
            pdf_report.cell(200,10, txt="{} : {}".format(result_porno[OBJ[i]], OBJ[i]), ln=1, align="L")
            error_p+=1
        i+=1
        
    #print("nombre de tentative bloqué : "+ str(bloqued_p))
    #for x in result_porno.items():
        #print(x)
    
    b_site(pdf_report, pdf_report_global, bloqued_p, total_p, error_p)


def b_site(pdf_report, pdf_report_global, bloqued_p, total_p, error_p):
    pdf_report.cell(200,10, txt="STEP 2 : BANK SITE CONNEXION", ln=1, align="L")
    #print("STEP 2 : Bank site")
    with open("/home/deucalion/Documents/work_code/ids/json.json", "r") as f:
        obj = json.load(f)
    OBJ = obj["bank"]
    total_b = len(OBJ)
    i = 0
    bloqued_b = 0
    result_bank = {}
    error_b = 0
    while i < total_b:
        try:
            r = requests.get(OBJ[i])
            if r.status_code == 200:
                result_bank[OBJ[i]] = 'Not Bloqued'
                pdf_report.cell(200,10, txt="{} : {}".format(result_bank[OBJ[i]], OBJ[i]), ln=1, align="L")
            elif r.status_code == 403:
                result_bank[OBJ[i]] = 'Bloqued'
                pdf_report.cell(200,10, txt="{} : {}".format(result_bank[OBJ[i]], OBJ[i]), ln=1, align="L")
                bloqued_b+=1
            else:
                result_bank[OBJ[i]] = 'Error'
                pdf_report.cell(200,10, txt="{} : {}".format(result_bank[OBJ[i]], OBJ[i]), ln=1, align="L")
                error_b+=1
        except:
            result_bank[OBJ[i]] == 'Can not create the request'
            pdf_report.cell(200,10, txt="{} : {}".format(result_bank[OBJ[i]], OBJ[i]), ln=1, align="L")
            error_b+=1
        i+=1
        
    #for x in result_bank.items():
        #print(x)

    m_site(pdf_report, pdf_report_global, bloqued_p, bloqued_b, total_p, total_b, error_p, error_b)



def m_site(pdf_report, pdf_report_global, bloqued_b, bloqued_p, total_p, total_b, error_p, error_b):
    pdf_report.cell(200,10, txt="STEP 3 : MALWARE SITE CONNEXION", ln=1, align="L")
    #print("STEP 3 : Malware site")
    with open("/home/deucalion/Documents/work_code/ids/json.json", "r") as f:
        obj = json.load(f)
    OBJ = obj["malware_site"]
    total_m = len(OBJ)
    i = 0
    bloqued_m = 0
    result_malware = {}
    error_m = 0
    while i < total_m:
        try:
            r = requests.get(OBJ[i])
            if r.status_code == 200:
                result_malware[OBJ[i]] = 'Not Bloqued'
                pdf_report.cell(200,10, txt="{} : {}".format(result_malware[OBJ[i]], OBJ[i]), ln=1, align="L")
            elif r.status_code == 403:
                result_malware[OBJ[i]] = 'Bloqued'
                pdf_report.cell(200,10, txt="{} : {}".format(result_malware[OBJ[i]], OBJ[i]), ln=1, align="L")
                bloqued_m+=1
            else:
                result_malware[OBJ[i]] = 'Error'
                pdf_report.cell(200,10, txt="{} : {}".format(result_malware[OBJ[i]], OBJ[i]), ln=1, align="L")
                error_m+=1
                        
        except:
            result_malware[OBJ[i]] == 'Can not create the request'
            pdf_report.cell(200,10, txt="{} : {}".format(result_malware[OBJ[i]], OBJ[i]), ln=1, align="L")
            error_m+=1
        i+=1

    #for x in result_malware.items():
        #print(x)
    

    ip_tor(pdf_report, pdf_report_global, bloqued_p, bloqued_b, bloqued_m, total_p, total_b, total_m, error_p, error_b, error_m)



def ip_tor(pdf_report, pdf_report_global, bloqued_p, bloqued_b, bloqued_m, total_p, total_b, total_m, error_p, error_b, error_m):
    pdf_report.cell(200,10, txt="STEP 4 : IP TOR CONNEXION", ln=1, align="L")
    #print("STEP 4 : IP TOR")
    with open("/home/deucalion/Documents/work_code/ids/json.json", "r") as f:
        obj = json.load(f)
    OBJ = obj["iptor"]
    total_tor = len(OBJ)
    i = 0
    bloqued_tor = 0
    result_tor = {}
    error_tor = 0
    while i < total_tor:
        try:
            r = requests.get(OBJ[i])
            if r.status_code == 200:
                result_tor[OBJ[i]] = 'Not Bloqued'
                pdf_report.cell(200,10, txt="{} : {}".format(result_tor[OBJ[i]], OBJ[i]), ln=1, align="L")
            elif r.status_code == 403:
                result_tor[OBJ[i]] = 'Bloqued'
                pdf_report.cell(200,10, txt="{} : {}".format(result_tor[OBJ[i]], OBJ[i]), ln=1, align="L")
                bloqued_tor+=1
            else:
                result_tor[OBJ[i]] = 'Error'
                pdf_report.cell(200,10, txt="{} : {}".format(result_tor[OBJ[i]], OBJ[i]), ln=1, align="L")
                error_tor+=1
        
        except:
            result_tor[OBJ[i]] = 'Can not create the request'
            pdf_report.cell(200,10, txt="{} : {}".format(result_tor[OBJ[i]], OBJ[i]), ln=1, align="L")
            error_tor+=1
        i+=1

    #for x in result_tor.items():
        #print(x)
    
    finish(pdf_report, pdf_report_global, bloqued_p, bloqued_b, bloqued_m, bloqued_tor, total_p, total_b, total_m, total_tor, error_p, error_b, error_m, error_tor)
    










def finish(pdf_report, pdf_report_global, bloqued_p, bloqued_b, bloqued_m, bloqued_tor, total_p, total_b, total_m, total_tor, error_p, error_b, error_m, error_tor):

    pdf_report_global.cell(200, 10, txt="Tentives de connexion sur les sites pornographiques :", ln=1, align="L")
    pdf_report_global.cell(200, 10, txt="Total   : {}".format(total_p), ln=1, align="L")
    pdf_report_global.cell(200, 10, txt="Bloquée : {}".format(bloqued_p), ln=1, align="L")
    pdf_report_global.cell(200, 10, txt="Error   : {}".format(error_p), ln=1, align="L")


    pdf_report_global.cell(200, 10, txt="Tentives de connexion sur les sites banquaires :", ln=1, align="L")
    pdf_report_global.cell(200, 10, txt="Total   : {}".format(total_b), ln=1, align="L")
    pdf_report_global.cell(200, 10, txt="Bloquée : {}".format(bloqued_b), ln=1, align="L")
    pdf_report_global.cell(200, 10, txt="Error   : {}".format(error_b), ln=1, align="L")


    pdf_report_global.cell(200, 10, txt="Tentives de connexion sur les sites de malware:", ln=1, align="L")
    pdf_report_global.cell(200, 10, txt="Total   : {}".format(total_m), ln=1, align="L")
    pdf_report_global.cell(200, 10, txt="Bloquée : {}".format(bloqued_m), ln=1, align="L")
    pdf_report_global.cell(200, 10, txt="Error   : {}".format(error_m), ln=1, align="L")


    pdf_report_global.cell(200, 10, txt="Tentives de connexion sur les IP TOR:", ln=1, align="L")
    pdf_report_global.cell(200, 10, txt="Total   : {}".format(total_tor), ln=1, align="L")
    pdf_report_global.cell(200, 10, txt="Bloquée : {}".format(bloqued_tor), ln=1, align="L")
    pdf_report_global.cell(200, 10, txt="Error   : {}".format(error_tor), ln=1, align="L")



    pdf_report.output("report_total.pdf")
    pdf_report=FPDF(orientation='P', unit='mm', format='A3')
    pdf_report_global.output('report_global.pdf')
    pdf_report_global=FPDF(orientation='P', unit='mm', format='A3')


    Notification(
        title='SoftSecurity Notification',
        description='Test terminé, vous pouvez découvrir vos rapports.',
        icon_path='logo_dino.png',
        duration=2,
        urgency=Notification.URGENCY_CRITICAL
    ).send()




