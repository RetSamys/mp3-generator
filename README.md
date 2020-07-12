# mp3-generator
A project that might take me a decade or two because of how lazy I am.

I intend to code everything in Python 3 with a later re-create in JavaScript for webpages, and with the least dependencies/libraries possible (if I use libraries, they should be pre-installed).

Just some general, rambly thoughts:

If ever finished, this combines two crazy ideas that have no real practical value:
1) Imagine you could leave an short audioclip anywhere - as a QR code!
2) Babelia - but with sound clips instead of images or text!

1) QR codes sound like such an accessible thing - unfortunately, none of the popular QR readers read binary, much less save the binary as a file for you. Also, this is already done way better, for example by soundwave readers translating an image of the wave forms of an audioclip to sound. But I haven't seen anyone do it for QR - in fact, I haven't really seen any files being encoded as binary QR (but I only googled half-heartedly). I could imagine there could be issues, this being a somewhat unusual format, maybe involuntary downloads through QR codes are exploitable, but maybe it's also damn hard to make a proper QR reader, as you get less and less error correction with an increasingly complex QR code for higher and higher file sizes. Good thing I don't want to do it properly, a narrow 1:1 thing with some restrictions to make sure only MP3 files pass will be enough for me

2) https://babelia.libraryofbabel.info/
OK, so, I have one concern regarding the whole Library of Babel concept: It seems like a somewhat accessible way to circumvent copyright (or obfuscate) if you want to share stuff. This is only a theoretical concern, and probably not a huge practical problem, because aside from probably a ton of better tools for this kind of thing, the Library of Babel's reverse search is restrictive enough that you probably won't find more than a page. For images on Babelia, you might get something a little more useful, though. The seed usually being bigger than the file itself would maybe protect a site owner (don't take legal advice from me), but I have to wonder if the "Bookmarkable" short links could fall under something like a DMCA takedown request.
For audio, especially music, I have the impression the rights holders take this kind of thing a lot more serious than those for text or images... Hopefully, though, a 3 second clip in wonderful crispy 8kbps blows these concerns out of the water =D
