import os
import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import urllib
import urllib.parse

from resources.lib.globals import G



def show_root_menu():
    """ Show the plugin root menu """
    li_style = xbmcgui.ListItem('[B]' + G.LANGUAGE(32001) + '[/B]', offscreen=True)
    li_style.setArt({'thumb': os.path.join(G.THUMB_PATH, 'camera.jpg'), 'fanart': G.FANART_PATH})
    add_directory_item({"mode": "camera"}, li_style)

    li_style = xbmcgui.ListItem('[B]' + G.LANGUAGE(32002) + '[/B]', offscreen=True)
    li_style.setArt({'thumb': os.path.join(G.THUMB_PATH, 'senato.png'), 'fanart': G.FANART_PATH})
    add_directory_item({"mode": "senato"}, li_style)

    li_style = xbmcgui.ListItem('[B]' + G.LANGUAGE(32003) + '[/B]', offscreen=True)
    li_style.setArt({'thumb': os.path.join(G.THUMB_PATH, 'tv.png'), 'fanart': G.FANART_PATH})
    add_directory_item({"mode": "tv"}, li_style)

    li_style = xbmcgui.ListItem('[B]' + G.LANGUAGE(32004) + '[/B]', offscreen=True)
    li_style.setArt({'thumb': os.path.join(G.THUMB_PATH, 'radio.png'), 'fanart': G.FANART_PATH})
    add_directory_item({"mode": "radio"}, li_style)

    xbmcplugin.endOfDirectory(handle=G.PLUGIN_HANDLE, succeeded=True)



def add_directory_item(parameters, li, folder=True):
    url = sys.argv[0] + '?' + urllib.parse.urlencode(parameters)
    return xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=url, listitem=li, isFolder=folder)



def programmi_camera():
    thumb = 'https://yt3.googleusercontent.com/hFbWr3ydEXfeoX1BS18GG7OEkXW_jNCDBhWu5sVoBAVv7fdpVUcIRKSNlRery4EbiUzQsRK39OU=s160-c-k-c0x00ffffff-no-rj'
    
    canali = [
        ('Camera - Canale Satellitare', 'BD4kcj6KspM'),
        ('Camera - Canale Assemblea', 'Cnjs83yowUM'),
    ]
    for titolo, video_id in canali:
        link = f'plugin://plugin.video.youtube/play/?video_id={video_id}'
        li = xbmcgui.ListItem(titolo, offscreen=True)
        li.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
        li.setInfo('video', {})
        li.setProperty('isPlayable', 'true')
        xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=li, isFolder=False)

    xbmcplugin.endOfDirectory(handle=G.PLUGIN_HANDLE, succeeded=True)



def programmi_senato():
    thumb = 'https://yt3.googleusercontent.com/ytc/AIdro_kuWqJTQYB5earQtR1bMmun99HvofpjYQKNYbZdS4hNaA=s160-c-k-c0x00ffffff-no-rj'
    
    canali = [
        ('Senato - Canale 1', 'sPbVV3E737E'),
        ('Senato - Canale 2', 'WyQMW1oJpOo'),
        ('Senato - Canale 3', 'PjPRSf2oN4w'),
        ('Senato - Canale 4', 'KQPgwlDN-1E'),
        ('Senato - Canale 5', 'eIyBRC6dHoQ'),
        ('Senato - Canale 6', 'loiN1npW2MM'),
        ('Senato - Canale 7', 'c0hzsRTIbQk'),
        ('Senato - Canale 8', 'vOR7zAjorO8'),
    ]
    for titolo, video_id in canali:
        link = f'plugin://plugin.video.youtube/play/?video_id={video_id}'
        li = xbmcgui.ListItem(titolo, offscreen=True)
        li.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
        li.setInfo('video', {})
        li.setProperty('isPlayable', 'true')
        xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=li, isFolder=False)

    xbmcplugin.endOfDirectory(handle=G.PLUGIN_HANDLE, succeeded=True)



def programmi_tv():
    titolo = 'RaiNews24'
    liStyle = xbmcgui.ListItem(titolo, offscreen=True)
    link = 'https://8e7439fdb1694c8da3a0fd63e4dda518.msvdn.net/rainews1/hls/playlist_mo.m3u8'
    thumb = 'https://www.rainews.it/dl/components/img/svg/RaiNewsBarra-logo.png'
    liStyle.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=liStyle, isFolder=False)


    titolo = 'TgCom24'
    liStyle = xbmcgui.ListItem(titolo, offscreen=True)
    link = 'https://live03-col.msf.cdn.mediaset.net/live/ch-kf/kf-clr.isml/manifest.mpd|User-Agent=HbbTV/1.6.1'
    thumb = 'https://www.mimesi.com/wp-content/uploads/2017/11/tgcom24.jpg'
    liStyle.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=liStyle, isFolder=False)


    titolo = 'SkyTg24'
    liStyle = xbmcgui.ListItem(titolo, offscreen=True)
    # Token (valido fino al 22/12/2027)
    link = 'https://hlslive-web-gcdn-skycdn-it.akamaized.net/TACT/12221/web/master.m3u8?hdnts=st=1764666351~exp=1829466206~acl=/*~hmac=b0e9165b6c55027903ad103c8219f363d8765eb300c0d9a339e9767fc3509556'
    thumb = 'https://www.motork.io/it/wp-content/uploads/sites/2/2020/02/skytg24-logo.jpg'
    liStyle.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=liStyle, isFolder=False)


    titolo = 'R.Radicale TV'
    liStyle = xbmcgui.ListItem(titolo, offscreen=True)
    link = 'https://video-ar.radioradicale.it/diretta/padtv2/playlist.m3u8'
    thumb = 'https://www.radioradicale.it/sites/all/themes/radioradicale_2014/images/audio-400.png'
    liStyle.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=liStyle, isFolder=False)


    titolo = 'R.Radicale TV - Camera'
    liStyle = xbmcgui.ListItem(titolo, offscreen=True)
    link = 'https://video-ar.radioradicale.it/diretta/camera2/playlist.m3u8'
    thumb = 'https://www.radioradicale.it/sites/all/themes/radioradicale_2014/images/audio-400.png'
    liStyle.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=liStyle, isFolder=False)


    titolo = 'R.Radicale TV - Senato'
    liStyle = xbmcgui.ListItem(titolo, offscreen=True)
    link = 'https://video-ar.radioradicale.it/diretta/senato2/playlist.m3u8'
    thumb = 'https://www.radioradicale.it/sites/all/themes/radioradicale_2014/images/audio-400.png'
    liStyle.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=liStyle, isFolder=False)


    titolo = 'IlSole24Ore TV'
    liStyle = xbmcgui.ListItem(titolo, offscreen=True)
    link = 'https://ilsole24ore-radiovisual.akamaized.net/hls/live/2035302/persidera/master.m3u8'
    thumb = 'https://www.ilsole24ore.tv/assets/img/logo-radio24TV.png'
    liStyle.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=liStyle, isFolder=False)


    titolo = 'Radio24 TV'
    liStyle = xbmcgui.ListItem(titolo, offscreen=True)
    link = 'https://ilsole24ore-radiovisual.akamaized.net/hls/live/2035302/stream/master.m3u8'
    thumb = 'https://www.radio24.ilsole24ore.com/assets/img/splash_web-black.png'
    liStyle.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=liStyle, isFolder=False)

    xbmcplugin.endOfDirectory(handle=G.PLUGIN_HANDLE, succeeded=True)



def programmi_radio():
    titolo = 'RaiGRParlamento'
    liStyle = xbmcgui.ListItem(titolo, offscreen=True)
    link = 'https://radioparlamento-live.akamaized.net/hls/live/2032597/radioparlamento/radioparlamento/playlist.m3u8'
    thumb = 'http://db.radioline.fr/pictures/radio_994f2bf74254de17bb2c096c0cbf9e21/logo200.jpg'
    liStyle.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
    liStyle.setInfo('music', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=liStyle, isFolder=False)


    titolo = 'RadioRadicale'
    liStyle = xbmcgui.ListItem(titolo, offscreen=True)
    link = 'https://live.radioradicale.it/live.mp3'
    thumb = 'https://www.radioradicale.it/sites/all/themes/radioradicale_2014/images/audio-400.png'
    liStyle.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
    liStyle.setInfo('music', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=liStyle, isFolder=False)


    titolo = 'R.Radicale - Camera'
    liStyle = xbmcgui.ListItem(titolo, offscreen=True)
    link = 'https://live.radioradicale.it/camera.mp3'
    thumb = 'https://www.radioradicale.it/sites/all/themes/radioradicale_2014/images/audio-400.png'
    liStyle.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
    liStyle.setInfo('music', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=liStyle, isFolder=False)


    titolo = 'R.Radicale - Senato'
    liStyle = xbmcgui.ListItem(titolo, offscreen=True)
    link = 'https://live.radioradicale.it/senato.mp3'
    thumb = 'https://www.radioradicale.it/sites/all/themes/radioradicale_2014/images/audio-400.png'
    liStyle.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
    liStyle.setInfo('music', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=liStyle, isFolder=False)


    titolo = 'RadioPopolare'
    liStyle = xbmcgui.ListItem(titolo, offscreen=True)
    link = 'https://livex.radiopopolare.it/radiopop2'
    thumb = 'https://www.radiopopolare.it/wp-content/uploads/2019/08/icon-logo@2x-1.png'
    liStyle.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
    liStyle.setInfo('music', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=liStyle, isFolder=False)

    
    titolo = 'Radio24'
    liStyle = xbmcgui.ListItem(titolo, offscreen=True)
    link = 'https://ilsole24ore-radio.akamaized.net/hls/live/2035301/radio24/playlist.m3u8'
    thumb = 'https://www.radio24.ilsole24ore.com/assets/img/splash_web-black.png'
    liStyle.setArt({'thumb': thumb, 'fanart': G.FANART_PATH})
    liStyle.setInfo('music', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=G.PLUGIN_HANDLE, url=link, listitem=liStyle, isFolder=False)

    xbmcplugin.endOfDirectory(handle=G.PLUGIN_HANDLE, succeeded=True)


def run(argv):
    """ Addon entry point """
    G.init_globals(argv)

    if G.MODE == "camera":
        programmi_camera()

    elif G.MODE == "senato":
        programmi_senato()

    elif G.MODE == "tv":
        programmi_tv()

    elif G.MODE == "radio":
        programmi_radio()

    else:
        show_root_menu()
