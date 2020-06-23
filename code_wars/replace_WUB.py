""" 
Input
The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters

Output
Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

Examples
song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
 """

def song_decoder(song):
    song  = song.split("WUB")
    song = [w for w in song if w != str()]
    return " ".join(song)


print(song_decoder("AWUBWUBWUBBWUBWUBWUBC")) # A B C