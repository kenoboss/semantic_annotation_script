import xml.etree.ElementTree as etree
from operator import attrgetter

target = open("result.txt", "w", encoding="utf-8")


tree = etree.parse('output.xml')
root = tree.getroot()

sids = []
for questionaire in root.iter('questionaire'):
    #q_id = questionaire.attrib['qid']
    s_id = questionaire.attrib['sid']
    sids.append(s_id)
    # start = questionaire.attrib['start']
    # end = questionaire.attrib['end']
    # string = questionaire.attrib['value']

for sentence in root.iter('sentence'):
    sentence_id = sentence.attrib['id']

    if (sentence_id in sids):
        control = False
        for questionaire in root.iter('questionaire'):
            q_id = questionaire.attrib['qid']
            s_id = questionaire.attrib['sid']
            start = questionaire.attrib['start']
            end = questionaire.attrib['end']
            string = questionaire.attrib['value']

            if (sentence_id == s_id):
                sentence_line = ""
                for tokens in sentence.findall('tokens'):
                    sentence_line += str(sentence_id)+": "
                    index = 1
                    for token in tokens.findall('token'):
                        if (int(start) == index and int(end) == index):
                            sentence_line += "<"+str(q_id)+" "+str(token.attrib['value'])+" "+str(q_id)+"> "
                        else:
                            if (int(start) == index):
                                sentence_line += "<"+str(q_id)+" "+str(token.attrib['value'])+" "
                            elif(int(end) == index):
                                sentence_line += str(token.attrib['value'])+" "+str(q_id)+"> "
                            else:
                                sentence_line += str(token.attrib['value'])+" "
                        index = index + 1


                if (control == False):
                    control = True
                    target.write(sentence_line+"\n")
                target.write(str(q_id)+": "+str(string)+"\n\n")


    else:
        sentence_line = ""
        for tokens in sentence.findall('tokens'):
            sentence_line += str(sentence_id)+": "
            for token in tokens.findall('token'):
                sentence_line += str(token.attrib['value'])+" "

        target.write(sentence_line+"\n\n")





target.close()
