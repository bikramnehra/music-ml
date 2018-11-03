import sys
import logging
import ijson.backends.yajl2 as ijson
from numpy import array
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class model():
    def __init__(self):
        """
        performing two operations during initialization
        1. creating a dictionary of tags
        2. creating sparse matrix modeling the data
        """
        self.create_tag_dict()
        self.model_matrix = self.create_sparse_matrix(self.load_data())

    def load_data(self):
        """
        method to lazy load music.json file in memory
        """
        f = open("data/music-sample.json", 'rb')
        data = ijson.items(f, "item")

        return data

    def top_k_songs(self, songs, k):
        """
        method to return top k songs(based on score) from a list of given songs
        setting the default value of k to 5
        """
        k = int(k) if k else 5
        songs = sorted(songs.items(), key=lambda x: x[1], reverse=True)
        result = []
        # excluding input songs from the result
        for i in range(len(songs)):
            if int(songs[i][0]) not in self.input_songs:
                result.append(songs[i][0])
                if len(result) == k:
                    break

        return result

    def compute_score_v1(self, input_tags, limit):
        """
        computing score for every song using sets 
        """
        logger.info("computing score using sets...")
        model_dict = {}
        for song in self.load_data():
            current_tag_set = set(song["tags"])
            inter_set = input_tags.intersection(current_tag_set)
            union_set = input_tags.union(current_tag_set)
            score = len(inter_set) / float(len(union_set))
            model_dict[song["id"]] = score

        return self.top_k_songs(model_dict, limit)

    def create_tag_dict(self):
        """
        method to creating dictionary of all tags
        """
        logger.info("creating tag dictionary...")
        self.tags_dict = {}
        i = 0
        for song in self.load_data():
            for tag in song["tags"]:
                if tag not in self.tags_dict:
                    self.tags_dict[tag] = i
                    i += 1

    def create_sparse_matrix(self, songs):
        """
        method to create sparse matrix
        """
        logger.info("creating sparse matrix...")
        row = []
        col = []
        data = []
        total_songs = 1
        for r_idx, song in enumerate(songs):
            total_songs += 1
            for tag in song["tags"]:
                c_idx = self.tags_dict[tag]
                row.append(r_idx)
                col.append(c_idx)
                data.append(1)

        row = array(row)
        col = array(col)
        data = array(data)

        return csr_matrix((data, (row, col)), shape=(total_songs, len(self.tags_dict.keys())))

    def compute_score_v2(self, input_tags, limit):
        """
        computing score using cosine similariy
        """
        logger.info("computing score using cosine similarity...")
        test_song = [{"tags": list(input_tags)}]
        test_matrix = self.create_sparse_matrix(test_song)
        similarity = cosine_similarity(
            test_matrix[0:1], self.model_matrix).tolist()[0]

        songs_dict = {}
        for idx, val in enumerate(similarity):
            songs_dict[idx] = val

        return self.top_k_songs(songs_dict, limit)

    def create_tag_set(self):
        """
        method to fetch and create a set of tags for given songs
        """
        logger.info("creating tag set...")
        tags = []

        for song in self.load_data():
            if song["id"] in self.input_songs:
                tags.append(song["tags"])

        flat_tag_list = [item for sublist in tags for item in sublist]

        return set(flat_tag_list)

    def get_recommendations(self, input_songs, limit):
        """
        method to get recommendation based on given songs
        """
        self.input_songs = [int(song) for song in input_songs]
        logger.info("the input songs are: {} and limit: {}".format(
            self.input_songs, limit))
        tag_set = self.create_tag_set()
        v1_output = self.compute_score_v1(tag_set, limit)
        v2_output = self.compute_score_v2(tag_set, limit)
        final_output = {"recommendations(based on set ops)": v1_output,
                        "recommendations(based on cosine similarity)": v2_output}
        logger.info("the final output is: {}".format(final_output))

        return final_output
