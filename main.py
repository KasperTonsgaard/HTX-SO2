from appJar import gui

import fakeNewsPDF
import fakeNewsSpeaker
import fakeNewsWebsite


# create a GUI variable called app
app = gui("Fake News Generator", "400x100")

def buttonPress(buttonName):
    if buttonName == "Generate PDF":
        fakeNewsPDF.GeneratePDF()
        app.showSubWindow("pdf")

    elif buttonName == "Generate Website":
        fakeNewsWebsite.GenerateWebsite()
        app.showSubWindow("website")

    elif buttonName == "Speak":
        fakeNewsSpeaker.SayFakeNews()


app.addLabel("title", "Welcome to 18xR Fake News Generator")
app.addButtons(["Generate PDF", "Generate Website", "Speak"], buttonPress)

app.startSubWindow("pdf", modal=True)
app.addLabel("PDF was made successfully", "PDF was made successfully\nFind it in the pdf folder")
app.stopSubWindow()

app.startSubWindow("website", modal=True)
app.addLabel("Website was made successfully", "Website was made successfully\nFind fakenews.html in the website folder")
app.stopSubWindow()


app.go()