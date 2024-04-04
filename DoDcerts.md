# Working with a DoD Canvas
I specifically am trying to use a DoD Canvas version.  I was getting an error like the following when I ran some of the Canvas API commands:

```
SSLError: HTTPSConnectionPool(host='aueems.cce.af.mil', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)')))
```

Turns out this is typically an error in the root certificates on your machine.  

The first thing to check is if you can go to the API through your web browser. If so, then your web browser has some root certificates that your Python program is not seeing.  You can also check what the root certificate is that you are missing [instructions here](https://www.hostgator.com/help/article/how-to-check-the-ssl-information-of-websites).

To solve this for DoD Certs requires two things:
1.  The root DoD certificates
2.  To add these certificates to your local list of root certificates

## Getting the DoD root certificates
To be more specific, you need the DoD root certificates in a `.pem` file format.  I got it from [this](https://github.com/erdc/dodcerts) repository.  Specifically, I just downloaded [the file](https://github.com/erdc/dodcerts/blob/master/dodcerts/dod-ca-certs.pem) in `dodcerts`.

There are also ways to generate the pem file if you have the certificates in another format (google is your friend here), but I had a hard time finding an official version of the certs, in .pem or not, so I just used the github version linked above.

## Adding certificates to your local list.
Note that the package that Python uses to find certificates is called certifi. So, in the Python venv that you want to use, run the command `certifi.where()` and then append the .pem you have to the pem that command lists.  I used instructions from [this webpage](https://appdividend.com/2022/06/01/python-certifi/), but basically:

```
cafile = open(certifi.where(),'ab')
my_cacerts_file = open(Path to .pem file I downloaded,'rb')
new_ca = my_cacerts_file.read()
cafile.write(new_ca)
```
That fixed it for me.

