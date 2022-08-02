from GrabzIt import GrabzItClient


def convert_to_gif(url, name):
    KEY = 'NzllZDVmMTA5NTI5NDY0MThmNGVkNzY4YTQwNmFhZGY='
    SECRET = 'dmA/P10/CUY/P2FiDz8/RD8iPx8BPz53Pz8YHz8/P3s='

    grabzIt = GrabzItClient.GrabzItClient(KEY, SECRET)
    grabzIt.URLToAnimation(url)
    grabzIt.SaveTo(f"{name}.gif")

    return print(f'Success. {name}.gif created')

convert_to_gif(url="https://youtu.be/7_Tts6B8r3M",
               name='MY_GIF')