---
title: "Towards Secure and Leak-Free Workflows Using Microservice Isolation"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin
  - Pascal Mérindol
  - Antoine Gallais
  - Cristel Pelsser

# Author notes (optional)
author_notes: []

date: '2021-06-07T00:00:00Z'

# Schedule page publish date (NOT publication's date).
publishDate: '2021-06-20T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *[International Conference on High-Performance Switching and Routing](https://hpsr2021.ieee-hpsr.org/) (HPSR 2021), Paris*
publication_short: In *HPSR2021*

abstract: "Companies like Netflix increasingly use the cloud to deploy their business processes. Those processes often involve partnerships with other companies, and can be modeled as workflows. This shift towards the cloud environment has led to more and more data leaks and breaches, resulting in huge losses of money for businesses like the movie industry, as well as a loss of user privacy for businesses dealing with user data like the pharmaceutical industry. In this paper, we show how those workflows can be enforced while preventing data exposure. Following the principles of zero-trust, we develop an infrastructure using the isolation provided by a microservice architecture, to enforce owner policy. We show that our infrastructure is resilient to the set of attacks considered in our security model. We implement a simple, yet realistic, workflow with our infrastructure in a publicly available proof of concept. We then verify that the specified policy is correctly enforced by testing the deployment for policy violations, and estimate the overhead cost of authorization."

# Summary. An optional shortened abstract.
summary: []

tags:
  - Data leak
  - Data breach
  - Workflow
  - Microservices
  - Authorization
  - Security

# Display this page in the Featured widget?
featured: false

# Standard identifiers for auto-linking
hugoblox:
  ids:
    doi: 10.1109/HPSR52026.2021.9481820

# Custom links
links:
  # - type: pdf
  #   url: ""
  # - type: code
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  # - type: dataset
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  - type: slides
    url: towards-secure-and-leak-free-workflows-using-microservices-slides.pdf
  # - type: source
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  # - type: video
  #   url: https://youtube.com

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/fr/photos/statue-en-beton-blanc-dun-homme-PEWUJV_saKI)'
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

Best Paper Award "Short Track Student".