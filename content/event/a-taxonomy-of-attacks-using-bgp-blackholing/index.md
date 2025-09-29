---
title: A Taxonomy of Attacks Using BGP Blackholing

event: European Symposium on Research in Computer Security
event_url: https://esorics2019.uni.lu

location: Luxembourg
address:
  street: 120 route d’Echternach
  city: Luxembourg
  region: ""
  postcode: 'L-1453'
  country: Luxembourg

summary: []
abstract: 'BGP blackholing is a common technique used to mitigate DDoS attacks. Generally, the victim sends in a request for traffic to the attacked IP(s) to be dropped. Unfortunately, remote parties may misuse blackholing and send requests for IPs they do not own, turning a defense technique into a new attack vector. As DDoS attacks grow in number, blackholing will only become more popular, creating a greater risk this service will be exploited. In this work, we develop a taxonomy of attacks combining hijacks with blackholing: BGP blackjacks (blackhole hijacks). We show that those attacks effectively grant more reach and stealth to the attacker than regular hijacks, and assess the usability of those attacks in various security deployments. We then find that routing security mechanisms for BGP do not provide an adequate protection against some of those attacks, and propose additional mechanisms to properly defend against or mitigate them.'

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2019-09-23T10:55:00Z'
date_end: '2019-09-23T11:20:00Z'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2021-06-20T00:00:00Z'

authors:
  - admin
  - Cristel Pelsser

tags:
  - BGP
  - Security
  - Blackholing
  - DDoS
  - Communities
  - Hijacks
  - Leaks

# Is this a featured talk? (true/false)
featured: false

image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
  focal_point: ''

links:
  # - type: code
  #   url: https://github.com
  - type: slides
    url: a-taxonomy-of-attacks-using-bgp-blackholing-slides.pdf
  # - type: video
  #   url: https://youtube.com

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---