# Look at all those chickens
**Category** - <span style="color:blue;">Beginner</span>

## Challenge Text
Hmmm, it appears this image was sent last year when one of our brave hackers went out to follow a lead to save some birds from those nasty bugs, but couldn't reach them! We did have it on good word that they were in captivity nearby to the picture that was taken- can you find out the name of the place where these birds were locked up?

The flag format is DUCTF{Captivity_Name} (case insensitive)

The answer is two words

Regards,
a_metre

## Goal
To identify the name of the place where the birds were locked up.

## Initial Observations
* A jpg image is provided, is there any metadata included in the image?
* I wonder if a reverse image search can assist?
* They specifically want a name of a place where birds were locked up. Must keep note of that when submitting an answer.
* The challenge text mentions that the hacker couldn't reach the birds, why not? Is there something that prevents them from gaining access?

## Steps Taken
1. Downloaded the image, inspected the metadata/EXIF data - no such luck.
2. Performed a Google Reverse Image search, a result comes up talking about a bin chicken island. The picture is definately of bin chickens, and there appears to be water separating the hacker from the birds, potentially it is some sort of island. This looks promising.
3. The article about Bin Chicken Island mentions that it is in Coburg, Victoria.
4. Looking at Bin Chicken Island in Coburg, Victoria I notice that Pentridge Prison, quite a famous Australian prison that has been home to some of well known alumni prisoners.
5. Convert Pentridge Prison into the required format is a success.