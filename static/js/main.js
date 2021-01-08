var uris = "[]";

$(document).on("click","#generate-spotify-recs", function(){
    //construct payload using form data then send to server 
    let payload = {};
    payload['danceability'] = $('#danceability').val();
    payload['valence'] = $('#valence').val()
    payload['energy'] = $('#energy').val()
    payload['track-count'] = $('#track-count').val()
    payload['seed-genre'] = $('#seed-genre').val()
    payload['seed-artist'] = $('#seed-artist').val()

    $.ajax({
        type: "POST",
        url: "/get-recommended-playlist",
        data: JSON.stringify(payload),
        contentType: "application/json",
        success: function(res){
            $('#song-container').empty();
            $('#create-my-playlist').html('Save Playlist to Spotify')
            console.log(res);
            for (x of res['songs']){
                content = `<div><p>`+x['name'] + `<small> by `
                for (i of x['artists']){
                    content += i['name'] + ","
                }
                content = content.slice(0,-1);
                content += `</small></p></div>`
                $('#song-container').append(content);
            }

            //make button for saving visible 
            $('#create-my-playlist').show();
            $('#create-my-playlist').attr('disabled', false);
            //save uri list to variable so to be used by save event listener
            uris = res['uris'];

        },
        error: function (xhr, status, errorThrown) {
            if (xhr.status == 400 || xhr.status == 403){
                location.reload();
            }
    
        }
    });
});

$(document).on("click","#create-my-playlist", function(){
    //take uris from storage and send them to server 
    payload = uris 
    $.ajax({
        type: "POST",
        url: "/save-private-playlist",
        data: payload,
        contentType: "application/json",
        success: function(res){
            alert("Successfully saved playlist to spotify");
            //disable button
            $('#create-my-playlist').attr('disabled', true);
            $('#create-my-playlist').html('Playlist Saved!');

        },
        error: function (xhr, status, errorThrown) {
            alert("Error saving playlist to Spotify. Try again or refresh page");
    
        }
    });

});