
#represents a video including basic info such as title and duration
class Video:

    VALID_RATINGS = ["PG-13", "R", "G"]

    def __init__(self, title, duration, personal_rating, poster, trailer):
        self.personal_rating = personal_rating;
        self.title = title
        self.duration = duration
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

        # prints info about the video
        def show_info(self):
            print("title:" + title + ",\nduration:" + duration)

#and attributes are inherited + new attributes describing a movie are added
#Movie is a subclass of Video, since it's a special kind of video. All functions
class Movie(Video):
    def __init__(self, title, duration, personal_rating, story, poster, trailer):
        Video.__init__(self, title, duration, personal_rating, poster, trailer)
        self.story = story

    # see parent-class
    def show_info(self):
        print("title: " + self.title + "\nduration: " + self.duration
        + "\nrating: " + self.personal_rating + "\nstory: "
        + self.story)

#TvShow is a subclass of Video, since it's a special kind of video. All functions
#and attributes are inherited + new attributes describing a tvshow are added
class TvShow(Video):
    def __init__(self, title, duration, personal_rating, season, episode, tv_station,
    poster, trailer):
        Video.__init__(self, title, duration, personal_rating, poster, trailer)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    # see parent-class
    def show_info(self):
        print("title: " + self.title + "\nduration: " + self.duration
        + "\nrating: " + self.personal_rating + "\nseason: "
        + self.season + "\nepisode: " + self.episode + "\nTV station: "
        + self.tv_station)
