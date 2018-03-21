import media
import fresh_tomatoes

# Some media objects are created (movies and tv-series-episodes) and
# inserted into an array of media-items. Then the sute-creation is
# started by calling 'open_movies_page'

toy_story = media.Movie(
    "Toy Story",
    "90 min",
    "8.0/10",
    "Toy Story plot",
    "https://upload.wikimedia.org/wikipedia/commons/0/0a/Toy_Story_logo.svg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
)

lotr1 = media.Movie(
    "The Lord of the Rings: The Fellowship of the Ring",
    "200 min",
    "10/10",
    """First part of the Lord of the Rings trilogy. From the shire to the
    breaking ot the fellowship""",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_" +
    "The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=z_WZxJpHzEE"
)

lotr2 = media.Movie(
    "The Lord of the Rings: The Two Towers",
    "200 min",
    "10/10",
    """Second part of the Lord of the Rings trilogy. The fellowship is broken
    and each part follows a different
    path. Tells of the further journey of the ring, the war between Rohan
    and Isengard and (spoiler alert)
    features the return of a most beloved character thought dead""",
    "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_" +
    "The_Two_Towers.jpg",
    "https://www.youtube.com/watch?v=Y4neBR0h39c"
)

lotr3 = media.Movie(
    "The Lord of the Rings: The Return of the King",
    "200 min",
    "10/10",
    """Third part of the Lord of the Rings trilogy. Tells of the final battles
    between good and evil and follows
    the journey of the ring to whichever end it may come""",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_" +
    "The_Return_of_the_King.jpg",
    "https://www.youtube.com/watch?v=KOQSQaGgJxs"
)

bb_1_1 = media.TvShow(
    "Breaking Bad",
    "55 min",
    "10/10",
    1,
    1,
    "AMC",
    "https://upload.wikimedia.org/wikipedia/commons/7/77/" +
    "Breaking_Bad_logo.svg",
    "https://www.youtube.com/watch?v=HhesaQXLuRY"
)

bb_1_2 = media.TvShow(
    "Breaking Bad",
    "55 min",
    "9.8/10",
    1,
    2,
    "AMC",
    "https://upload.wikimedia.org/wikipedia/commons/7/77/" +
    "Breaking_Bad_logo.svg",
    "https://www.youtube.com/watch?v=HhesaQXLuRY"
)

got_1_1 = media.TvShow(
    "Game Of Thrones",
    "45 min",
    "9.5/10",
    1,
    1,
    "HBO",
    "http://www.gstatic.com/tv/thumb/tvbanners/" +
    "14160794/p14160794_b_v8_aa.jpg",
    "https://www.youtube.com/watch?v=gcTkNV5Vg1E"
)

media = [toy_story, lotr1, lotr2, lotr3, bb_1_1, bb_1_2, got_1_1]
fresh_tomatoes.open_movies_page(media)
