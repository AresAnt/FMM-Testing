# FMM-Testing

This is a simple demo of FMM-Testing.

Under /ScreenShot are pics of how the process of running this program

This demo is related to three fhir servers: hapi(https://fhirtest.uhn.ca/), wild (http://wildfhir.aegis.net/fhir3-0-1-gui/index.jsf) and vonk(http://vonk.furore.com/);

We create resource from all this servers, and put their results to the other servers. 

How to use
----------------
First 

Need to install requests moudule

```
$ pip install requests
```

Second

Make sure your Json file is all right

Then get the Json minified and compressed. You can do that in there: https://codebeautify.org/jsonminifier

Copy the result to change the python code. [ content , resourceName ]

```
if __name__ == __main__:
  content = "(change here)"
  resourceName = "(change here)"
```
