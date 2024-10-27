### Python

Download from Microsoft Store: https://www.microsoft.com/store/productId/9NCVDN91XZQP?ocid=pdpshare

When the download is complete, in a console, run:

```
python --version
```

If the output is "Python 3.12.2 (or higher)" Click [here](../../README.md#initial-setup) to return to the setup page, otherwise you need to add the path to python3.12 to the PATH environment variable.

To do so, in the search bar next to START, type "python3.12" and click on "Open file location".

![Alt text](<../assets/images/image-19.png>)

Then right-click on the top bar that shows the path and select copy address.

![Alt text](<../assets/images/image-20.png>)

In a console, run:

```
setx /M PATH "%PATH%;<copied address>"
```

so it should look like:

```
setx /M PATH "%PATH%;C:\Users\Luca.LaPenna\AppData\Local\Microsoft\WindowsApps"
```

if the output is successfull close the terminal and open a new one to apply the changes.

In the new console, run:

```
python --version
```

The output should now be "Python 3.12.2 (or higher)".

Click [here](../../README.md#initial-setup) to return to the setup page.