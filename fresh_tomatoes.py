import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Meus Filmes Favoritos</title>

    <!--CSS INTERNAL-->
    <link rel="stylesheet" href="css/movie_style.css">

    <!--BOOTSTRAP 3-->

    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>

    <!--JAVASCRIPT -->
    <script src="JS/app.js"></script>

    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- menu da pagina -->
    <div class="self_main">
        <h2>Meus filmes</h2>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
     <h3>{title_video}</h3>
    <img src="{poster_image_url}" width="220" height="342">
    <h5>{storyline_video}</h5>
        <table class="table">
      <thead class="thead-dark">
        <tr>
          <th scope="col">Date</th>
          <th scope="col">Duration</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">{date_filme}</th>
          <td>{duration_video}</td>
        </tr>
        </tbody>
        </table>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            title_video=movie.title,
            duration_video=movie.duration,
            date_filme=movie.date,
            storyline_video=movie.storyline_video,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,


        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
