from dimits import Dimits


model = "/home/sujal/repos/AI project/data/models"
dt = Dimits(voice="en_US-lessac-medium", modelDirectory=model)
text = "As fresh snow blanketed the grounds of the kingdom, the white knight gazed out upon the sprawling valley. sighed to himself and said, I must be the loneliest knight in all of the land. All of a sudden, the white knight spotted a strange creature wandering up the snowy path towards him."
dt.text_2_audio_file(
    text, "hello_world", "/home/sujal/repos/AI project/data/sample_audio", format="wav"
)
