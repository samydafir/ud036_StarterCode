import webbrowser
import os
import re
import media

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Entertainment Center</title>

    <!-- Bootstrap 4 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="css/main.css" type="text/css" media="screen">

    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.tile').hide();
          $('.tile').each(function(i, obj) {
            $(this).show(400);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar. Modified to include a TV-Shows section
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <nav class="navbar fixed-top navbar-expand-sm navbar-dark bg-dark">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#nav-content" aria-controls="nav-content" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>

    <!-- Brand -->
    <a class="navbar-brand" href="#">Entertainment Center</a>

    <!-- Links -->
    <div class="collapse navbar-collapse" id="nav-content">
        <ul class="navbar-nav">
            <li class="nav-item">
                <a class="nav-link" href="#moviesection">Movies</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#tvshowsection">TV Shows</a>
            </li>
        </ul>
</nav>
    <div class="container-fluid" id="moviesection">
    <h2>Movies</h2>
    <div class="row">
        {movie_tiles}
    </div>
    </div>
    <hr class="section-separator">
    <div class="container-fluid" id="tvshowsection">
    <h2>TV Shows</h2>
    <div class="row">
        {tv_show_tiles}
    </div>
    </div>
  </body>
</html>
'''


# A single movie entry html template
tile_content = '''
<div class="col-md-4 tile text-center mx-auto" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img class="rounded-corners" src="{poster_image_url}" width="220" height="342">
    <h2>{title}</h2>
</div>
'''

# Creates the html content for movie and tv_show tiles.Extracts the youtube url
# and info required for display from each object in the passed list. Differentiates
# between movies and tv_shows. Processes TV-shows such that every show is only
# displayed once on the site, no matter how many episodes the list contains.
# Returns an array containing two strings: html for movies and tv-shows.
def create_movie_tiles_content(videos):
    # The HTML content for this section of the page
    content_movies = ''
    content_tv_shows = ''
    found_shows = set()
    for medium in videos:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', medium.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', medium.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                          else None)
        if isinstance(medium, media.Movie):
            # Append the tile for the movie with its content filled in
            content_movies += tile_content.format(
                title=medium.title,
                poster_image_url=medium.poster_image_url,
                trailer_youtube_id=trailer_youtube_id
            )
        elif isinstance(medium, media.TvShow) and not medium.title in found_shows:
            # Append the tile for the tv_show with its content filled in
            content_tv_shows += tile_content.format(
                title=medium.title,
                poster_image_url=medium.poster_image_url,
                trailer_youtube_id=trailer_youtube_id
            )
            found_shows.add(medium.title)

    return [content_movies, content_tv_shows]

# Creates a new html file, writes the static content, replaces keys with created
# html code and writes the file to disk
def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    content = create_movie_tiles_content(movies)
    rendered_content = main_page_content.format(
        movie_tiles=content[0], tv_show_tiles = content[1])

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
