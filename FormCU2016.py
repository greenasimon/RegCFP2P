from bs4 import BeautifulSoup
import csv
import os
import glob

#Open CSV file and add the headers
# Maintaining orders are manadatory for headers to capture the correct data in csv files
csvheaders = [["FormType","AccessionNum","PublicDocCount", "CIK", "FileNumber", "FilmNumber", "FiledDate","ChangeDate",
               "CompanyName", "IrsNum", "IncState", "FiscYrEnd", "SecAct","Phone", "BisStreet", "BisCity", "BisState",
               "BisZip", "MailStreet", "MailCity", "MailState", "MailZip",
               #document tags
               "filercik", "liveflag", "ConfirmCopy", "ReturnCopy", "OverrideInternet", "ProgressUpdate",
               "IssuerName", "OrgStatus", "OrgJurisdiction", "DateInc", "IssuerStreet", "IssuerCity", "IssuerState",
               "IssuerZip", "website", "PortalName", "PortalCIK", "PortalFileNum","IssuerSign", "IssuerTitle",
               "PersonSign", "PersonTitle"]]
outFile = open('Form_CU_2016.csv','w', newline= '')
inputData = []
#for the text part
SecHeaders = ["ACCESSION NUMBER","PUBLIC DOCUMENT COUNT", "CENTRAL INDEX KEY", "SEC FILE NUMBER", "FILM NUMBER",
              "FILED AS OF DATE","DATE AS OF CHANGE", "COMPANY CONFORMED NAME","IRS NUMBER", "STATE OF INCORPORATION",
              "FISCAL YEAR END", "SEC ACT", "BUSINESS PHONE" ]
#for the same sub headings in text
SubHeaders = ["BUSINESS ADDRESS", "MAIL ADDRESS"]
Attrs = ["STREET 1", "CITY", "STATE", "ZIP"]
#for the tags in the doc, single valued
DocHeaders = ["filercik", "livetestflag", "confirmingcopyflag", "returncopyflag", "overrideinternetflag",
              "progressupdate", "nameofissuer",
              "legalstatusform", "jurisdictionorganization", "dateincorporation", "com:street1", "com:city",
              "com:stateorcountry", "com:zipcode", "issuerwebsite", "companyname", "commissioncik", "commissionfilenumber",
              "issuersignature", "issuertitle",
              "personsignature", "persontitle"]

# Defining function to extract elements from text
def ExtractTextElement( parentHeader, childHeader):
    temp = parentHeader.split(childHeader + ":")
    if len(temp)>1:
        ret = temp[1].splitlines()[0].strip(' \t')
    else: ret = ""
    return ret

#function to extract content from tags
def ExtractTagElement( parentSoup, childTag ):
    tempTag = parentSoup.find_all(childTag)
    ret = ""
    if len(tempTag) == 0:
        tempTag.append(parentSoup.find(childTag))
    for subTag in tempTag:
        if subTag != None and len(subTag.contents) > 0:
           if ret == "":
               ret = subTag.contents[0].strip(' \t\r\n')
           else: ret = ret + "/" + subTag.contents[0].strip(' \t\r\n')
    return ret
#Change directory to the file folder
os.chdir("/projects/academic/bawolfe/pullman/forms/RegCF/Edgar filings/ALL_C-U_2016")
#os.chdir("C:/Users/GreenaSimon/PycharmProjects/IS")
with outFile:
    writer = csv.writer(outFile)
    writer.writerows(csvheaders)
    count = 0
    for file in glob.glob("*.txt"):
        print("trying to open", file)
        with open(file)as sample:
            print("Opening", file )
            soup = BeautifulSoup(sample, "lxml")
        print("made soup", file)
        DescHeader = soup.find("acceptance-datetime").contents[0]
        FormType = 'C/U'
        Outdata = [FormType] #Initilizing
        # Extracts Sec Header info begin
        print("starting secheaders")
        for secHeader in SecHeaders:
            Outdata.append( ExtractTextElement( DescHeader, secHeader ))        # sec header info end
        # Extracting data from sub headings with same attrs
        print("startingsubheaders")
        for subHeader in SubHeaders:
            sub = DescHeader.split(subHeader+':')
            if len(sub)>1:
               for attr in Attrs:
                   Outdata.append(ExtractTextElement(sub[1], attr))
        # Extracting tag details begin
        print("starting docheaders")
        for docHeader in DocHeaders:
            Outdata.append(ExtractTagElement(soup, docHeader))
        print("done extracting")
        #write this row to csv
        inputData.append(Outdata)
        count = count + 1
        print("processed", file,count)
        sample.close()
    writer.writerows(inputData)