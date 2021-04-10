# Spotify Playlist Generator
Creates a personal playlist based on self chosen settings.

### Update 2021/04/10 - added audio feature analysis & code improvements

<img src="https://github.com/marwonn/spotify-playlist-generator/blob/master/static/images/1_04.png"  width="600">

<img src="https://github.com/marwonn/spotify-playlist-generator/blob/master/static/images/2_04.png"  width="600">


### Old Version

<img src="https://github.com/marwonn/spotify-playlist-generator/blob/master/static/images/1.jpg"  width="400">
<img src="https://github.com/marwonn/spotify-playlist-generator/blob/master/static/images/2.jpg"  width="400">
<img src="https://github.com/marwonn/spotify-playlist-generator/blob/master/static/images/3.png"  width="400">

### Setting options - frontend:

**Danceability** describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.

**Energy** is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.

**Valance**: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).

**Track count**: Number of tracks which will be searched and saved by the script.

**Seed genre**: Search of tracks is derived from a choosen seed genre.

### Setting options - script:
In `app.py` (line 16 / 17) artist seed & track seed can be set. Or put a `#` in front of the code to ignore the seed settings. 


### Running the app 
1.`pip install -r requirements.txt` \
2. fill in your credentials in `config.py` \
3. set redirect url in your spotify developer account to: http://localhost:5000/spotify-oauth2callback \
4. start with `flask run`


### Upcoming improvements
- audio feature analysis of all playlists of a current user
- make reccomendations derived from that personal audio feature analysis 
