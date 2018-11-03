# cc_BikramdeepSingh_MusicML

A simplistic recommendation engine, which maximizes for the discovery of new songs. Songs are predicted using the following two approaches:

1. Set Operations:

   * Create a set of all tags for the given input songs
   * Calcluate score for each and every song by dividing length of 
      intersection by the length of the union
   * Return highest scoring top k songs

2. Cosine Similarity
   
   * Create sparse matrix storing information about tags present in 
     every song on the whole dataset
   * Create a set of all tags for the given input songs
   * Create sparse matrix for this data
   * Calculate cosine similarity between input data and whole data set
   * Return top k song having highest cosine similarity score



## Installation

### Requirements
* Linux
* Python 3.6 and up
* Docker 18 and above(optional)
* music.json file present <project-home-dir>/data folder

### Steps

1. Using Docker

```
$ git clone <repo-url>
$ cd <project-home-dir>
$ sudo docker pull fnndsc/ubuntu-python3
$ sudo docker build -t musicml .
$ docker run -p 5000:5000 musicml
```

2. Without Docker

```
$ git clone <repo-url>
$ cd <project-home-dir>
$ pip install -r requirements.txt
$ python app.py
```

## Usage

1. Sample Request

   `https://music-ml.herokuapp.com/recommendations?&songs=3,6,12`

   Sample Response

   ```json
   {
    "recommendations(based on cosine similarity)": [
        42,
        79,
        47,
        65,
        71
    ],
    "recommendations(based on set ops)": [
        42,
        79,
        47,
        65,
        71
    ]
   }
   ```

2. limit can also be specified in the request:

 `https://music-ml.herokuapp.com/recommendations?&songs=3,6,12&limit=3`

Note: The current production deployment only supports 100 songs(0 - 99) for songs parameter e.g 126 is an invalid value for songs parameter.
