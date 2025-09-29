---
title: Securing Workflows Using the Microservices Architecture

event: Network Traffic Measurement and Analysis conference
event_url: 'https://tma.ifip.org/2019'

location: Paris
address:
  street: 292 rue Saint-Martin
  city: Paris
  region: Île-de-France
  postcode: 75003
  country: France

summary: []
abstract: "Ongoing efforts in the security community have tried to achieve desirable security properties, such as secure data at rest and in transport, policy enforcement, and data leak prevention for many years. Those efforts culminated in the design of security protocols and infrastructures such as the Transport Security Layer (TLS) protocol, or the Public Key Infrastructure, as well as policy enforcement mechanisms such as the eXtensible Access Control Markup Language (XACML), Access Control Lists (ACLs), firewall rules and many more. All those security mechanisms quickly become very hard to configure, manage and monitor, as well as losing flexibility over time, especially in the context of a workflow. In addition to the complexity of such a system, data leaks occur more and more often. Those leaks are perceived as huge losses of money for businesses like the movie industry, and must be prevented in order to achieve a truly secure workflow system. In order to achieve all those desirable security properties, we turn to the world of microservices, which can provide us with all those security benefits while maintaining a streamlined design and flexibility. This containerized environment allows service streamlining, while container orchestrators and service meshes allow us to create and manage identities and policies, as well as having a flexible telemetry system in the form of tracing, monitoring and logging. One thing the microservice architecture does not solve is the verification of the correctness of policies, a problem we are aiming to demonstrate and solve. This work presents how the microservice architecture can help us achieve a secure and leak-free workflow."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2019-06-20T13:00:00Z'
date_end: '2020-06-20T14:30:00Z'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2021-06-20T00:00:00Z'

authors:
  - admin
  - Pascal Mérindol
  - Antoine Gallais
  - Cristel Pelsser

tags:
  - Workflow
  - Security
  - Data leak
  - Microservices
  - Access control

# Is this a featured talk? (true/false)
featured: false

image:
  caption: 'Image credit: **Loïc Miller**'
  focal_point: ''

links:
  # - type: code
  #   url: https://github.com
  - type: poster
    url: securing-workflows-using-microservices-poster.pdf
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