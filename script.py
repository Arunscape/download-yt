import youtube_dl
import feedparser
# ydl_opts = {}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
baseUrl = 'https://www.youtube.com/feeds/videos.xml?channel_id='

techChannels = [
    ('UCXuqSBlHAE6Xw-yeJA0Tunw', 'LinusTechTips'),
    ('UCkWQ0gDrqOCarmUKmppD7GQ', 'JayzTwoCents'),
    ('UCeeFfhMcJa1kjtfZAGskOCA', 'TechLinked'),
    ('UC0vBXGSyV14uvJ4hECDOl0Q', 'TechQuickie'),
    ('UCBZiUUYeLfS5rIj4TQvgSvA', 'ChannelSuperFun'),
    ('UCTI1K7wGKCYLzG3xx3Jo_zw', 'MemoryExpress'),
    ('UCBJycsmduvYEL83R_U4JriQ', 'MKBHD')
]

hermitCraft = [
    ('UChFur_NwVSbUozOcF_F2kMg', 'Mumbo'),
    ('UCDpdtiUfcdUCzokpRWORRqA', 'RenDog'),
    ('UCPK5G4jeoVEbUp5crKJl6CQ', 'Grian'),
    ('UCPK5G4jeoVEbUp5crKJl6CQ', 'Zedaph'),
    ('UCZ9x-z3iOnIbJxVpm1rsu2A', 'Iskall'),
    ('UC32w6uX5qtmUtF4QQQ2PKaQ', 'HermitCraftRecap')
]

educational = [
    ('UCJ0-OtVpF0wOKEqT2Z1HEtA', 'ElectroBOOM'),
    ('UCKKiQ8Bz3pgiJ7JdqNrQfeQ', 'ElectroBOOM'),  # Mehditation, 2nd channel
    ('UCu6mSoMNzHQiBIOCkHUa2Aw', "Cody'sLab"),
    ('UC2MJylovjrLtsGP0_4UrqrQ', "Cody'sLab"),  # Cody'sBlab, 2nd channel
    ('UC7DdEm33SyaTDtWYGO2CwdA', 'PhysicsGirl'),
    ('UCSIvk78tK2TiviLQn4fSHaw', 'UpandAtom'),
    ('UC0e3QhIYukixgh5VVpKHH9Q', 'CodeBullet'),
    ('UCUHW94eEFW7hkUMVaZz4eDg', 'MinutePhysics'),
    ('UC3KEoMzNz8eYnwBC34RaKCQ', 'SimoneGiertz')
]

other = [
    ('UCD6GYvOYBBNVm1eGQKUaGCA', 'ThisHourHas22Minutes'),
    ('UCNkEZxxZeRd6VXMnQV8EX0g', 'LostLandsMusicFestival')
]


if __name__ == "__main__":
    for x in techChannels:
        d = feedparser.parse(baseUrl + 'UCXuqSBlHAE6Xw-yeJA0Tunw')
        print(d)
