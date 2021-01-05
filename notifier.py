import os

# The notifier function
def notify(title, subtitle, message, link):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    url = '-open '+link
    os.system('terminal-notifier {}'.format(' '.join([m, t, s, url])))
