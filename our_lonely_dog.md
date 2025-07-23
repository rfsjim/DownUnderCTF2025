# Our Lonely Dog
**Category** - <span style="color:blue;">Beginner</span>

## Challenge Text
e-dog has been alone in the downunderctf.com email server for so long, please yeet him an email of some of your pets to keep him company, he might even share his favourite toy with you.

He has a knack for hiding things one layer deeper than you would expect.

Regards,
crem

## Goal
To get a flag from the dog.

## Initial Observations
I had the email server domain and a name for the dog. 

## Steps Taken
1. Sent email to the identified email address
2. After a considerable while a response was received from the dog
```
Hi,

E-dog gets quite pupset when they can't find their bone, especially when it's been a ruff day. Maybe we need to pull out a new one for them?
```
3. Emails have many other details as part of the `headers`. One of the `headers` in this particular email was the required flag
` X-FLAG: DUCTF{...} ` 