# -*- coding: utf-8 -*-
import webbrowser
''' Armazena as informações basicas dos videos '''


class Video():
    def __init__(self, title_video, duration_video, date_filme):
        self.title = title_video
        self.duration = duration_video
        self.date = date_filme
''' Armazena as informações dos filmes '''


class Movie(Video):
    def __init__(self, title_video, duration_video, date_filme,
                 storyline_video, trailer_youtube_url, poster_image_url):
        Video.__init__(self, title_video, duration_video, date_filme)
        self.storyline_video = storyline_video
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url


'''Armazena as informações das Series de televisão '''


class Tvserie(Video):
    def __init__(self, episode_serie, season_serie,
                 title_video, trailer_youtube_url,
                 duration_video='n/a', date_filme='n/a'):
        Video.__init__(self, title_video,
                       duration_video='n/a', date_filme='n/a')
        self.episode = episode_serie
        self.season = season_serie
        self.trailer_youtube_url = trailer_youtube_url
