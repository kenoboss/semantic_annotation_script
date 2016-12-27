# coding: utf-8
import re
import time

file = open("t_890121_161.txt.xml", "r", encoding="utf-8")
lines = file.readlines()

sentences = []
sentences_id = []
for line in lines:
    if (re.search("^s\d+\:", line)):
        sentences.append(line)
        line_split = line.split(":")
        sentence_id = line_split[0]
        sentences_id.append(sentence_id)


target = open("output.xml", "w", encoding="utf-8")

target.write('<?xml version="1.0"?>\n')
target.write("<corpus>\n")
index = 0
for sentence in sentences:
    target.write("<sentence id='"+str(sentences_id[index])+"'>\n")

    target.write("<tokens>\n")

    tokens = sentence.split(" ")
    i = 1
    while i < len(tokens):
        if (tokens[i] == "'"):
            tokens[i] = "&apos;"

        target.write("<token id='"+str(i)+"' value='"+str(tokens[i])+"'/>\n")
        i = i + 1
    target.write("</tokens>\n")
    target.write("</sentence>\n")

    index = index + 1

target.close()

target =  open("output.xml", "a+", encoding="utf-8")

target.write("<questionaires>\n")

zaehler = 1

test = False
while (test == False):
    for sentence in sentences:
        tokens = sentence.split(" ")
        sentenclength = len(tokens) - 1
        questionaire = input(sentence+"Länge: "+str(sentenclength)+"\nEingabe: ")
        if not (questionaire == ""):
            line_split = sentence.split(":")
            sentence_id = line_split[0]
            start = input("Start:")
            end = input("Ende:")
            target.write("<questionaire start='"+str(start)+"' end='"+str(end)+"' qid='"+str(sentence_id)+"q"+str(zaehler)+"' sid='"+str(sentence_id)+"' value='"+str(questionaire)+"'/>\n")

            zaehler = zaehler + 1

    time.sleep(2)
    x = input("=============Wiederholung?========\n '-1' für Abbruch\nEingabe: ")
    if (x == "-1"):
        test = True
    else:
        test = False

    print("\n==========Ende Abfrage Wiederholung===========")


target.write("</questionaires>\n")
target.write("</corpus>\n")

target.close()
