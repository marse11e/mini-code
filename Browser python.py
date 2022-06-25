import webbrowser

webbrowser.open('https://yandex.ru/', new=2)
# webbrowser.get(using='google-chrome').open_new_tab('https://yandex.ru/')



# Type Name             |       Class Name

# 'mozilla'	                    Mozilla('mozilla')
# 'firefox'	                    Mozilla('mozilla')
# 'netscape'	                Mozilla('netscape')
# 'galeon'	                    Galeon('galeon')
# 'epiphany''	                Galeon('epiphany')
# 'skipstone'	                BackgroundBrowser('skipstone')
# 'kfmclient'	                Konqueror()
# 'konqueror''	                Konqueror()
# 'kfm'	                        Konqueror()
# 'mosaic'	                    BackgroundBrowser('mosaic')
# 'opera'	                    Opera()
# 'grail'	                    Grail()
# 'links'	                    GenericBrowser('links')
# 'elinks'	                    Elinks('elinks')
# 'lynx'	                    GenericBrowser('lynx')
# 'w3m'	                        GenericBrowser('w3m')
# 'windows-default'	            WindowsDefault
# 'macosx'	                    MacOSX('default')
# 'safari'	                    MacOSX('safari')
# 'google-chrome'	            Chrome('google-chrome')
# 'chrome''	                    Chrome('chrome')
# 'chromium''	                Chromium('chromium')
# 'chromium-browser'            Chromium('chromium-browser')




# Но не всегда получается обойтись одним только .get() и в этом случае на помощь приходит функция .register(), например:
# import webbrowser
# webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
# webbrowser.get('Chrome').open_new_tab('https://yandex.ru/')

