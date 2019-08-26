# -*- coding: utf-8 -*-
import os
import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import urllib
import urlparse


addon = xbmcaddon.Addon()
language = addon.getLocalizedString
handle = int(sys.argv[1])
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}
titolo_global = ''
fanart_path = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'resources', 'fanart.jpg')




def parameters_string_to_dict(parameters):
    paramDict = dict(urlparse.parse_qsl(parameters[1:]))
    return paramDict


def show_root_menu():
    ''' Show the plugin root menu '''
    liStyle = xbmcgui.ListItem('[B]'+language(32001)+'[/B]')
    liStyle.setArt({ 'thumb': 'https://www.camera.it/application/xmanager/projects/leg18/img/header/logo_camera.jpg', 'fanart' : fanart_path })
    addDirectoryItem_nodup({"mode": "camera"},liStyle)

    liStyle = xbmcgui.ListItem('[B]'+language(32002)+'[/B]')
    liStyle.setArt({ 'thumb': 'https://www.senato.it/application/xmanager/projects/leg18/img/home2017/logo-senato-home.png', 'fanart' : fanart_path })
    addDirectoryItem_nodup({"mode": "senato"},liStyle)

    liStyle = xbmcgui.ListItem('[B]'+language(32003)+'[/B]')
    liStyle.setArt({ 'thumb': 'https://media.cdnandroid.com/97/fe/ae/31/imagen-radio-radicale-tv-0big.jpg', 'fanart' : fanart_path })
    addDirectoryItem_nodup({"mode": "radicaletv"},liStyle, folder=False)

    liStyle = xbmcgui.ListItem('[B]'+language(32004)+'[/B]')
    liStyle.setArt({ 'thumb': 'http://www.appsgeyser.com/blog/wp-content/uploads/2016/12/social-radio-icon-3.png', 'fanart' : fanart_path })
    addDirectoryItem_nodup({"mode": "radio"},liStyle)

    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)


def addDirectoryItem_nodup(parameters, li, title=titolo_global, folder=True):
    url = sys.argv[0] + '?' + urllib.urlencode(parameters, 'utf-8')
    #xbmc.log('LIST------: '+str(url),xbmc.LOGNOTICE)
    if not folder:
        li.setInfo('video', {})
        li.setProperty('isPlayable', 'true')
    return xbmcplugin.addDirectoryItem(handle=handle, url=url, listitem=li, isFolder=folder)


def play_video(link_video,live):
    listitem =xbmcgui.ListItem(titolo_global)
    listitem.setInfo('video', {'Title': titolo_global})
    if link_video == '':
        xbmc.log('NO VIDEO LINK',xbmc.LOGNOTICE)
        if xbmcgui.Dialog().ok(addon.getAddonInfo('name'), language(32005)):
            exit()
    else:
        listitem.setProperty('inputstreamaddon','inputstream.adaptive')
        listitem.setProperty('inputstream.adaptive.manifest_type','hls')
        listitem.setPath(link_video)
        xbmcplugin.setResolvedUrl(handle, True, listitem)


def programmi_camera():
    titolo = 'Camera - Canale Assemblea'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'plugin://plugin.video.youtube/?action=play_video&videoid=_pjPv7dS-_w'
    thumb = 'https://webtv.camera.it/system/events/thumbnails/000/014/843/large/AULAXVIIIC.gif?1566771620'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'Camera - Canale Satellitare'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'plugin://plugin.video.youtube/?action=play_video&videoid=WVjdPb7F4uY'
    thumb = 'https://webtv.camera.it/assets/thumbs/flash_7/2019/EI_20190520_ch4_14419.jpg'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)


def programmi_senato():
    titolo = 'Senato - Web TV 1'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'http://senato-live.morescreens.com/senato-live/ngrp:webtv1_all/playlist.m3u8?DVR'
    thumb = 'http://prd-static-senato.spectar.tv/rev-1544534780/uploads/1/video_thumbnails/upload_318_3763.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'Senato - Web TV 2'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'http://senato-live.morescreens.com/senato-live/ngrp:webtv2_all/playlist.m3u8?DVR'
    thumb = 'http://prd-static-senato.spectar.tv/rev-1544534780/uploads/1/video_thumbnails/upload_471_3766.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'Senato - Web TV 3'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'http://senato-live.morescreens.com/senato-live/ngrp:webtv3_all/playlist.m3u8?DVR'
    thumb = 'http://prd-static-senato.spectar.tv/rev-1544534780/uploads/1/video_thumbnails/upload_390_3769.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'Senato - Web TV 4'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'http://senato-live.morescreens.com/senato-live/ngrp:webtv4_all/playlist.m3u8?DVR'
    thumb = 'http://prd-static-senato.spectar.tv/rev-1544534780/uploads/1/video_thumbnails/upload_569_3772.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)


def programmi_radio():
    titolo = 'Rai GR Parlamento'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'https://grparlamento1-lh.akamaihd.net/i/grparlamento1_1@586839/master.m3u8'
    thumb = 'http://db.radioline.fr/pictures/radio_994f2bf74254de17bb2c096c0cbf9e21/logo200.jpg'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'Radio Radicale'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'https://live.radioradicale.it/live.mp3'
    thumb = 'https://www.radioradicale.it/sites/all/themes/radioradicale_2014/images/audio-400.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'Radio Radicale Camera'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'https://live.radioradicale.it/camera.mp3'
    thumb = 'https://www.radioradicale.it/sites/all/themes/radioradicale_2014/images/audio-400.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'Radio Radicale Senato'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'https://live.radioradicale.it/senato.mp3'
    thumb = 'https://www.radioradicale.it/sites/all/themes/radioradicale_2014/images/audio-400.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)





# Main
params = parameters_string_to_dict(sys.argv[2])
mode = str(params.get("mode", ""))
titolo_global=str(params.get("titolo", ""))


if params.get("page", "")=="":
    pagenum=0
else:
    pagenum=int(params.get("page", ""))

if mode=="camera":
    programmi_camera()

elif mode=="senato":
    programmi_senato()

elif mode=="radicaletv":
    titolo_global=language(32003)
    play_video('https://video.radioradicale.it/liverr/padtv2/playlist.m3u8',True)

elif mode=="radio":
    programmi_radio()

else:
    show_root_menu()
