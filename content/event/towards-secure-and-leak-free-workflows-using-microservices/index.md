---
title: Towards Secure and Leak-Free Workflows Using Microservice Isolation

event: International Conference on High-Performance Switching and Routing
event_url: https://hpsr2021.ieee-hpsr.org/

location: Paris
address:
  street: 34 rue de Fleurus
  city: Paris
  region: Île-de-France
  postcode: 75006
  country: France

summary: []
abstract: "Companies like Netflix increasingly use the cloud to deploy their business processes. Those processes often involve partnerships with other companies, and can be modeled as workflows. This shift towards the cloud environment has led to more and more data leaks and breaches, resulting in huge losses of money for businesses like the movie industry, as well as a loss of user privacy for businesses dealing with user data like the pharmaceutical industry. In this paper, we show how those workflows can be enforced while preventing data exposure. Following the principles of zero-trust, we develop an infrastructure using the isolation provided by a microservice architecture, to enforce owner policy. We show that our infrastructure is resilient to the set of attacks considered in our security model. We implement a simple, yet realistic, workflow with our infrastructure in a publicly available proof of concept. We then verify that the specified policy is correctly enforced by testing the deployment for policy violations, and estimate the overhead cost of authorization."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2021-06-08T17:15:00Z'
date_end: '2021-06-08T17:30:00Z'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2021-06-20T00:00:00Z'

authors:
  - admin
  - Pascal Mérindol
  - Antoine Gallais
  - Cristel Pelsser

tags:
  - Data leak
  - Data breach
  - Workflow
  - Microservices
  - Authorization
  - Security

# Is this a featured talk? (true/false)
featured: false

image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/fr/photos/statue-en-beton-blanc-dun-homme-PEWUJV_saKI)'
  focal_point: ''

links:
  # - type: code
  #   url: https://github.com
  - type: slides
    url: towards-secure-and-leak-free-workflows-using-microservices-slides.pdf
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