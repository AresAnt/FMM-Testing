# -*- coding: utf-8 -*-
import requests
import json
import os

def hapi_Server(contents,resourceName):
    try:
        if type(contents) is str:
            hapiserverCreateurl = "https://fhirtest.uhn.ca/baseDstu3/" + resourceName + "?_format=json&_pretty=true"
            create = requests.post(hapiserverCreateurl,data=contents)

            if create.status_code == 201:
                print("HTTP Status : 201")
                print("HTTP Header:")
                print(create.headers)
                print("Successful! Resource was Created.")

            ReadId = create.headers["Location"].split('/')[-3]

            hapiserverReadurl = "https://fhirtest.uhn.ca/baseDstu3/" + resourceName +  "/" + ReadId + "?_pretty=true&_format=json"
            read = requests.get(hapiserverReadurl)

            # return read.content.decode('utf-8')
            return read.content.encode('utf-8')
    except Exception as e:
        print("Hapi Server Create and Read Wrong",e)

def wild_Server(contents,resourceName):
    try:
        if type(contents) is str:
            wildserverCreateurl = "http://wildfhir.aegis.net/fhir3-0-1/" + resourceName + "?_format=json&_pretty=true"
            create = requests.post(wildserverCreateurl,json=json.loads(contents))
            
            if create.status_code == 201:
                print("HTTP Status : 201")
                print("HTTP Header:")
                print(create.headers)
                print("Successful! Resource was Created.")

            ReadId = create.headers["Location"].split('/')[-3]

            wildserverReadurl = "http://wildfhir.aegis.net/fhir3-0-1/" + resourceName + "/" + ReadId + "?_pretty=true&_format=json"
            read = requests.get(wildserverReadurl)

            # return read.content.decode('utf-8')
            return read.content.encode('utf-8')
    except Exception as e:
        print("Wild Server Create and Read Wrong",e)

def Grahame_Server(contents,resourceName):
    try:
        if type(contents) is str:
            grahameserverCreateurl = "http://test.fhir.org/r3/" + resourceName + "?_format=json&_pretty=true"
            create = requests.post(grahameserverCreateurl,json=json.loads(contents))
            
            if create.status_code == 201:
                print("HTTP Status : 201")
                print("HTTP Header:")
                print(create.headers)
                print("Successful! Resource was Created.")
            else:
                print("Wrong")
                print(create.status_code)
                return 'Grahame Server break down.'

            ReadId = create.headers["Location"].split('/')[-3]
            grahameserverReadurl = "http://test.fhir.org/r3/" + resourceName + "/" + ReadId + "?_pretty=true&_format=json"
            read =requests.get(grahameserverReadurl)

            # return read.content.decode('utf-8')
            return read.content.encode('utf-8')
    except Exception as e:
        print("Grahame Server Create and Read Wrong",e)

def vonk_Server(contents, resourceName):
    try:
        if type(contents) is str:
            vonkserverCreateurl = "http://vonk.furore.com/" + resourceName + "?_format=json&_pretty=true"
            create = requests.post(vonkserverCreateurl,json=json.loads(contents))

            if create.status_code == 201:
                print("HTTP Status : 201")
                print("HTTP Header:")
                print(create.headers)
                print("Successful! Resource was Created.")
            else:
                print("Wrong")
                print(create.status_code)
                return 'Grahame Server break down.'

            ReadId = create.headers["Location"].split('/')[-3]
            vonkserverReadurl = "http://vonk.furore.com/" + resourceName + "/" + ReadId + "?_pretty=true&_format=json"
            read = requests.get(vonkserverReadurl)

            # return read.content.decode('utf-8')
            return read.content.encode('utf-8')
    except Exception as e:
        print("Vonk Server Create and Read Wrong",e)


if __name__=='__main__':
    contents = "{\"resourceType\":\"ProcedureRequest\",\"extension\":[{\"extension\":[{\"url\":\"code\",\"valueCodeableConcept\":{\"coding\":[{\"display\":\"example genetic order code\"}]}},{\"url\":\"geneticsObservation\",\"valueReference\":{\"reference\":\"Observation/f001\"}},{\"url\":\"specimen\",\"valueReference\":{\"reference\":\"Specimen/101\"}},{\"url\":\"status\",\"valueCode\":\"unknown\"}],\"url\":\"http://hl7.org/fhir/StructureDefinition/procedurerequest-geneticsItem\"}],\"status\":\"draft\",\"intent\":\"order\",\"code\":{\"coding\":[{\"display\":\"Test Object for Genomics Profiles\",\"system\":\"http://hl7.org/fhir/dotnet-api-operation-outcome\",\"code\":\"6005\"}]},\"subject\":{\"reference\":\"Patient/example\"}}"
    resourceName = 'ProcedureRequest'

    # make all their dirs
    if not os.path.exists('./' + resourceName + '/hapi'):
        os.makedirs('./' + resourceName + '/hapi')

    if not os.path.exists('./' + resourceName + '/wild'):
        os.makedirs('./' + resourceName + '/wild')

    # if not os.path.exists('./' + resourceName + '/grahame'):
    #     os.makedirs('./' + resourceName + '/grahame')

    if not os.path.exists('./' + resourceName + '/vonk'):
        os.makedirs('./' + resourceName + '/vonk')

    # first Implementation ---------------------------------------------------------------------------
    fw = open('./' + resourceName + '/hapi/hapi_implementation.txt','w')
    print("Start Running hapi_server to create hapi implementation.")
    hapi1 = hapi_Server(contents,resourceName)
    fw.write(hapi1)
    fw.close
    print("Hapi implementation was read from hapi server, resource was writen to ./hapi/hapi_implementation.txt")

    fw = open('./' + resourceName + '/wild/wild_implementation.txt', 'w')
    print("\nStart Running wild_server to create wild implementation.")
    wild1 = wild_Server(contents, resourceName)
    fw.write(wild1)
    fw.close
    print("Hapi implementation was read from wild server, resource was writen to ./wild/wild_implementation.txt")

    fw = open('./' + resourceName + '/vonk/vonk_implementation.txt','w')
    print("\nStart Running vonk_server to create vonk implementation.")
    vonk1 = vonk_Server(contents, resourceName)
    fw.write(vonk1)
    fw.close
    print("Vonk implementation was read from vonk server, resource was writen to ./vonk/vonk_implementation.txt")

    # fw = open('./' + resourceName + '/grahame/grahame_implementation.txt', 'w')
    # print("\nStart Running Grahame_server to create grahame implementation.")
    # grahame1 = Grahame_Server(contents, resourceName)
    # fw.write(grahame1)
    # fw.close
    # print("Hapi implementation was read from grahame server, resource was writen to ./grahame/grahame_implementation.txt")


    # second hapi Implementation ---------------------------------------------------------------------------
    fw = open('./' + resourceName + '/hapi/wild_to_hapi.txt', 'w')
    print("\nStart Running hapi_server to create wild_to_hapi implementation.")
    hapi2_1 = hapi_Server(wild1, resourceName)
    fw.write(hapi2_1)
    fw.close
    print("Hapi implementation was read from hapi server, resource was writen to ./hapi/wild_to_hapi.txt")

    fw = open('./' + resourceName + '/hapi/vonk_to_hapi.txt', 'w')
    print("\nStart Running hapi_server to create vonk_to_hapi implementation.")
    hapi2_3 = hapi_Server(vonk1, resourceName)
    fw.write(hapi2_3)
    fw.close
    print("Hapi implementation was read from hapi server, resource was writen to ./hapi/vonk_to_hapi.txt")

    # fw = open('./' + resourceName + '/hapi/grahame_to_hapi.txt', 'w')
    # print("\nStart Running hapi_server to create grahame_to_hapi implementation.")
    # hapi2_2 = hapi_Server(grahame1, resourceName)
    # fw.write(hapi2_2)
    # fw.close
    # print("Hapi implementation was read from hapi server, resource was writen to ./hapi/grahame_to_hapi.txt")

    # second wild Implementation ---------------------------------------------------------------------------
    fw = open('./' + resourceName + '/wild/hapi_to_wild.txt', 'w')
    print("\nStart Running wild_server to create hapi_to_wild implementation.")
    wild2_1 = wild_Server(hapi1, resourceName)
    fw.write(wild2_1)
    fw.close
    print("Wild implementation was read from wild server, resource was writen to ./wild/hapi_to_wild.txt")

    fw = open('./' + resourceName + '/wild/vonk_to_wild.txt', 'w')
    print("\nStart Running wild_server to create vonk_to_wild implementation.")
    wild2_3 = wild_Server(vonk1, resourceName)
    fw.write(wild2_3)
    fw.close
    print("Wild implementation was read from wild server, resource was writen to ./wild/vonk_to_wild.txt")

    # fw = open('./' + resourceName + '/wild/grahame_to_wild.txt', 'w')
    # print("\nStart Running wild_server to create grahame_to_wild implementation.")
    # wild2_2 = wild_Server(grahame1, resourceName)
    # fw.write(wild2_2)
    # fw.close
    # print("Hapi implementation was read from wild server, resource was writen to ./wild/grahame_to_wild.txt")

    # second vonk Implementation ------------------------------------------------------------------------------

    fw = open('./' + resourceName + '/vonk/hapi_to_vonk.txt', 'w')
    print("\nStart Running vonk_server to create hapi_to_vonk implementation.")
    vonk2_1 = wild_Server(hapi1, resourceName)
    fw.write(vonk2_1)
    fw.close
    print("Vonk implementation was read from wild server, resource was writen to ./vonk/hapi_to_vonk.txt")

    fw = open('./' + resourceName + '/vonk/wild_to_vonk.txt', 'w')
    print("\nStart Running vonk_server to create wild_to_vonk implementation.")
    vonk2_2 = wild_Server(wild1, resourceName)
    fw.write(vonk2_2)
    fw.close
    print("Vonk implementation was read from wild server, resource was writen to ./vonk/wild_to_vonk.txt")



    # second grahame Implementation ---------------------------------------------------------------------------
    # fw = open('./' + resourceName + '/grahame/hapi_to_grahame.txt', 'w')
    # print("\nStart Running Grahame_server to create grahame implementation.")
    # grahame2_1 = Grahame_Server(hapi1, resourceName)
    # fw.write(grahame2_1)
    # fw.close
    # print("Hapi implementation was read from grahame server, resource was writen to ./grahame/hapi_to_grahame.txt")
    #
    # fw = open('./' + resourceName + '/grahame/wild_to_grahame.txt', 'w')
    # print("\nStart Running Grahame_server to create grahame implementation.")
    # grahame2_2 = Grahame_Server(wild1, resourceName)
    # fw.write(grahame2_2)
    # fw.close
    # print("Hapi implementation was read from grahame server, resource was writen to ./grahame/wild_to_grahame.txt")

    print('\nProgram Down')