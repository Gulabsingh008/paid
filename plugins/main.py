a

    ��g�6  �                   @   s  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZ	d dl
mZ d dlm
Z
mZmZmZmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZmZ d d	lmZ d d
lmZ d dlm Z  d dl!m"Z" d d
lm#Z#m$Z$ d dl%m&Z& ede
eed�Z'e�(� Z)e)j*ddd�dd� �Z+dd� Z,e'�-e�.dg��eed�dd��Z/e'�-e�.d��dd� �Z0e'�-e�.dg��eed�d d��Z/d!d"� Z1e2d#k�re3d$� d%d&� Z4d'd(� Z5e�6� Z7zFz$e7�8e4� � e7�8e5� � e7�9�  W n e:�y�   Y n0 W e7�;�  n
e7�;�  0 dS ))�    N)�progress_bar)�API_ID�API_HASH�	BOT_TOKEN�WEBHOOK�PORT)�
ClientSession)�listen)�getstatusoutput)�web)�Client�filters)�Message)�	FloodWait)�StickerEmojiInvalid)�message)�InlineKeyboardButton�InlineKeyboardMarkup)�Ashu�bot)Zapi_idZapi_hashZ	bot_token�/T)Z
allow_headc                 �   s
   t �d�S )Nz$https://github.com/AshutoshGoswami24)r   Z
json_response)Zrequest� r   �m2.py�root_route_handler!   s    r   c                  �   s   t jdd�} | �t� | S )Ni���)Zclient_max_size)r   ZApplicationZ
add_routes�routes)Zweb_appr   r   r   �
web_server&   s    
r   �start�r   �mc                 �   s6   |j tjttddd�gtddd�gg�d�I d H  d S )Nu5   ✜ ᴀsʜᴜᴛᴏsʜ ɢᴏsᴡᴀᴍɪ 𝟸𝟺 ✜zhttps://t.me/AshutoshGoswami24)�urlu+   🦋 𝐅𝐨𝐥𝐥𝐨𝐰 𝐌𝐞 🦋zhttps://t.me/AshuSupport)Zreply_markup)�
reply_textr   Z
START_TEXTr   r   r   r   r   r   �
account_login,   s    �����r!   �stopc                 �   s0   |� dd�I d H  tjtjtjgtj�R �  d S )Nu$   ♦ 𝐒𝐭𝐨𝐩𝐩𝐞𝐭 ♦T)r    �os�execl�sys�
executable�argv)�_r   r   r   r   �restart_handler=   s    r)   Zuploadc           1      �   s�	  |� d�I d H }| �|jj�I d H }|�� I d H }|�d�I d H  d|jj� �}zjt|d��}|�� }W d   � n1 sz0    Y  |�d�}g }|D ]}	|�	|	�dd�� q�t
�|� W n(   |� d�I d H  t
�|� Y d S 0 |�d	t
|�� d
��I d H  | �|jj�I d H }
|
j}|
�d�I d H  |�d�I d H  | �|jj�I d H }|j}
|�d�I d H  |�tj�I d H  | �|jj�I d H }|j}|�d�I d H  zh|dk�r�d
}nT|dk�r�d}nD|dk�r�d}n4|dk�r�d}n$|dk�r�d}n|dk�rd}nd}W n t�y    d}Y n0 |�tj�I d H  | �|jj�I d H }|j}|�d�I d H  d}|dk�rr|}n|}|�tj�I d H  | �|jj�I d H  }}|j}|�d�I d H  |�� I d H  |j}|�d��s�|�d��r�td|� d�� d}n|d k t
|�dk�rd}nt|�}�zRt|d t
|��D �]8}	||	 d �d!d"��d#d$��d%d&��d'd&�}d| }d(|v �r:t� 4 I d H ��}|j|d)d*d+d,d+d-d.d/d0d1d2d3d4d5d6�d7�4 I d H �8}|�� I d H }t�d8|��d�}W d   �I d H  �q
1 I d H �s 0    Y  W d   �I d H  �q1 I d H �s.0    Y  n�d9|v �rftjd:|� �d;d<id7��� d= }n�d>|v �s�d?|v �s�d9|v �s�d@|v �r�dAd<dBdCdDdEdFdGdH�}d=|� ff} tjdI|| dJ�}!|!�� d= }nJdK|v �r�|�dL�dM }"dN|" dO }n$dP|v �r|�dL�dM }"dQ|" dR }||	 dS �dTd&��dUd&��dLd&��dVd&��dWd&��dXd&��dYd&��dZd&��d[d&��d\d&��d]d&�� � }#t!|��"d^�� d_|#d d`� � �}$da|v �r�db|� dc|� dd�}%ndb|� de|� df�}%dg|v �r�dh|$� di|� dj|� dk�}&n�da|v �rdl|� dm|� dn|$� dk�}&n�do|v �r<dp|%� dq|� dn|$� dk�}&n�dr�sLds|v �rfdp|%� dt|� dn|$� dk�}&n\|%duk�szdv|v �r�dp|%� dt|� dn|$� dk�}&n.dw�s�dx|v �r�dy}&ndp|%� dz|� dn|$� dk�}&�zJd{t!|��"d^�� d||#� d}|
� d~|� d{�	}'d{t!|��"d^�� d||#� d|
� d~|� d{�	}(d�|v �r�zLt#�||$�I d H })| j$|jj|)|(d��I d H }*|d7 }t
�|)� t%�&d� W nV t'�y� }+ z<|� t!|+��I d H  t%�&|+j(� W Y d }+~+W �q2W Y d }+~+n
d }+~+0 0 �nDdw|v �r�zbdh|$� d�|� dk�}&|&� d��},t
�)|,� | j$|jj|$� dw�|(d��I d H }*|d7 }t
�|$� dw�� W nV t'�y� }+ z<|� t!|+��I d H  t%�&|+j(� W Y d }+~+W �q2W Y d }+~+n
d }+~+0 0 n~d�|$� d�|� d�|� d��}-|� |-�I d H }.t#�*||&|$�I d H }/|/}0|.�d�I d H  t#�+| ||'|0||$|.�I d H  |d7 }t%�&d� W nZ t�	yh }+ z@|� d�t!|+�� d�|$� d�|� ��I d H  W Y d }+~+�q2W Y d }+~+n
d }+~+0 0 �q2W n6 t�	y� }+ z|� |+�I d H  W Y d }+~+n
d }+~+0 0 |� d��I d H  d S )�Nu(   sᴇɴᴅ ᴍᴇ .ᴛxᴛ ғɪʟᴇ  ⏍Tz./downloads/�r�
z://�   uG   ∝ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐟𝐢𝐥𝐞 𝐢𝐧𝐩𝐮𝐭.u8   ɪɴ ᴛxᴛ ғɪʟᴇ ᴛɪᴛʟᴇ ʟɪɴᴋ 🔗** **uo   **

sᴇɴᴅ ғʀᴏᴍ  ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛᴀʟ ɪs 1uz   ∝ 𝐍𝐨𝐰 𝐏𝐥𝐞𝐚𝐬𝐞 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞Z144Z256x144Z240Z426x240Z360Z640x360Z480Z854x480Z720Z1280x720Z1080Z	1920x1080ZUNu   ️ ⁪⁬⁮⁮⁮ZRobinzhttp://zhttps://zwget 'z' -O 'thumb.jpg'z	thumb.jpgZnozfile/d/zuc?export=download&id=zwww.youtube-nocookie.com/embedzyoutu.bez?modestbranding=1� z/view?usp=sharingZ	visioniasz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zen-US,en;q=0.9zno-cachez
keep-alivezhttp://www.visionias.in/ZiframeZnavigatez
cross-site�1zuMozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36z("Chromium";v="107", "Not=A?Brand";v="24"z?1z	"Android")ZAcceptzAccept-Languagez
Cache-ControlZ
ConnectionZPragmaZRefererzSec-Fetch-DestzSec-Fetch-ModezSec-Fetch-SitezUpgrade-Insecure-Requestsz
User-Agentz	sec-ch-uazsec-ch-ua-mobilezsec-ch-ua-platform)�headersz(https://.*?playlist.m3u8.*?)\"zvideos.classplusappzChttps://api.classplusapp.com/cams/uploader/video/jw-signed-url?url=�x-access-tokenZ\eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9r   ztencdn.classplusappz media-cdn-alisg.classplusapp.comzmedia-cdn.classplusappzapi.classplusapp.comzMobile-Androidz1.4.37.1Z18Z5d0d17ac8b3c9f51z(2848b866799971ca_2848b8667a33216c_SDK-30Zgzip)ZHostr0   z
user-agentzapp-versionzapi-versionz	device-idzdevice-detailszaccept-encodingz>https://api.classplusapp.com/cams/uploader/video/jw-signed-url)r/   �paramsz/utkarshapp.mpdr   �����z$https://apps-s3-prod.utkarshapp.com/z/utkarshapp.comz/master.mpdz&https://d26g5bnklkwsh4.cloudfront.net/z/master.m3u8r   �	�:�+�#�|�@�*�.ZhttpsZhttp�   z) �<   Zyoutuz
b[height<=z][ext=mp4]/bv[height<=z!][ext=mp4]+ba[ext=m4a]/b[ext=mp4]z
]/bv[height<=z]+ba/b/bv+baZacecwplyzyt-dlp -o "z" -f "bestvideo[height<=zQ]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "�"z yt-dlp -i -f "bestvideo[height<=z=]+bestaudio" --no-keep-video --remux-video mkv --no-warning "z" -o "zplayer.vimeozyt-dlp -f "z/+bestaudio" --no-keep-video --remux-video mkv "Zm3u8Z
livestreamz%" --no-keep-video --remux-video mkv "�0�unknownz.pdf�downloadZpdfzC+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "z**z. u   .mkv

Batch Name  » u   

Downloaded By » u   .pdf

Batch Name  » Zdrive)Zchat_idZdocumentZcaptionz.pdf" "z -R 25 --fragment-retries 25uZ   **❊⟱ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ⟱❊ »

📝 𝐍𝐚𝐦𝐞 » u!   
⌨ 𝐐𝐮𝐥𝐢𝐭𝐲 » u   

🔗 𝐔𝐑𝐋 »** `�`uZ   ⌘ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐈𝐧𝐭𝐞𝐫𝐮𝐩𝐭𝐞𝐝
u   
⌘ 𝐍𝐚𝐦𝐞 » u   
⌘ 𝐋𝐢𝐧𝐤 » uE   ✅ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐃𝐨𝐧𝐞),r    r	   Zchat�idr@   �delete�open�read�split�appendr#   �removeZedit�len�textr   ZQ1_TEXT�	ExceptionZC1_TEXTZT1_TEXT�
startswithr
   �int�range�replacer   �get�re�search�group�requests�json�strip�str�zfill�helperZ
send_document�time�sleepr   �x�systemZdownload_videoZsend_vid)1r   r   Zeditable�inputr\   �path�fZcontentZlinks�iZinput0Zraw_textZinput1Z	raw_text0Zinput2Z	raw_text2�resZinput3Z	raw_text3ZhighlighterZMRZinput6r   Z	raw_text6Zthumb�count�Vr   ZsessionZresprJ   r/   r1   ZresponserB   Zname1�nameZytf�cmdZccZcc1Zka�copy�eZdownload_cmdZShow�progZres_file�filenamer   r   r   r!   C   s�   &

�








�����
���b
��������
�

��������	�
��� 



((

�
*


�(�
,&c                  �   sV   t rRt� I d H } t�| �}|�� I d H  t�|dt�}|�� I d H  tdt� �� d S )Nz0.0.0.0zWeb server started on port )	r   r   r   Z	AppRunnerZsetupZTCPSiter   r   �print)ZappZrunnerZsiter   r   r   �main@  s    
rl   �__main__u�  
    █░█░█ █▀█ █▀█ █▀▄ █▀▀ █▀█ ▄▀█ █▀▀ ▀█▀     ▄▀█ █▀ █░█ █░█ ▀█▀ █▀█ █▀ █░█   
    ▀▄▀▄▀ █▄█ █▄█ █▄▀ █▄▄ █▀▄ █▀█ █▀░ ░█░     █▀█ ▄█ █▀█ █▄█ ░█░ █▄█ ▄█ █▀█ c                   �   s   t �� I d H  d S �N)r   r   r   r   r   r   �	start_botS  s    ro   c                   �   s   t � I d H  d S rn   )rl   r   r   r   r   �	start_webV  s    rp   )<r#   rQ   r%   rU   rZ   ZasynciorT   �
subprocessZcorerY   Zutilsr   �varsr   r   r   r   r   Zaiohttpr   Zpyromodr	   r
   r   Zpyrogramr   r
   Zpyrogram.typesr   Zpyrogram.errorsr   Z*pyrogram.errors.exceptions.bad_request_400r   Z!pyrogram.types.messages_and_mediar   r   r   Zstyler   r   Z
RouteTableDefr   rP   r   r   Z
on_messageZcommandr!   r)   rl   �__name__rk   ro   rp   Zget_event_loopZloopZcreate_taskZrun_forever�KeyboardInterruptr"   r   r   r   r   �<module>   s`   

 }
�
