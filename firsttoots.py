# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 18:02:35 2017

@author: vrbox
"""

from mastodon import Mastodon

mastodon = Mastodon(
    client_id = 'toot1000_clientcred.secret',
    access_token = 'toot1000_usercred.secret',
    api_base_url = 'https://social.coop'
)

firsttoot = mastodon.toot('Tooting from python using #mastodonpy !')

toot2 = mastodon.status_post('Wow that was really easy. Thanks, @halcy@icosahedron.website!',
                             in_reply_to_id = firsttoot['id'])