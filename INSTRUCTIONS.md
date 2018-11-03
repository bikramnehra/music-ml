## Fictional MVP!

A fictional client has asked for a recommendation system for their music player system.
It's supposed to be a simplistic recommendation engine, which maximizes for the discovery of new songs.

In this system there is just one element:

- **music**: have an ID and a list of tags (see `music.json.zip`)


How to model or index this data is up to you.

### Endpoint

There should just be one endpoint which should return 5 song recommendations based on the tags of the songs being passed in from the query parameter `songs`.

##### `GET /recommendations?songs=3,6,12`


Query string should have:

- songs: multiple song ids

Response should look like:
```json
{
  "recommendations": ["<music ID>", "<music ID>", "<music ID>", "<music ID>", "<music ID>"]
}
```

## Deployment

**Deploy it to a free cloud service so we can test it (AWS, Heroku, etc)**

The focus of this assignment is to get a deployed service that is accessible to the public. You may use whatever tools you're most comfortable with.


## Hints

- Don't worry about finding a perfect solution, it is an MVP. There isn't a single correct approach; we want to see your process and your results.

- Please commit regularly so we can follow along; branching should not be required.

- Answer `QnA.md` and create a `README.md` file with a short description of what you've built, and instructions required to build, run, and test your solution. (If a link to that repo did not accompany this assignment, please let us know ASAP and don't forget to tell us your GitHub user ID).

- Don't bite off more than you can chew. We anticipate that this problem should take less than eight hours; if you feel like this estimate is off for any reason, let us know as soon as possible so we can tweak it to fit in that range.

- Please feel free to ask us any questions and let us know if you have problems, we're happy to help!
