---
title: 'A Taxonomy of Attacks Using BGP Blackholing'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin
  - Cristel Pelsser

# Author notes (optional)
author_notes: []

date: '2019-09-23T00:00:00Z'

# Schedule page publish date (NOT publication's date).
publishDate: '2021-06-20T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *[European Symposium on Research in Computer Security](https://esorics2019.uni.lu) (ESORICS 2019), (pp. 107-127), Luxembourg*
publication_short: In *ESORICS2019*

abstract: "BGP blackholing is a common technique used to mitigate DDoS attacks. Generally, the victim sends in a request for traffic to the attacked IP(s) to be dropped. Unfortunately, remote parties may misuse blackholing and send requests for IPs they do not own, turning a defense technique into a new attack vector. As DDoS attacks grow in number, blackholing will only become more popular, creating a greater risk this service will be exploited. In this work, we develop a taxonomy of attacks combining hijacks with blackholing: BGP blackjacks (blackhole hijacks). We show that those attacks effectively grant more reach and stealth to the attacker than regular hijacks, and assess the usability of those attacks in various security deployments. We then find that routing security mechanisms for BGP do not provide an adequate protection against some of those attacks, and propose additional mechanisms to properly defend against or mitigate them."

# Summary. An optional shortened abstract.
summary: []

tags:
  - BGP
  - Security
  - Blackholing
  - DDoS
  - Communities
  - Hijacks
  - Leaks

# Display this page in the Featured widget?
featured: true

# Standard identifiers for auto-linking
hugoblox:
  ids:
    doi: 10.1007/978-3-030-29959-0_6

# Custom links
links:
  # - type: pdf
  #   url: ""
  # - type: code
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  # - type: dataset
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  - type: slides
    url: a-taxonomy-of-attacks-using-bgp-blackholing-slides.pdf
  # - type: source
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  # - type: video
  #   url: https://youtube.com

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Image credit: [**ESORICS2019**](https://esorics2019.uni.lu/photos/)'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---